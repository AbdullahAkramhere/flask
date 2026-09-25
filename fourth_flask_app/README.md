# Fourth Flask App

A small Flask login practice application.

## Routes

- `GET /` displays the login form.
- `GET /login` redirects back to the login page.
- `POST /login` redirects to `/success` when the username is `admin`.
- `GET /success` displays a successful login message.

## Run

From the repository root:

```powershell
flask --app fourth_flask_app.app run --debug
```

Open `http://127.0.0.1:5000/` in a browser.

This is a learning example only. It does not implement password authentication or persistent user sessions.
