# Sixth Flask App

A Flask-WTF practice application that collects and displays a user's name, password hash, remember-me choice, salary, gender, country, message, and uploaded photo filename.

## Requirements

Install the dependencies in your virtual environment:

```powershell
pip install Flask Flask-WTF WTForms
```

## Run

From the repository root, run:

```powershell
flask --app sixth_flask_app.app run --debug
```

Open `http://127.0.0.1:5000/` in a browser.

## Form fields

- Name
- Password
- Remember me
- Salary
- Gender
- Country
- Message
- Photo upload

The application displays the submitted values after successful validation. The password is displayed as a generated hash, and the uploaded file is not saved; only its filename is displayed.
