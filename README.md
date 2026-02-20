# Task Management API

A professional, secure Backend API for managing personal tasks. Built with **Django** and **Django REST Framework**.

## 🚀 Live Demo
Check out the live API documentation here: 
[https://Obinna32.pythonanywhere.com/api/docs/](https://Obinna32.pythonanywhere.com/api/docs/)

## ✨ Features
- **Custom User Model**: Uses Email instead of Username for modern authentication.
- **JWT Authentication**: Secure login using JSON Web Tokens (SimpleJWT).
- **Task CRUD**: Full Create, Read, Update, and Delete functionality for tasks.
- **Ownership Security**: Users can only see, edit, or delete tasks they created.
- **Custom Actions**: Specialized `/toggle/` endpoint for flipping task completion status.
- **API Documentation**: Interactive Swagger UI provided by `drf-spectacular`.
- **Error Handling**: Consistent JSON error responses across the entire API.
- **Logging**: Production-ready error logging.

## 🛠️ Tech Stack
- **Language**: Python 3.10+
- **Framework**: Django 4.x / 5.x
- **Toolkit**: Django REST Framework
- **Auth**: SimpleJWT (JSON Web Tokens)
- **Database**: SQLite (Development)
- **Documentation**: Swagger / OpenAPI 3.0
- **Deployment**: PythonAnywhere

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/task_management_api.git
   cd task_management_api
   ```
2. **Create and activate a virtual environment:**

```bash
python -m venv venv
.\venv\Scripts\activate
```
3. **Install dependencies and create a virtual environment:**
```bash
pip install -r requirements.txt
```
 Create a .env file and input this:
```Text
SECRET_KEY=your_secret_key
DEBUG=True
```
4. **Run migrations and start the server:**

```bash
python manage.py migrate
python manage.py runserver
```
***📖 API Endpoints***
Users
- **POST** ***/api/users/register/*** - Register a new user
- **POST** ***/api/users/token/*** - Login and receive JWT tokens
- **POST** ***/api/users/token/refresh/*** - Refresh an expired access token

**Tasks**
- **GET** ***/api/tasks/*** - List all tasks for the logged-in user
- **POST** ***/api/tasks/*** - Create a new task
- **GET** ***/api/tasks/{id}/*** - Retrieve a specific task
- **PUT** ***/api/tasks/{id}/*** - Update a task
- **DELETE** ***/api/tasks/{id}/*** - Delete a task
- **POST** ***/api/tasks/{id}/toggle/*** - Toggle task completion status
