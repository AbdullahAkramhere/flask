# Seventh Flask App

A simple Flask file-upload practice application. It accepts a file from a form, sanitizes the filename with Werkzeug's `secure_filename`, saves the file, and displays an acknowledgement page with the saved filename.

## Requirements

Install Flask in your virtual environment:

```powershell
pip install Flask
```

## Run

From the repository root, run:

```powershell
flask --app seven_flask_app.app run --debug
```

Open `http://127.0.0.1:5000/` in a browser.

## Usage

1. Choose a file on the upload form.
2. Select **Upload**.
3. The app submits the file to `/success` and displays its sanitized filename.

The uploaded file is saved in the application's current working directory. Run the command from the repository root so the saved file location is predictable.
