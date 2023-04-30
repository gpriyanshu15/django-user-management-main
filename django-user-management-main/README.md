# Django User Registration API

This is a Django API for user registration with the following features:

- Create a user with a username, password, mobile, name, address, and email
- Send an email with the user's password
- Validate that the username consists of alphabets, mobile is an integer with length 10, email is valid, and password contains alphanumeric and some special character
- Allow a user to login with their username and password
- Retrieve all users from the database in JSON format

## Requirements

- Python 3.6 or above
- Django 3.1 or above
- Django REST Framework 3.12 or above

## Installation

1. Clone the repository
2. Change into the project directory: `cd django-user-registration-api`
3. Install the dependencies: `pip install -r requirements.txt`
4. Run the server: `python manage.py runserver`

## Usage

### Create a user

To create a user, make a POST request to the `/api/users/` endpoint with the following fields in the request body:

- `username`: the user's username (consisting of alphabets only)
- `password`: the user's password (containing alphanumeric and some special character)
- `mobile`: the user's mobile number (an integer with length 10)
- `name`: the user's name
- `address`: the user's address
- `email`: the user's email address (validated for correct email format)

Example request body:

```json
{
  "username": "johndoe",
  "password": "Passw0rd$",
  "mobile": 1234567890,
  "name": "John Doe",
  "address": "123 Main St",
  "email": "johndoe@example.com"
}
```

Example response:

```json
{
  "user_id": 1
}
```

### Login

To login, make a POST request to the /api/login/ endpoint with the following fields in the request body:

1. username: the user's username
2. password: the user's password

Example request body:

```json
{
  "username": "johndoe",
  "password": "Passw0rd$"
}
```

Example response:

```json
{
  "message": "Login successful"
}
```

###Retrieve all users

To retrieve all users, make a GET request to the /api/users/ endpoint.

Example response:

```json
[
  {
    "id": 1,
    "username": "johndoe",
    "password": "Passw0rd$",
    "mobile": 1234567890,
    "name": "John Doe",
    "address": "123 Main St",
    "email": "johndoe@example.com"
  }
]
```








