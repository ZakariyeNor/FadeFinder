# Manual Testing Plan for Header, Footer, Navigation, Links, and Responsiveness

### **Purpose**
To ensure that the **header, footer, navigation, internal and external links, and responsive design** function correctly across all pages, providing a smooth user experience.

---

![](manual_testing_screenshots/test.png)


## **2. Header Testing**
This is how the navigation looks when user land on the app
![](manual_testing_screenshots/desktop_nav_logout.png)
This is how the navigation looks like for admin user log in 
![](manual_testing_screenshots/desktop_nav_admin_logiin.png)
And this is how the navigation looks like when user log in. And it also displays the success massage of the user login
![](manual_testing_screenshots/desktop_nav_user_login.png)

### **2.1 Visibility & Layout**
This the visibility of the nav in mobile or small size screens and it's when user or admin is not logged in 
![](manual_testing_screenshots/mobile_nav_login.png)
- **Test Steps:**
1. Open **Home, Book, Account and About** pages.
  It shows the required navigation links, but based on if it's logged in or not 
2. Verify that the **header appears at the top** of each page.
  The header is always at the top of the page, both larger and small screen size devices
![](manual_testing_screenshots/mobile_nav_login.png)
  3. Ensure that elements like **logo(Barber booking), navigation links, and dropdowns** are correctly aligned.

- **Expected Outcome:**
  - The header should be **visible and consistent** across all pages.
  it works as it should.
  - All elements should be properly aligned.

### **2.2 Navigation Links**
- **Test Steps:**
  1. Click on each **navigation link** (e.g., **Home, Book, Account and About**).
  2. Verify that each link **navigates to the correct page**.

- **Expected Outcome:**
  - Clicking a link should navigate to the **correct page**.
  - No **broken links**.
  - The **active page** should be visually indicated.
  

## **3. Footer Testing**
  ![](manual_testing_screenshots/desktop_footer.png)
### **3.1 Visibility & Layout**
- **Test Steps:**
  1. Fixed footer **bottom of each page**.
  2. Ensure the **footer is displayed** correctly.
  3. Check that it remains **fixed at the bottom** (if applicable).

- **Expected Outcome:**
  - The footer should be **visible and properly formatted** on all pages.

### **3.2 Footer Links**
- **Test Steps:**
  1. Click on each on admin login footer **footer link** (Book or booked, about, admin and logout ).
  ![](manual_testing_screenshots/desktop_footer_admin_login_have_bookings.png)
    check user login footer **footer link** (Book or booked, about, Contact us and logout ).
  ![](manual_testing_screenshots/desktop_user_footer_no_booking.png)
  2. Verify that each link **navigates to the correct page**.
  3. Test **external links** (social links) and confirm they open in a **new tab**.

- **Expected Outcome:**
  - Internal links should navigate properly.
  - External links should **open in a new tab**.

### 2.2 ** Mobile Footer**
- **Test Steps:**
  1. Fixed to the bottom of each Page.
  2. Check mobile device footer, it must display , icons of home, calender, profile and gps
    The profile has to has hover effect to show login and logout when user hover over it 
  3. Check the alignment and styling of the footer content.
  ![](manual_testing_screenshots/mobile_footer.png)
- **Expected Outcome:**
  - The footer should be correctly aligned at the bottom.
  - All footer links should be clickable and should navigate to the corresponding pages.
  - The footer should be responsive and adapt to different screen sizes.

---
### **3.3 Social Media Icons**
- **Test Steps:**
  1. Click on each **social media icon** in the footer.
  2. Ensure they **open the correct social media page** in external tab.
  3. Mobile footer should not have social links instead they are in the about app

- **Expected Outcome:**
  - Social media icons should direct to the **correct platform**.

---

# Manual Testing Plan for Home Page

### Purpose:
To ensure that the Home Page (`home`) renders correctly, with all elements.

---

## 3. **Content Checks:**

The images displayed on the homepage are sourced from Pexels, and although they are environmental images, they are dynamically uploaded and stored on Cloudinary for efficient media management and optimization. The primary goal is to provide users with the ability to upload their own images, offering an interactive and customizable experience.

The text in the app has been generated with the assistance of ChatGPT to streamline the development process and ensure faster content creation.

### 3.1 **Page Content Rendering**
- **Test Steps:**
  1. Open the Home Page.
  2. Verify that the **main content** of the page (images, text, etc.) is displayed correctly.
  3. Check for any missing or broken content (e.g., missing images, incorrect text).
  4. Missing image must have the alt text and cove.jpg image in the images file

  ![](manual_testing_screenshots/desktop_home_barber_section.png)

- **Expected Outcome:**
  - All content on the Home Page should render without errors or broken links.
  - Images and other media should load correctly.
  - The content should be aligned with the app's purpose.

