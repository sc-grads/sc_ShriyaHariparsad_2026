# Ecommerce Website Agent Guide

## Python environment

- Use the repository's `.venv` when available. In PowerShell, activate it with `.\.venv\Scripts\Activate.ps1`.
- Run the application with `python main.py` from the repository root.
- Before reporting a Python change as complete, run `python -m compileall main.py website`.
- There is no configured test runner, formatter, linter, or dependency lockfile. Do not claim tests passed unless a test command is added or provided separately.
- Runtime dependencies are inferred from imports and include Flask, Flask-SQLAlchemy, Flask-Login, Flask-WTF, WTForms, python-dotenv, and Werkzeug. Preserve the existing environment rather than installing packages speculatively.

## Application structure

- `main.py` is the development entry point and calls `website.create_app()`.
- `website/__init__.py` owns the Flask app factory, extensions, blueprint registration, login loader, and database initialization.
- `website/views.py` contains storefront, search, cart, checkout, orders, wishlist, returns, and PayFast routes.
- `website/auth.py` contains customer and employee authentication, profile, password, and related JSON routes.
- `website/admin.py` contains employee-only product, order, return, media, and admin API routes.
- `website/models.py` contains SQLAlchemy models; `website/forms.py` contains Flask-WTF forms and validation.
- Templates live in `website/templates`; shared layout and asset loading are in `website/templates/base.html`. Static assets live in `website/static`.

## Coding conventions

- Preserve the existing Flask blueprint and SQLAlchemy patterns: route decorators, `render_template`, `db.session`, flash messages, and JSON responses.
- Use PascalCase for classes and snake_case for functions, routes, fields, and variables. Match nearby code; type annotations are not currently used.
- Authentication combines Flask-Login with `session['user_type']` to distinguish customers from employees. Preserve that contract when changing login or authorization behavior.
- Hash passwords through the existing Werkzeug-backed model properties; never store plaintext passwords.
- On database write failures, follow the local rollback and user-facing error handling patterns.

## Operational cautions

- `.env` contains secret keys, administrator bootstrap values, and PayFast credentials. Never commit, print, or expose those values.
- Creating the app is not side-effect free: startup runs `db.create_all()` and may synchronize the default employee from `.env`.
- SQLite data is stored under `instance/database.sqlite3`; avoid modifying or deleting it during code changes unless explicitly requested.
- Product uploads use the `media/` directory and are served by an admin route. Keep upload and serving behavior consistent when changing product management.
- PayFast configuration is read while `website/views.py` imports, so checkout changes must account for missing or incomplete environment values.
- CSRF is currently disabled in `website/__init__.py`; do not assume forms have CSRF protection when assessing or changing request handling.
- Keep changes focused. Do not add generated files, credentials, database contents, or media uploads to commits.