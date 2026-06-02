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
- [ ] First API endpoint
- [ ] Asset model
- [ ] CRUD operations
- [ ] Database integration

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
    - Created my first custom API endpoint
    - Learned that API endpoints can return JSON data
    - Confirmed that FastAPI automatically converts Python dictionaries and lists into JSON responses