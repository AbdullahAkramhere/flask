# Eighth Flask App

A Flask-WTF practice application demonstrating CSRF-protected forms and Flask flash messages. The main form accepts a name and displays a success or validation message. A second POST form demonstrates handling a regular request field.

## Requirements

Install the dependencies in your virtual environment:

```powershell
pip install Flask Flask-WTF WTForms
```

## Run

From the repository root, run:

```powershell
flask --app eightth_flask_app.app run --debug
```

Open `http://127.0.0.1:5000/` in a browser.

## Routes

- `/` accepts `GET` and `POST`. It displays the Flask-WTF name form and validates its CSRF token and required name field.
- `/unprotected_form` accepts `POST` and reads the `Name` field. Because CSRF protection is enabled globally, this route also requires a valid CSRF token unless it is explicitly exempted.

The application does not save names to a database; it only displays a response or flash message for the current request.