---
  ![](manual_testing_screenshots/desktop_home_service_section.png)

## 4. **Functionality Checks:**

### 4.1 **Navigation (Header and Footer Links)**
- **Test Steps:**
  1. Click all links in the header and footer and verify that they work as expected.
  2. Check that the active link is highlighted (if this feature is implemented).
    the images and text in home page must take full 12 column in mobile size's.

- **Expected Outcome:**
  - All navigation links should be active and correctly highlight the current page.
    ![](manual_testing_screenshots/home_mobile.png) 

## 5. **Performance Checks:**

### 5.1 **Page Load Speed**
- **Test Steps:**
  1. Open the Home Page in the browser and measure how quickly the page loads.
  2. Use tools like Google PageSpeed Insights to check performance if necessary.

- **Expected Outcome:**
  - The page should load in a reasonable amount of time, ideally within 2-3 seconds.

---

## 7. **Test Considerations:**
- Ensure all links (internal and external) are functional.
- Check all static resources (CSS, JS) are loaded correctly without errors in the browser console.
- Verify that all interactive elements (forms, buttons) work as expected.
---


# Manual Testing Plan for Book Page

### Purpose:
To ensure that the Book Page (`book`) renders correctly, with all elements functioning as expected, including the booking form and integration with the backend functionality.

---

The cover image in the Book App is an environmental image that is dynamically uploaded and stored using Cloudinary for efficient media management and optimization.

  ![](manual_testing_screenshots/desktop_book_cover_section.png)

### 2.3 **Page Content**
- **Test Steps:**
  1. Open the Book Page and verify that the page content is displayed correctly.
  2. Ensure the page displays relevant booking information, such as Booking form, form fields, available times and date, etc.
  3. The content must display based on user login 
  4. Footer and header must show if user has bookings or not

  This is footer before login 
     ![](manual_testing_screenshots/desktop_admin_login_no_booking.png)
  
  This is footer and header after login 
     ![](manual_testing_screenshots/desktop_user_login_bookings.png)
     ![](manual_testing_screenshots/desktop_bookings.png)
---

## 3. **Functionality Checks:**

### 3.1 **Booking Form**
- **Test Steps:**
  1. Verify that the booking form is present on the page.
  2. Fill in the form fields (e.g., barber_name, service, date, time).
  3. Submit the form with valid data.
  4. Make sure the form must be visible only if the user is loged in

- **Expected Outcome:**
  - The booking form should allow users to choose and submit data without errors.
  - On form submission, users should see a confirmation or success message, indicating that their booking request was successfully processed.
  - After successful submission, the page should redirect and show a success message or error message.
  - The logic must work both large and small size screens and must be responsive

Small device's booking section while user is log in 
    ![](manual_testing_screenshots/mobile_book_login.png)

Small device's booking section logout
    ![](manual_testing_screenshots/mobile_book_logout.png)

Large device's booking section while user is logged in 
    ![](manual_testing_screenshots/desktop_book_boking_section_login.png)

---

### 3.2 **Form Update**
- **Test Steps:**
1. Now, tested if the booked appoinments is visible only when user is loged in and the appoinments is for the one logged in, otherwise the error must display (no Bookings yet)

  Now the booked section(already booked appoinments) is visible only if the user is logged, otherwise the booking section will look like this ![](manual_testing_screenshots/book_logout.png)

And it's responsive for different screens
  ![](manual_testing_screenshots/mobile_booked_section.png)


Now test to update apponment by clicking update

  ![](manual_testing_screenshots/desktop_manage_bookings.png)

The form must have same as like the booking form then, update and you'll get error or success message

  ![](manual_testing_screenshots/desktop_edit.png)

Success Message and book page redirection
![](manual_testing_screenshots/succ_mess_edit.png)

2. Test if the delete option is working and you must give delete confirmation message to the user before deleting the appoinment, then redirect to the book page and give success message in the book page
Delete confirmation
  ![](manual_testing_screenshots/delete_confirmation.png)

Delete confirmation message and redirection to the book page
  ![](manual_testing_screenshots/deletion_cofirmation_message.png)

# Manual Testing Plan for About Page

### Purpose:
To verify that the About Page (`about_me` view) is rendering correctly, displaying the necessary information, handling collaboration requests properly, and integrating seamlessly with the **base.html** template.


![](manual_testing_screenshots/manual_testing_screenshots)

---

## 3. **Functionality Checks**

### 3.1 **Collaboration Request Form**
- **Test Steps:**
  1. Locate the **collaboration request form** on the page.
  2. Verify that all form fields (barber name, shop name, business type, service offered, email, phone number, additional info) are visible and editable.
  3. Submit the form with valid data.
  4. The form must be visible only if user is logged in 

  This is how the about page must look like before log in both small devices and large devices

