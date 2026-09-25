# Fifth Flask App

A Flask routing and template-rendering practice application.

## Routes

- `GET /` renders the main index page.
- `GET /home` renders the same index page.
- `GET /about` displays a list of social media sites.
- `GET /<name>` renders a personalized welcome page. For example, `/Ali` displays `Welcome, Ali`.
- `GET /contact/<role>` displays a role-specific contact message.

The index page includes a `Welcome Ali` link generated with `url_for('welcome', name='Ali')`.

## Run

From the repository root:

```powershell
flask --app fifth_flask_app.app run --debug
```

Open `http://127.0.0.1:5000/` in a browser.
