# Laboratory Work 7 - Console Application

## Goal of the Work

The purpose of this laboratory work is to combine all previous laboratory works into one interactive console application.

The application demonstrates:

- object-oriented programming
- collections
- inheritance
- interfaces
- strategies
- typing
- exception handling
- file storage
- CLI interaction

---

# Project Structure

## main.py

Application entry point.

Starts the CLI application.

---

## cli.py

Responsible for:

- menu
- input/output
- user interaction

No business logic is implemented here.

---

## app.py

Contains business logic:

- adding users
- deleting users
- searching
- sorting
- filtering

---

## exceptions.py

Contains custom exceptions:

- UserNotFoundError
- DuplicateUserError

---

## storage.py

Responsible for:

- saving users to JSON
- loading users from JSON

---

# CLI Description

Implemented menu options:

1. Add user
2. Show all users
3. Find user
4. Delete user
5. Sort users
0. Exit

The application works in a loop until the user exits.

Invalid input is handled using try/except.

Data is automatically saved on exit and loaded on startup.

---

# Demonstration

## Scenario 1

Program startup and automatic data loading.

---

## Scenario 2

Adding and deleting users with confirmation.

---

## Scenario 3

Sorting users using different strategies.

---

## Scenario 4

Exception handling and invalid input processing.

---

# Conclusion

In this laboratory work we studied:

- modular architecture
- CLI applications
- exception handling
- JSON storage
- type annotations
- separation of layers