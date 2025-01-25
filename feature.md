# MyProject Structure

Below is the structure of the project, the user story specifictions or approved P.B.I's.

## Project Structure
---

### File Descriptions

### `home/`
- **`models.py`**: Defines database models for the home app.
- **`admin.py`**: Registers models with the Django admin.
- **`views.py`**: Contains view logic for the home app.
- **`urls.py`**: Defines URL patterns for the home app.
- **`templates/home/home.html`**: Template for the home page.

### `book/`
- **`models.py`**: Defines database models for the book app.
- **`admin.py`**: Registers models with the Django admin.
- **`views.py`**: Contains view logic for the book app.
- **`urls.py`**: Defines URL patterns for the book app.
- **`templates/book/book.html`**: Template for the book list page.

### `about/`
- **`models.py`**: Defines database models for the about app.
- **`admin.py`**: Registers models with the Django admin.
- **`views.py`**: Contains view logic for the about app.
- **`urls.py`**: Defines URL patterns for the about app.
- **`templates/about/about.html`**: Template for the about page.

### `login/`
- **`urls.py`**: Defines URL patterns for user authentication (using `django-allauth`).
- **`templates/account/`**: Contains templates for authentication pages (e.g., login, registration).

### `myproject/`
- **`settings.py`**: Contains project-wide settings.
- **`urls.py`**: Defines the root URL patterns for the project.
- **`wsgi.py`**: WSGI configuration for deploying the project.

### `templates/`
- **`base.html`**: Base template for all pages in the project.

---

