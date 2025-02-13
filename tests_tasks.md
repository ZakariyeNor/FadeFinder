# Manual Testing Tasks

## 1. Home Page Testing:

## Responsiveness:
- Test the layout on different screen sizes (mobile, tablet, desktop).
- Ensure that images, text, and other elements adjust correctly to the screen width.
- Verify that navigation links and buttons are easy to click on all screen sizes.

## UI/UX:
- Ensure the page loads within an acceptable time.
- Check that all text is readable and the font sizes are appropriate.
- Test the accessibility of navigation links, ensuring that they are visible and correctly aligned.
- Verify the visibility and contrast of call-to-action buttons (e.g., “Book” button).

## Functionality:
- Ensure that all links (e.g., Home, Book, About and account) work and lead to the correct pages.
- Test any dynamic functionality.

## Logic:
- Verify that the correct user content is shown (e.g., logged-in users vs. logged-out users).
- Ensure that the homepage correctly displays recent bookings, services, or any dynamic content.

## Access:
- Test access to the homepage for logged-in and logged-out users.
- Ensure that non-logged-in users are redirected properly to login or book pages.

---

# 2. Book Page Testing:

## Responsiveness:
- Verify that the booking form adjusts to various screen sizes (especially mobile devices).
- Ensure form fields and buttons are well-spaced and easy to interact with on all devices.

## UI/UX:
- Check that the booking form is clear and well-labeled (barber, service, date, and time fields).
- Ensure the form provides clear error messages for invalid inputs (e.g., invalid date, unavailable time).

## Functionality:
- Test the booking process:
  - Choose a barber and service.
  - Select a date and time.
  - Confirm that the system displays available times.
  - Ensure that the form can be submitted correctly and that the data is saved.

## Logic:
- Ensure that the system prevents multiple bookings for the same time slot.
- Test the case where a user tries to book with invalid information (e.g., past date).

## Access:
- Ensure that only logged-in users can access the booking page or are redirected to the login page.

---

# 3. Login Page Testing:

## Responsiveness:
- Test that the login form is properly aligned on all screen sizes.
- Check that input fields are easy to interact with on mobile.

## UI/UX:
- Ensure that form fields (username/email and password) are clearly labeled.
- Verify that error messages appear when login fails (e.g., incorrect password).
- Check that login button is visible and accessible.

## Functionality:
- Ensure that the login form submits successfully with correct credentials.
- Test login with valid and invalid credentials.
- Verify that the user is redirected to the homepage or dashboard upon successful login.

## Logic:
- Ensure that logged-in users see personalized content after login.
- Check that the form clears any previous input when the page is reloaded.

## Access:
- Verify that users who are already logged in cannot access the login page (they should be redirected to the homepage).
- Test that the login page is accessible to non-authenticated users.

---

# 4. Logout Page Testing:

## Responsiveness:
- Test the logout button’s visibility and accessibility on different screen sizes.

## UI/UX:
- Ensure that the logout button is clear and stands out.
- Check for a confirmation message after successful logout (e.g., "You have been logged out").

## Functionality:
- Test that the logout action works, redirecting the user to the login page or homepage.
- Verify that the session is fully cleared after logout.

## Logic:
- Ensure the user is logged out and redirected after clicking the logout button.

## Access:
- Verify that the logout option is visible and accessible to logged-in users only.

---

# 5. Sign-In (Signup) Page Testing:

## Responsiveness:
- Test the responsiveness of the sign-in form.
- Ensure input fields are clear and large enough on mobile devices.

## UI/UX:
- Ensure the signup form is well-structured (fields for name, email, password, etc.).
- Verify the visibility and accessibility of the signup button.
- Check that appropriate error messages are shown (e.g., missing fields, password strength).

## Functionality:
- Test the form submission with valid and invalid information.
- Ensure that successful submission redirects the user to the appropriate page (home or dashboard).

## Logic:
- Ensure the user is created successfully and can log in immediately after signing up.

## Access:
- Verify that the signup page is accessible to non-logged-in users only.
- Ensure that logged-in users cannot access the signup page (they should be redirected to the homepage).

---

# 6. Edit Booking Page Testing:

## Responsiveness:
- Check that the edit booking form adapts to various screen sizes.
- Ensure the form fields are well-aligned and readable on mobile devices.

## UI/UX:
- Ensure that the form displays the current booking details (barber, service, date, time).
- Verify that users can update the fields and see the changes reflected.

## Functionality:
- Test the ability to edit and submit a booking successfully.
- Verify that the system saves the updated booking details.
- Check for validation (e.g., prevent users from editing the time to a booked slot).

## Logic:
- Ensure that users can only edit bookings that they created.
- Verify that bookings are correctly updated in the database.

## Access:
- Ensure that only the user who created the booking can edit it.
- Test that users cannot edit bookings made by others.

---

# 7. About Page Testing (Formspree and Google Map API):

## Responsiveness:
- Test that the map and form on the About page adjust correctly on all devices (desktop, tablet, mobile).
- Ensure that the form inputs are easy to use on mobile.

## UI/UX:
- Ensure the map is visible and interactive.
- Test the visibility and accessibility of the contact form (Formspree integration).

## Functionality:
- Test that the form submits correctly and sends data via Formspree.
- Ensure that the map loads correctly and displays the intended location.

## Logic:
- Verify that Formspree correctly handles form submissions and sends confirmation emails.
- Check the map to ensure it reflects the correct location.

## Access:
- Ensure that the About page is accessible to all users.
- Verify that the map and form are functional for both logged-in and logged-out users.

---

# General Testing Tasks Across All Pages:

- Test different browsers (Chrome, Firefox, Safari, Edge) to ensure cross-browser compatibility.
- Check for broken links on all pages.
- Test loading times and performance on various devices and networks.
- Test accessibility (using screen readers, ensuring the app is usable with only keyboard navigation).
- Test security: Ensure that pages requiring authentication (e.g., booking, editing) properly restrict access to unauthorized users.


# User Stories for Automated Testing with pytest in Django

## User Story 1: Home Page Header and Footer
**As a user**, I want the home page to display the header and footer correctly, so that I can navigate the site properly and view any relevant information at the top and bottom of the page.

### Acceptance Criteria:
- The header should include a site title, logo, and navigation links.
- The footer should include contact information, social media links, and additional navigation (e.g., terms and conditions).
- The header and footer should be visible on all screen sizes (mobile, tablet, and desktop).

---

## User Story 2: BarberInfo Model Display
**As an admin**, I want to see a list of barber descriptions in the Django admin panel so that I can manage the details of the barbers.

### Acceptance Criteria:
- The list display should show `title`, `created_on`, and `updated_on`.
- The search functionality should allow searching by `title`.
- The description field should be editable using the Summernote text editor.

---

## User Story 3: ServicesDes Model Display
**As an admin**, I want to see the services descriptions in the admin panel so that I can easily manage the services offered by the barbershop.

### Acceptance Criteria:
- The list display should show `title`, `created_on`, and `updated_on`.
- The search functionality should allow searching by `title`.
- The description field should be editable using the Summernote text editor.

---

## User Story 4: Home Page (BarberInfoContent View)
**As a user**, I want to see a list of barbers and the services offered on the home page so that I can make an informed choice when booking.

### Acceptance Criteria:
- The home page should list all the barbers with their descriptions.
- The page should also display the services offered by the barbershop.
- The `barberinfo` and `servicedescription` context data should be passed to the template.

---

## User Story 5: URL Mapping (Home URL)
**As a user**, I want the home page to load correctly when I visit the root URL (`/`).

### Acceptance Criteria:
- The URL should render the `home.html` template.
