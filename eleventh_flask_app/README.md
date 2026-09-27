# Eleventh Flask App

A Flask and SQLite practice application for collecting participant details and displaying the saved participant list.

## Requirements

Install Flask in your virtual environment:

```powershell
pip install Flask
```

## Run

From the repository root, run:

```powershell
flask --app eleventh_flask_app.app run --debug
```

Open `http://127.0.0.1:5000/` in a browser. SQLite stores participant data in `database.db` in the current working directory.

## Routes

- `GET /` and `GET /home` display the home page.
- `GET /join` displays the participant form.
- `POST /join` saves a participant's name, email, city, country, and phone number.
- `GET /participants` displays the saved participants.