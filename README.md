# Asset Catalog API

## Overview

A backend API for cataloging game development assets.

This project is being built to learn backend development concepts such as:
- REST APIs
- HTTP requests
- Databases
- Authentication
- API design
- Documentation

## Current Status

In development.

Current progress:
- [x] Project setup
- [x] Virtual environment
- [x] FastAPI installation
- [x] First API endpoint
- [x] Asset model
- [x] CRUD operations
- [ ] Database integration

## Current Features

- Create assets
- Retrieve all assets
- Retrieve individual assets by ID
- Update asset metadata
- Delete assets
- Automatic ID generation
- Automatic version tracking
- HTTP error handling

## Goals

The long-term goal is to create a service that allows game developers to:

- Create projects
- Track assets
- Organize assets by type
- Search assets
- Manage metadata

## Tech Stack

- Python
- FastAPI
- Uvicorn

## Running the Project

Activate the virtual environment:

```bash
# Windows
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn main:app --reload
```

## Learning Notes

This project is intentionally being developed as a learning exercise.
The focus is understanding backend development fundamentals rather than building the fastest possible solution.

### 2026-06-02

- Successfully created and activated a Python virtual environment
- Installed FastAPI and Uvicorn
- Created initial project structure
- Published project to GitHub
- Learned how FastAPI routes work
- Learned that URL paths are matched by route decorators such as '/' and '/assets'
- Created a GET '/assets' endpoint
- Learned that API endpoints can return JSON data
- Confirmed that FastAPI automatically converts Python dictionaries and lists into JSON responses
- Created a POST '/assets' endpoint
- Learned how to test POST requests using FastAPI's '/docs' page
- Learned that request bodies are sent as JSON
- Confirmed that 'GET /assets' returns assets created by 'POST /assets'

### 2026-06-09

- Created a PUT '/assets/{id}' endpoint
- Created a DELETE '/assets{id}' endpoint
- Created a helper function to search for assets by ID
- Learned about HTTP Exception handling and 404 responses
- Learned the difference between an object instance and a class definition
- Learned the difference between creating an object and storing it in a collection
- Learned that asset IDs should not depend on list positions
- Completed CRUD operations and updating code organization