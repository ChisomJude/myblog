# Simple Blog Application - Local Development Guide

This guide explains how to run the Flask blog application locally on your machine for development and testing.

## Prerequisites

- Python 3.7+ installed on your system.
- pip (Python package manager).

### Step 1: Clone and Navigate to the App Directory

- Open your terminal and move into the flask_app folder:

```
cd myblog

```

### Step 2: Create a Virtual Environment

- It is best practice to use a virtual environment to manage dependencies.

**macOS / Linux:**
```
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```
python -m venv venv
venv\Scripts\activate
```

*You should see (venv) appear at the start of your terminal prompt.*

### Step 3: Install Dependencies

- Install the required Python packages listed in requirements.txt:  `pip install -r requirements.txt`


### Step 4: Initialize the Database

- The application uses SQLite. You need to create the database file (blog.db) and the tables before running the app. Run the custom Flask command defined in app.py:

```
export FLASK_APP=app.py   

# On Windows use: 

set FLASK_APP=app.py
flask init-db

```

- You should see the message: Initialized the database.

### Step 5: Run the Application

- Start the development server: `flask run`


You should see output similar to:

 

 (Press CTRL+C to quit)


### Step 6: Access the App

Open your web browser and navigate to:

http://127.0.0.1:5000

Running Tests

To run the unit tests included with the application:

pytest