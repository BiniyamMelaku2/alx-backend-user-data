# 0x03. User authentication service

## Resources
Read or watch:

* [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
* [Requests module](https://requests.kennethreitz.org/en/master/user/quickstart/)
* [HTTP status codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)

## Setup
You will need to install `bcrypt`

> pip3 install bcrypt

# Tasks

## [0. User model](./user.py)
In this task you will create a SQLAlchemy model named `User` for a database table named `users` (by using the [mapping declaration](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#declare-a-mapping) of SQLAlchemy).

The model will have the following attributes:

* `id`, the integer primary key
* `email`, a non-nullable string
* `hashed_password`, a non-nullable string
* `session_id`, a nullable string
* `reset_token`, a nullable string

```
bob@dylan:~$ python3 main.py
users
users.id: INTEGER
users.email: VARCHAR(250)
users.hashed_password: VARCHAR(250)
users.session_id: VARCHAR(250)
users.reset_token: VARCHAR(250)
```

## [1. create user](./db.py)
complete the `DB` class provided to implement the `add_user` method.

Note that `DB._session` is a private property and hence should NEVER be used from outside the `DB` class.

Implement the `add_user` method, which has two required string arguments: `email` and `hashed_password`, and returns a `User` object. The method should save the user to the database. No validations are required at this stage.

```
bob@dylan:~$ python3 main.py
1
2
```
