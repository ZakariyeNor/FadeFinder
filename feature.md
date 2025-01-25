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

### Tasks breakdown

### Header Implementation Tasks
- [ ] **Create Header HTML**
      
  - Add a header section to `base.html` with navigation links (Home, Book Now, Login, About).
  - Ensure the header is responsive and works on all screen sizes.
  - Ensure the menu toggles the visibility of navigation links.
  - Ensure clicking the each link redirects the user to the page (`/`).

- [ ] **Test Header Links**
  - Verify that all header links (Home, Book Now, Login, About) work correctly.
  - Test the header on desktop and mobile devices.
    
### Footer Implementation Tasks
- [ ] **Create Footer HTML**
      
  - Add a footer section to `base.html` with links (Social Links, Find Us, Book Now, Log Out, Sign-Up).
  - Ensure the footer is responsive and works on all screen sizes.
  - Ensure the footer looks good on desktop and mobile devices.
  - Add a link to the about page in the footer and the link find us in the footer must view the section map.
     
- [ ] **Test Footer Links**
  - Verify that all footer links (Social Links, Find Us, Book Now, Log Out, Sign-Up) work correctly.
  - Test the footer on desktop and mobile devices.
    
### Home app

- Create home app, then the two sections required for the home page.
- Create models for the content

- [ ] **Testing Tasks**
 - Test features and functionality of the content
 - Verify that the pictures and text displayed in the main section are fetched from the database.
