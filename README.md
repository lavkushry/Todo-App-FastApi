# Todo-App-FastApi
# Todo Application

This is a simple Todo application built with Python using the FastAPI framework. It uses SQLite as the database and SQLAlchemy as the ORM.

## Features

- User Registration
- User Authentication
- CRUD operations for Todos

## Installation

1. Clone the repository
```bash
git clone https://github.com/lavkushry/Todo-App-FastApi.git
```
1. Change the working directory
```bash
cd todo-app
```
1. Install the dependencies
```bash
pip install -r requirements.txt
``` 
1. Run the application
```bash
uvicorn main:app --reload
```
API Endpoints
POST /auth/: Register a new user
POST /auth/token: Authenticate a user and return a token
GET /todos/: Get all todos for the authenticated user
GET /todos/{todo_id}: Get a specific todo for the authenticated user
POST /todos/todo: Create a new todo for the authenticated user
PUT /todos/todo/{todo_id}: Update a specific todo for the authenticated user
DELETE /todos/todo/{todo_id}: Delete a specific todo for the authenticated user
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. 