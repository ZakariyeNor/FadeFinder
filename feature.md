# MyProject Structure

Below is the structure of the project, the user story specifictions or approved P.B.I's.

## Project Structure

fadefinder/
├── home/
│   ├── models.py
│   ├── admin.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── home/
│           └── home.html
├── book/
│   ├── models.py
│   ├── admin.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── book/
│           └── book.html
├── about/
│   ├── models.py
│   ├── admin.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── about/
│           └── about.html
├── login/  # For allauth (login, logout, register)
│   ├── urls.py
│   └── templates/
│       └── account/  # Allauth templates
├── fidefinder/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── templates/
    └── base.html
