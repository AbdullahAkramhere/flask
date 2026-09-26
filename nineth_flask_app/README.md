# Ninth Flask App

A Flask registration-form practice application using Bootstrap for styling. It collects an email address, password, contact number, gender, and newsletter preference, then returns the submitted form data as JSON.

## Requirements

Install Flask in your virtual environment:

```powershell
pip install Flask
```

## Run

From the repository root, run:

```powershell
flask --app nineth_flask_app.app run --debug
```

Open `http://127.0.0.1:5000/` in a browser.

## Routes

- `GET /` renders the registration form from `templates/indexx.html`.
- `POST /read-form` reads the submitted form and returns JSON containing the email, contact number, gender, newsletter choice, and a success message.

The password is read by the server for this practice example but is not included in the JSON response. The form uses Bootstrap 5.3.3 from jsDelivr for its styling.