Large device's 'collaboration form before log in 

![](manual_testing_screenshots/desktop_about_logout.png)

small device's collaboration form before log in 

![](manual_testing_screenshots/about_logout.png)

Large and small device's collaboration form after log in 

![](manual_testing_screenshots/mobile_logedin_about.png)

The FAQ, contact us and map must be visible all the time, even if the user is not log in or guest and contact us can submit with out log in information

FAQ section
![](manual_testing_screenshots/about_faq.png)
small devices the collaboration form before log in 

Find Us & Contact Us 
![](manual_testing_screenshots/about_findus.png)

Social links in mobile size must be under the map and  section
![](manual_testing_screenshots/about_mobile_social.png)


### 3.2 **Form Validation**
- **Test Steps:**
  1. Submit the form with **empty fields**.
  2. Submit with an **invalid email format**.
  3. Submit with a **phone number** containing letters or special characters.

- **Expected Outcome:**
  - The form should prevent submission of incomplete or incorrect data.
  - Relevant error messages should appear when input is invalid.

---

### 3.3 **Google Maps API Integration**
- **Test Steps:**
  1. Check if the **Google Map** is displayed on the About Page.
  2. Verify that the map loads correctly and does not show an API error.
  3. Ensure that the correct **API key** is being used.

- **Expected Outcome:**
  - The map should be visible and functional (zooming and panning should work).
  - No API errors should be displayed.

---

## 4. **Database & Backend Checks**

### 4.1 **Fetching About Content**
- **Test Steps:**
  1. Check if the `About` model data is properly loaded into the page.
  2. Verify that any recent updates to the **About section** are reflected.

- **Expected Outcome:**
  - The page should dynamically fetch and display the latest `About` content.

---

### 4.2 **Collaboration Data Storage**
- **Test Steps:**
  1. Submit a valid **collaboration request**.
  2. Check the **Django admin panel** or database to confirm that the request is saved.

- **Expected Outcome:**
  - The request should be saved in the `Collaboration` model.
  - The submitted data should match the form input.

---

### 5.2 **Form Submission Errors**

  - An appropriate error message should be displayed.
  - The form should not crash the page.

---

### 7.2 **Direct Database Access Prevention**
- **Test Steps:**
  1. Try accessing `/admin/about/` without logging in.
  2. Observe whether access is restricted.

- **Expected Outcome:**
  - The Django **admin panel** should be inaccessible without authentication.

---

# Manual Testing for Authentication (Django Allauth)

## 1. Sign-Up Page

### Test Case 1: Successful Sign-Up

**Steps:**
1. Navigate to `/accounts/signup/`.
2. Enter a valid email address.
3. Enter a valid password and confirm it.
4. Click on **Sign Up**.

**Expected Result:**
- The user is redirected to home page.
- The user account is created in the database.
- Success message on home page

  ![](manual_testing_screenshots/succ_registeratioon.png)

### Test Case 2: Sign-Up with an Existing Email

**Steps:**
1. Navigate to `/accounts/signup/`.
2. Enter an already registered email address.
3. Enter a valid password and confirm it.
4. Click on **Sign Up**.

**Expected Result:**
- An error message appears stating that the email is already in use.
- The user is not registered again.

  ![](manual_testing_screenshots/already_exi.png)

### Test Case 3: Invalid Password

**Steps:**
1. Navigate to `/accounts/signup/`.
2. Enter a valid email address.
3. Enter a weak password (e.g., `123`).
4. Click on **Sign Up**.

**Expected Result:**
- An error message appears indicating password strength requirements.
- The user is not registered.

  ![](manual_testing_screenshots/err_registeration.png)

## 2. Login Page

### Test Case 4: Successful Login

**Steps:**
1. Navigate to `/accounts/login/`.
2. Enter a valid email and password.
3. Click on **Login**.

**Expected Result:**
- The user is redirected to the home page.
- The session is established.

 ![](manual_testing_screenshots/succ_login.png)

### Test Case 5: Login with Incorrect Credentials

**Steps:**
1. Navigate to `/accounts/login/`.
2. Enter an incorrect email or password.
3. Click on **Login**.

**Expected Result:**
- An error message appears indicating invalid credentials.
- The user is not logged in.

  ![](manual_testing_screenshots/err_login.png)

## 3. Logout Page

### Test Case 7: Successful Logout

**Steps:**
1. Log in to the application.
2. Navigate to `/accounts/logout/`.
3. Click on **Logout**.

**Expected Result:**
- Warning before logging out.

  ![](manual_testing_screenshots/desktop_logout.png)


- The user is logged out.
- The user is redirected to the home page.

![](manual_testing_screenshots/logout_confirmation_message.png)

