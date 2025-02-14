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

# Automated Testing

## Tasks for Home Page 

## Task 1: Test Home Page Header and Footer Display
- Verify the header includes the site title, logo, and navigation links.
- Check the footer for contact info, social media links, and navigation.

## Task 2: Verify BarberInfo Data and ServicesDes Data on Home Page and if their Fields Rendering
- Ensure the list of barbers and their descriptions are displayed correctly on the home page.
- Verify that `title`, `created_on`, and `updated_on` are displayed for each barber.
- Ensure the services offered by the barbershop are displayed on the home page.
- Check that each service’s `title` and `description` are visible.
- Ensure that `barberinfo` and `servicedescription` context are passed to the home template.
- Verify that the home page loads correctly from the root URL (`/`).
- Ensure the response for the home page renders the `home.html` template.
- Verify that the status code for the home page request is 200 (OK).


## Tasks for Book Page 

## Task 1: Test Booking Form Display
- Verify that the booking form shows a list of available barbers and services.
- Check if the form displays a cover image and intro text at the top of the page.
- Ensure the form is responsive and accessible on mobile, tablet, and desktop.

## Task 2: Test Booking Form Submission
- Verify that the booking form submits successfully and creates a booking record in the database.
- Ensure the booking is linked to the authenticated user.
- Confirm a success message is displayed upon successful booking.
- Check if an error message is shown when the form is invalid (e.g., invalid time or date).

## Task 3: Test Edit & Delete Booking Functionality
- Ensure only the user who created the booking can edit it.
- Verify that the user can modify the barber, service, date, and time.
- Confirm that a success message is shown when changes are saved.
- Ensure only the user who created the booking can delete it.
- Verify that the booking is removed from the database after successful deletion.
- Confirm that a success message is displayed upon deletion.

## Task 4: Test URL Mapping for Booking Pages
- Verify that the `/form/` URL renders the booking form.
- Ensure the `/edit_booking/<booking_id>/` URL renders the edit booking form.
- Verify the `/delete_booking/<booking_id>/` URL allows the user to delete the booking.

## Task 5: Test Booking Model Validation for Overlapping Appointments
- Ensure the system prevents overlapping bookings with the same barber and service at the same time.
- Verify that the system displays an error message when a conflict occurs.


# Tasks for Login, Logout, and Sign-Up with Allauth

## Task 1: Test Sign-Up and Login Functionality
- **Test Sign-Up:**
  - Ensure the sign-up page is accessible.
  - Verify that the sign-up form includes fields for username, email, and password.
  - Test successful sign-up and confirm that the user is redirected to the login page or homepage.
  - Verify that the new user is created in the database.
  - Ensure that an email confirmation is sent (if applicable).
- **Test Login:**
  - Ensure the login page is accessible.
  - Test successful login with valid credentials and verify redirection to the homepage or user dashboard.
  - Test invalid login attempts with incorrect credentials and ensure the form shows error messages.

## Task 2: Test Logout Functionality and Session Management
- Ensure the logout button/link is accessible to logged-in users.
- Verify that clicking logout redirects the user to the login page or homepage.
- Confirm that the user’s session is terminated after logout.
- Ensure that the user cannot access logged-in pages after logging out.

## Task 3: Test User Authentication and Access Control
- **Test Access Control:**
  - Verify that only authenticated users can access restricted pages (e.g., profile, dashboard).
  - Ensure unauthenticated users are redirected to the login page when attempting to access restricted pages.
- **Test Email Confirmation (If enabled in Allauth):**
  - Ensure that a confirmation email is sent after sign-up.
  - Verify that the user cannot log in until they click the confirmation link.
  - Check that the user’s account is activated after confirming the email.

# Testing Tasks for "About" Page

## Task 1: Test About Model and Admin Registration

  - Verify that an `About` instance can be created with valid fields (`title`, `about_image`, `content`).
  - Ensure the `About` model appears in the Django admin.
  - Verify that the `title` and `created_on` fields are displayed in the admin list view.

## Task 2: Test Collaboration Model and Admin Registration
  - Verify that a `Collaboration` instance can be created with valid fields (`barber_name`, `barber_shop`, `business_type`, `service_offered`, `email`, `number`).
  - Ensure the unique constraint on `barber_name` and `barber_shop` is enforced.
  - Ensure the `Collaboration` model appears in the Django admin.
  - Verify that `barber_name`, `barber_shop`, and `email` fields are displayed in the admin list view.

## Task 3: Test Collaboration Form Validation and Submission
  - Verify that a valid `CollaborationForm` submission creates a new `Collaboration` record in the database.
  - Ensure the user receives a success message after successful form submission.
  - Ensure that invalid form data triggers appropriate error messages.
  - Verify that duplicate collaboration entries (same `barber_name` and `barber_shop`) are prevented.

## Task 4: Test About Page View and Context & URL Mapping

  - Ensure that the `about_me` view renders correctly.
  - Verify that the context passed to the template includes `abouts` and `collaborations` data.
  
  - Ensure that the API key used for maps is correctly passed to the template.
  - Verify that the URL for the "About" page (`/`) maps to the `about_me` view.

## Task 5: Test About Image Upload Functionality

  - Verify that an image can be successfully uploaded to the `about_image` field.
  - Ensure that the uploaded image is displayed correctly on the "About" page, If it's not the placeholder image (cover.jpg) should displayed with error text.
  
