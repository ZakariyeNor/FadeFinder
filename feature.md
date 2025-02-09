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


### Create Header HTML
      
  - Add a header section to `base.html` with navigation links (Home, Book Now, Login, About).
  - Ensure the header is responsive and works on all screen sizes.
  - Ensure the menu toggles the visibility of navigation links.
  - Ensure clicking the each link redirects the user to the page (`/`).

- [ ] **Test Header Links**
  - Verify that all header links (Home, Book Now, Login, About) work correctly.
  - Test the header on desktop and mobile devices.
    

### Create Footer HTML
      
  - Add a footer section to `base.html` with links (Social Links, Find Us, Book Now, Log Out, Sign-Up).
  - Ensure the footer is responsive and works on all screen sizes.
  - Ensure the footer looks good on desktop and mobile devices.
  - Add a link to the about page in the footer and the link find us in the footer must view the section map.
     
- [ ] **Test Footer Links**
  - Verify that all footer links (Social Links, Find Us, Book Now, Log Out, Sign-Up) work correctly.
  - Test the footer on desktop and mobile devices.
    
### Home App

- Create a `home` app for the project.  
  - Add a main section and an additional content section to the home page.  
  - Create models for the main section and content to manage pictures and text dynamically.  
  - Populate the database with initial data for testing purposes.  

- [ ] **Testing Tasks:**  
  - Verify that pictures and text in the main section are fetched from the database.  
  - Ensure all features and functionalities of the content sections are working as expected.  

---

### Admin Login

- Configure Django's admin interface for site administration.  
  - Implement Role-Based Access Control (RBAC) for restricting access to admin-only features outside the admin panel.  
  - Customize the admin panel if needed for better usability.  

- [ ] **Testing Tasks:**  
  - Ensure admins can log in securely via the Django admin panel.  
  - Test that admin-only routes are accessible only by authenticated admin users.  

---

### Email & SMS Confirmation

- Integrate email services such as SendGrid for sending confirmation emails.  
- Integrate SMS services like Twilio for sending verification codes to users.  
- Create endpoints for sending and verifying email and SMS confirmation codes.  

- [ ] **Testing Tasks:**  
  - Ensure email confirmation links are sent during user registration.  
  - Verify that SMS confirmation codes are sent to the user's phone upon request.  

---

### Logout, Login, Guest Login, and Register Page

- Use Django Allauth for handling user authentication, registration, and session management.  
  - Make the logout button visible only when a user is logged in.  
  - Design a front-end login form with a sign-up option.  
  - Create a front-end registration form for new users.  
  - Generate temporary guest accounts with limited access for guest users.  

- [ ] **Testing Tasks:**  
  - Verify that users cannot access protected routes after logging out.  
  - Ensure front-end forms validate inputs before submission.  
  - Confirm that guest accounts have limited access and expire after a set time.  

---

### Booking Page - Calendar

  - Create a back-end model for storing booking information (e.g., user, date, time, and status).
  - Implement logic for checking booking availability based on selected dates and times.
  - Ensure booking data is saved securely in the database, and prevent duplicate bookings.
  - Design and implement a responsive calendar interface where users can pick a booking date and time.
  - Display available slots visually, with unavailable times grayed out or disabled.
  - Show confirmation or error messages upon successfully submitting or failing to book a slot.

- [ ] **Testing Tasks:**  
  - Verify that booking data is correctly saved in the database.  
  - Test the booking availability logic to ensure users cannot book the same time slot twice.
  - Verify that the calendar UI displays available and unavailable slots correctly.
  - Ensure cancel/reschedule functionality works seamlessly.
  - Ensure booking status is correctly saved and reflected in the database.

---

### About page 

  - Build models for both image and content
  - Use cloud storage to store pictures
  - Build contact form modal
  - Build Google map api

- [ ] **Tests:**
  - Test the content modal if admin user can upload pictures
  - Test if the cloud connection is working
  - Test map api

