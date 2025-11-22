import pytest
from flask_app.app import app as flask_app  # Import the app instance

@pytest.fixture
def app():
    """Create a test app instance."""
    yield flask_app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_index_loads(client):
    """Test that the index page (/) loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Blog" in response.data

def test_add_post(client):
    """Test adding a new post."""
    # First, test the redirect after posting
    response = client.post('/add', data={'title': 'Test Title', 'body': 'Test Body'}, follow_redirects=True)
    assert response.status_code == 200
    
    # Check that the new post is on the index page
    assert b"Test Title" in response.data
    assert b"Test Body" in response.data