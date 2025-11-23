import sqlite3
import click
from flask import Flask, render_template, request, g, redirect, url_for
from flask.cli import with_appcontext

DATABASE = 'blog.db'

app = Flask(__name__)
app.config['DATABASE'] = DATABASE


def get_db():
    """Connects to the specific database."""
    if 'db' not in g:
        g.db = sqlite3.connect(
            app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    """Closes the database connection."""
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    """Initializes the database from the schema."""
    db = get_db()
    with app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

# Register the init_db_command with the app
app.cli.add_command(init_db_command)
app.teardown_appcontext(close_db)

@app.route('/')
def index():
    """Show all blog posts."""
    #db = get_db(xxx) #manually added an error for testing
    db = get_db()
    posts = db.execute(
        'SELECT title, body, created FROM posts ORDER BY created DESC'
    ).fetchall()
    return render_template('index.html', posts=posts)

@app.route('/add', methods=('POST',))
def add_post():
    """Add a new post."""
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        
        if not title:
            # In a real app, you'd flash a message
            pass
        else:
            db = get_db()
            db.execute(
                'INSERT INTO posts (title, body) VALUES (?, ?)',
                (title, body)
            )
            db.commit()
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)