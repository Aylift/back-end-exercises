# Introduction

This repository consists of four django projects, which are four tasks from the list for credit in the course of 
back-end programming school subject.

### Projects:

* todo - provides API to manage tasks, each task consists of title, description, status and priority:
  * CRUD
  * Filtering by status and priority
  * Sorting by date of creation
* jwt_register - login/register system with JWT for authentication:
  * Registering users (with hashable passwords)
  * Logging in and JWT token generation
  * Middleware for JWT verification
  * Endpoint with secured path requiring token
* books - API for managing books in library. Users can add books and search for them by author or title and check availability.
  * CRUD
  * Searching books by titles and authors
  * Endpoint for checking if book is available
* url_shortener - API for shortening links, similar to bit.ly. Each link has unique, short id.
  * Storing original and shortened URL's
  * Endpoint for generating shortened link
  * Endpoint for forwarding user to original address

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ https://github.com/Aylift/back-end-exercises.git
    $ cd <one_of_four_projects>
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
Then simply apply the migrations:

    $ python manage.py migrate

You can now run the development server:

    $ python manage.py runserver

# Projects usage

After starting server, the easiest way to test endpoints is by using Postman. Below are all available
endpoints for each app, with examples of usage.

## todo
### endpoints:
* GET /api/tasks/ - list of tasks
* POST /api/tasks/ - adding a task
* Get /api/tasks/<id>/ - task details
* PUT /api/tasks/<id>/ - edit task
* DELETE /api/tasks/<id>/ - delete task
### filters:
* /api/tasks/?status=todo
* /api/tasks/?priority=high
* /api/tasks/?ordering=created_at
* /api/tasks/?ordering=-created_at
### example request:
* Header: POST /api/tasks/
* Body: {
  "title": "Zrobić zakupy",
  "description": "Kupić mleko i jajka",
  "status": "todo",
  "priority": "high"
}
## jwt_register
### endpoints:
* POST /api/register/ - user register
* POST /api/login/ - loggin in (get JWT token)
* POST /api/token/refresh/ - token refresh 
* GET /api/protected/ - access to protected path
### example request:
* Header: POST /api/register/
* Body: {
"username": "testuser",
"password": "secret123"
}
