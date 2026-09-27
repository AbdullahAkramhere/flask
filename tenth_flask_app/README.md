# Tenth Flask App

A Flask profile manager using Flask-SQLAlchemy and SQLite. It lists saved profiles, provides a form for adding a profile, and supports deleting profiles.

## Requirements

Install the dependencies in your virtual environment:

```powershell
pip install Flask Flask-SQLAlchemy
```

## Run

From the repository root, run:

```powershell
flask --app tenth_flask_app.app run --debug
```

Open `http://127.0.0.1:5000/` in a browser. The application creates its SQLite database at `tenth_flask_app/instance/site.db` when run directly with `python tenth_flask_app/app.py`.

## Routes

- `GET /` displays all profiles.
- `GET /add_data` displays the add-profile form.
- `POST /add` saves a profile and redirects to the profile list.
- `GET /delete/<id>` deletes the profile with the given ID and redirects to the profile list.

Each profile has a first name, last name, and age.