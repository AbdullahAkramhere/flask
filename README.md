# Flask Learning Apps

This repository contains six small Flask practice applications. Each app has its own README with routes and run instructions.

## 1. first_model_flask_app

An event log application using Flask-SQLAlchemy and SQLite. Users can add event descriptions, and saved events are displayed with their date and time.

Run from the repository root:

```powershell
flask --app first_model_flask_app.app run --debug
```

Open `http://127.0.0.1:5000/` in a browser.

## 2. second_flask_app

A basic Flask form application. It accepts form data on `/passing` and displays the submitted data on the result page.

Run from the repository root:

```powershell
flask --app second_flask_app.app run --debug
```

Open `http://127.0.0.1:5000/` in a browser.

## 3. third_flask_app

A square calculator. It displays a number form at `/` and calculates the square of the submitted number at `/square` using a GET query parameter.

Run from the repository root:

```powershell
flask --app third_flask_app.app run --debug
```

Open `http://127.0.0.1:5000/` in a browser, enter a number, and submit the form.

## 4. fourth_flask_app

A basic login practice application. The login form accepts the username `admin` and redirects to a success page.

Run from the repository root:

```powershell
flask --app fourth_flask_app.app run --debug
```

Open `http://127.0.0.1:5000/` in a browser.

See [fourth_flask_app/README.md](fourth_flask_app/README.md) for details.

## 5. fifth_flask_app

A routing and template-rendering application with home, about, personalized welcome, and role-based contact routes.

Run from the repository root:

```powershell
flask --app fifth_flask_app.app run --debug
```

Open `http://127.0.0.1:5000/` in a browser.

See [fifth_flask_app/README.md](fifth_flask_app/README.md) for details.

## 6. sixth_flask_app

A Flask-WTF form application that validates and displays text, password, checkbox, decimal, radio, select, text area, and file-upload fields.

Run from the repository root:

```powershell
flask --app sixth_flask_app.app run --debug
```

Open `http://127.0.0.1:5000/` in a browser.

See [sixth_flask_app/README.md](sixth_flask_app/README.md) for details.

## Setup

Create and activate a virtual environment, then install the required packages:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install Flask Flask-SQLAlchemy Flask-WTF WTForms
```

The applications should be run one at a time because they use the same default port, `5000`.
