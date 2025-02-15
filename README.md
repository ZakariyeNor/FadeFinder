# FadeFinder
Barber Booking Center
# [FadeFinder](https://barber-booking-center-b87a4a734af4.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/ZakariyeNor/FadeFinder)](https://www.github.com/ZakariyeNor/FadeFinder/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/ZakariyeNor/FadeFinder)](https://www.github.com/ZakariyeNor/FadeFinder/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/ZakariyeNor/FadeFinder)](https://www.github.com/ZakariyeNor/FadeFinder)

Description

The Barber Booking App is an online platform that allows users to easily book appointments with barbers. The app provides an intuitive interface for customers to select their preferred barber, choose an appointment slot, and manage their booking details. Barbers can manage their availability and keep track of upcoming appointments.

![screenshot](documentation/mockup.png)

source: [FadeFinder amiresponsive](https://ui.dev/amiresponsive?url=https://barber-booking-center-b87a4a734af4.herokuapp.com)

**Site Mockups**

# Wireframes Documentation

This document contains wireframes for the **FadeFinder** app, showcasing the design for both **mobile** and **desktop** views. Each wireframe is linked below with a detailed description of the page.

---

## 1. Home Page
The **Home Page** is the landing page of the app. It provides an overview of the barber shop and its services, with clear navigation to other pages.

### Mobile View
![Home Page Mobile](documentation/mockups/home.png)

### Desktop View
![Home Page Desktop](documentation/mockups/home_d.png)

---

## 2. Menu (Navigation)
The **Menu** provides access to all major pages of the app, including **Book Now**, **Login**, **Register**, and **About**.

- The menu is integrated into the header navigation bar on desktop.

### Mobile View

![Menu Mobile](documentation/mockups/menu.png)


## 3. Booking Page
The **Booking Page** allows users to select a service, choose a date and time, and confirm their appointment.

### Mobile View
![Booking Page Mobile](documentation/mockups/booking.png)

### Desktop View
![Booking Page Desktop](documentation/mockups/booking_d.png)

---

## 4. Login Page
The **Login Page** allows users to log in to their accounts using their email and password. It also includes a link to the **Register Page**.

### Mobile View
![Login Page Mobile](documentation/mockups/log_in.png)

### Desktop View
![Login Page Desktop](documentation/mockups/log_in_d.png)

---

## 5. Register Page
The **Register Page** allows new users to create an account by entering their name, email, and password.

### Mobile View
![Register Page Mobile](documentation/mockups/register.png)

### Desktop View
![Register Page Desktop](documentation/mockups/register_d.png)

---

## 6. Log Out Page
The **Log Out Page** confirms that the user has successfully logged out and provides options to log back in or return to the home page.

### Mobile View
![Log Out Page Mobile](documentation/mockups/log_out.png)

### Desktop View
![Log Out Page Desktop](documentation/mockups/log_out_d.png)

---

## 7. About Page
The **About Page** provides information about the barber shop, including its history, team, and location.

### Mobile View
![About Page Mobile](documentation/mockups/about.png)

### Desktop View
![About Page Desktop](documentation/mockups/about_d.png)

---

## UX

# The 5 Planes of UX

## 1. Strategy Plane

### Purpose
Users need an easy way to book services, manage their accounts, and navigate the barber shop’s website.  
**Business Goal:** Provide users with a seamless online experience for making appointments, registering, and learning about the services provided by the barber shop.

### Primary User Needs
- Users need to navigate the site easily to access services, book appointments, and get more information about the barber shop.
- Admins need efficient tools to log in and manage bookings, add services and upload images.
- New Users need a simple registration process and if they want to contact us they can contact us without login by email.
- Give user ability to manage their bookings.

### Business Goals
- Make booking appointments intuitive and seamless.
- Encourage user registration and engagement with the site.
- Ensure clear communication of the barber shop’s services, values, and contact details.

---

## 2. Scope Plane

### Features
- Header navigation with links (Home, Book, Account, About).
- Booking page with Booking form, calendar, and time.
- Login, Register, and Admin Login functionality.
- About page with info on the barber booking app, contact us form, collaboration request form and location.
- Footer navigation in mobile devices, links to social media and additional pages in tablet and desktop size.

### Content Requirements
- High-quality images of the barber shop and services.
- Text about the barber, barber shop’s services.
- Forms for logging in, registering, and booking appointments.
- Social media links (only phone size) and contact info on the About page

---

## 3. Structure Plane

### Information Architecture
- **Main Navigation:** Home, Book, Account(Log-in,log-out, register, admin), About (Header); Footer mobile (with icons of home, calendr, profile and gps) from tablet size (Social Links, Find Us, Book, Log Out, admin-log-out.
- **User Flow:**
  - **New Users:** Browse site → Register → Book an Appointment.
  - **Logged-In Users:** View services → Choose a date and time → Confirm booking.
    - Logged in users can add, edit, delete their own appoinments.),
    - They can see booking form, if they have already booked appoinments and can send form
  - **Admins:** Login → Manage bookings → View calendar and user data.

### User Flow
- Users can navigate via the header or footer to access pages.
- On the Booking page, users can select, barbers, services, dates, and times.
- Users can log in or register to book an appointment.
- Admins can log in, access the dashboard, and manage bookings, their services and more.

---

## 4. Skeleton Plane

### Wireframe Suggestions
- **Homepage:** Header with navigation, main section with images and text, footer with links.
- **Booking Page:** Barber list, service list, calendar, time, "Book" button.
- **Login/Registration Pages:** Forms for user info, login/register options.
- **Admin Dashboard:** Manage barber shop, it's services, bookings, see booked appoinments, can read collaboration requests.

---

## 5. Surface Plane

### Visual Design Elements

#### Colors:
- **Primary Color:** `#1f5a5e` (Dark Green) for headers and key UI elements.
- **Secondary Color:** `#ffffff` (White) for background and text containers.
- **Accent Color:** `#ffc107` (Gold) for action buttons like Book Now.
- **Action Color:** `#ffd700` (Gold) for call-to-action buttons.

#### Typography:
- **Heading Font:** [Montserrat](https://fonts.google.com/specimen/Montserrat) was used for the primary headers and titles.
- **Body Text Font:** [Lato](https://fonts.google.com/specimen/Lato) was used fo body text.
- **Primary Button Font:** [**Roboto**](https://fonts.google.com/specimen/Roboto) was used for call-to-action buttons.
- **Secondary Button Font:** [**Poppins**](https://fonts.google.com/specimen/Poppins) was used for all other secondary text.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

#### Visual Design:
- Clean, modern layout with an emphasis on simplicity and easy navigation.
- High-contrast text for readability.
- Interactive elements (buttons, links) with hover effects for better user interaction.


## User Stories

INSTRUCTIONS 

In this section, list all of your possible user stories for the project. Samples have been provided below using the example walkthrough project for your inspiration. Make sure to adjust to match your own project features!


| Target | Expectation | Outcome |
| --- | --- | --- |
| As a user | I would like to navigate to different pages using the header links | so that I can access the features of the app. |
| As a user | I would like to view pictures and text in the main section of the landing page | so that I can learn about the barber shop and its services. |
| As a user | I would like to use the footer links to access additional features and information | so that I can interact with the app more effectively. |
| As a user | I would like to book an appointment by selecting a service, date, and time | so that I can schedule a haircut or other services. |
| As a user | I would like to log in to my account | so that I can book appointments and manage my bookings. |
| As a new user | I would like to register for an account | so that I can access all features of the app. |
| As a logged-in user | I would like to log out of my account | so that I can securely end my session. |
| As a user | I would like to visit the About page | so that I can learn more about the barber shop and its team. |
| As a user | I would like to view a map of the barber shop location on the About page | so that I can easily find the shop. |
| As a user | I would like to read the FAQ section on the About page | so that I can get answers to common questions about the barber shop's services. |
| As an admin | I would like to log in to my account | so that I can manage bookings and view the booked appoinments. |
| As a user | I would like to fill out a collaboration form | so that I can partner with the barber shop for potential projects or services. |
| As a non-registered user | I would like to contact the barber shop | so that I can inquire about services or ask questions without needing to register. |

## Features


### Existing Features

Barber booking center is packed with a range of powerful features that help users, barbers, and admins manage appointments, profiles, and services seamlessly. From booking and collaboration to personalized user accounts and responsive design across devices, we strive to provide a user-friendly experience for everyone involved. Below, you'll find an overview of the current features available on the platform, each designed to improve accessibility, usability, and interaction for our community.

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Desktop Navigation Login | Displays the navigation bar on desktop when the user is logged in, with access to different sections and the ability to log out. | ![screenshot](documentation/features/desktop_nav_log_in.png) |
| Desktop Navigation Logout | Displays the navigation bar on desktop when the user is logged out, providing access to login and other public pages. | ![screenshot](documentation/features/desktop_nav_log_out.png) |
| Mobile Navigation Logged In | Displays the mobile navigation bar when the user is logged in, including login status and links to manage bookings. | ![screenshot](documentation/features/mobile_nav_logged_in.png) |
| Mobile Navigation Logout | Displays the mobile navigation bar when the user is logged out, with options for login and public pages. | ![screenshot](documentation/features/mobile_nav_logout.png) |
| Desktop Footer Login | Footer section on desktop with login options for users who are not logged in. | ![screenshot](documentation/features/desktop_footer_login.png) |
| Desktop Footer Logout | Footer section on desktop with logout options for users who are logged in. | ![screenshot](documentation/features/desktop_footer_logout.png) |
| Mobile Footer | Mobile version of the site with footer navigation links to important sections. | ![screenshot](documentation/features/mobile_footer.png) |
| Home Desktop | Displays the homepage on desktop, providing basic information about the barber shop and its services. | ![screenshot](documentation/features/home_desktop.png) |
| Mobile Home | Displays the mobile version of the homepage, including key barber shop details and services. | ![screenshot](documentation/features/mobile_home.png) |
| Booked Data | View showing the user's booked appointments, with details like time, service, and status. | ![screenshot](documentation/features/booked_data.png) |
| Desktop Book Login | View showing the booking page for logged-in users, where they can select services and schedule appointments. | ![screenshot](documentation/features/desktop_book_login.png) |
| Edit View | View allowing users to edit their profile details or booking information. | ![screenshot](documentation/features/edit_view.png) |
| Login | The login screen where users enter their credentials to access their account. | ![screenshot](documentation/features/login.png) |
| Register | The registration screen where users can create a new account by entering necessary details. | ![screenshot](documentation/features/register.png) |
| Logout Message | Message displayed after the user successfully logs out, confirming the action. | ![screenshot](documentation/features/logout_message.png) |
| Success Book | A success message displayed after a user successfully books an appointment. | ![screenshot](documentation/features/success_book.png) |
| Success Collaboration Message | Success message displayed after a user successfully submits a collaboration request. | ![screenshot](documentation/features/success_collaboration_message.png) |
| Success Form Submit | Success message after a user successfully submits a form on the site, confirming the submission. | ![screenshot](documentation/features/success_formspree.png) |
| Success Update | Success message displayed after successfully updating user details or bookings. | ![screenshot](documentation/features/success_update.png) |
| About Mobile | The mobile version of the About page, displaying details of the barber shop, the team, and services offered. | ![screenshot](documentation/features/about_mobile.png) |
| Desktop About with Logout | The desktop version of the About page with a logout option visible for logged-in users. | ![screenshot](documentation/features/desktop_about_logout.png) |
| Desktop About Login | The desktop view of the About page when a user is logged in, providing more detailed options. | ![screenshot](documentation/features/desktop_About_login.png) |
| Desktop About Login (Alt) | An alternative view of the About page for logged-in users, offering different layout or options. | ![screenshot](documentation/features/desktop_about_login2.png) |
| Desktop About Logout | The desktop version of the About page shown when the user is logged out, with more basic details. | ![screenshot](documentation/features/desktop_about_logout.png) |
| Delete Warning | A confirmation screen that warns the user before they proceed with deleting data such as appointments. | ![screenshot](documentation/features/delete_warning.png) |
| Error Collaboration Message | Error message shown if something goes wrong while submitting a collaboration request. | ![screenshot](documentation/features/error_collaboration_message.png) |
| Error Message | General error message displayed for invalid user actions or inputs throughout the site. | ![screenshot](documentation/features/collaboration_error.message.png) |
| Log In Message | A message displayed during the login process to indicate whether the credentials are correct or if there was an error. | ![screenshot](documentation/features/log_in_message.png) |
| Phone Profile Icon | The profile icon shown on mobile devices for users to quickly access their profile. | ![screenshot](documentation/features/phone_profile_icon.png) |




### Future Features

As we continue to improve and expand the functionalities of our platform, we have identified several key features and enhancements to make the user experience even better. These upcoming features are designed to provide more convenience, flexibility, and personalization, whether for users, barbers, or admins. We aim to streamline the booking process, improve communication, and offer more tailored options for our barbershops and customers. Below is a list of features we plan to implement in the future to meet the evolving needs of our platform.


- **Email Confirmation for Appointments & Account Actions**: Automatically send email confirmations to users when they book, update, delete appointments, or take actions like signing in or resetting passwords.
- **Admin Email Notifications**: Notify the admin via email when a user books, deletes, or updates an appointment, ensuring they stay informed about user actions.
- **Payment Integration**: Implement payment systems such as credit cards, Swish, or Mobile Swift for easy and secure transactions for appointments.
- **Multiple Barbers Under One Barbershop**: Allow one barbershop to have multiple barbers listed, each with their own availability and profiles.
- **Barbershop-Specific About Pages**: Provide a dedicated About page for each barbershop, detailing its unique history, team, and services offered.
- **Barbershop-Specific Home Pages**: Create a unique homepage for each barbershop, displaying essential information such as location, services, and contact details.
- **City-Based Barber Navigation**: Develop a section that stores a navigation system to help users find barbers in different cities, making it easier to book across locations.
- **Barber Dashboard**: Build a specialized dashboard for barbers to manage their schedules, appointments, and customer interactions.
- **Individual Barber Dashboards**: Enable each barber to have a personal dashboard to manage their bookings, services, and client interactions.
- **Guest User Booking**: Allow guest users (non-registered) to book appointments and receive email confirmations, ensuring convenience without the need for account creation.

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) | Cloud-based IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Jest-grey?logo=jest&logoColor=c21325)](https://jestjs.io) | Automated JavaScript testing. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Figma-grey?logo=figma&logoColor=F24E1E)](https://www.figma.com) | Creating wireframes. |
| [![badge](https://img.shields.io/badge/Google_Maps_API-grey?logo=googlemaps&logoColor=4285F4)](https://developers.google.com/maps) | Interactive map on my site. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, testing and explain things. |
| [![badge](https://img.shields.io/badge/Mermaid-grey?logo=mermaid&logoColor=FF3670)](https://mermaid.live) | Generate an interactive diagram for the data/schema. |
| [![badge](https://img.shields.io/badge/Flatpickr-grey?logo=flatpickr&logoColor=FF4500)](https://flatpickr.js.org) | Date and time picker. |
| [![badge](https://img.shields.io/badge/Summernote-grey?logo=summernote&logoColor=FF8800)](https://summernote.org) | WYSIWYG text editor. |
| [![badge](https://img.shields.io/badge/Django_Allauth-grey?logo=django&logoColor=091A3D)](https://django-allauth.readthedocs.io) | Authentication and registration for Django. |
| [![badge](https://img.shields.io/badge/Django_Middleware-grey?logo=django&logoColor=F7B500)](https://docs.djangoproject.com/en/stable/topics/middleware/) | Custom middleware in Django. |
| [![badge](https://img.shields.io/badge/Django_Crispy_Forms-grey?logo=django&logoColor=D8D8D8)](https://django-crispy-forms.readthedocs.io) | Styling forms in Django with Bootstrap. |
| [![badge](https://img.shields.io/badge/Bootstrap_Crispy_Forms-grey?logo=django&logoColor=7952B3)](https://django-crispy-forms.readthedocs.io/en/latest/) | Bootstrap integration for Django Crispy Forms. |


⚠️ NOTE ⚠️

Want to add more?

- Tutorial: https://shields.io/badges/static-badge
- Icons/Logos: https://simpleicons.org
  - FYI: not all logos are available to use

🛑 --- END --- 🛑

## Database Design

### Data Model

Auto-generating Entity Relationship Diagrams (ERD)

I have used Auto-generating Entity Relationship Diagrams (ERD) to document my database models, making it easier to visualize relationships between different models in my Django project. By utilizing the django-extensions and pygraphviz libraries, I was able to automatically generate an ERD representing the structure of my database. This approach streamlines the process of creating an up-to-date diagram, especially as the project evolves. Below are the steps I followed to generate the ERD, which can be included in your project’s documentation for better understanding and future reference.

I have used `pygraphviz` and `django-extensions` to auto-generate an ERD.

The steps taken were as follows:
- In the terminal: `sudo apt update`
- then: `sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config`
- then type `Y` to proceed
- then: `pip3 install django-extensions pygraphviz`
- in my `settings.py` file, I added the following to my `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```
- back in the terminal: `python3 manage.py graph_models -a -o erd.png`
- drag the new `erd.png` file into my `documentation/` folder
- removed `'django_extensions',` from my `INSTALLED_APPS`
- finally, in the terminal: `pip3 uninstall django-extensions pygraphviz -y`

![E.R.D](documentation/advanced-erd.png)

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/ZakariyeNor/FadeFinder/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/agile/project_agi.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/ZakariyeNor/FadeFinder/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues/ZakariyeNor/FadeFinder)](https://www.github.com/ZakariyeNor/FadeFinder/issues) | ![screenshot](documentation/agile/issues.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-closed/ZakariyeNor/FadeFinder)](https://www.github.com/ZakariyeNor/FadeFinder/issues?q=is%3Aissue+is%3Aclosed) | ![screenshot](documentation/agile/done_issues.ong.png) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCow" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

## Testing

> [!NOTE]
- Documentation of the manual testing, front and back-end testing files.
> For all testing, you can find them [TESTING.md](documentation/test_documentation) folder.

> Or for each 
 > [Manual Testing](documentation/test_documentation/manual_testing.md),
 > [Front-end Tests](documentation/test_documentation/Front_end_validation.md),
 > [Back-end Tests](documentation/test_documentation/back_end_tests.md),

- | [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) |
- I used to output html templates, to validate in HTML validator without templatetags,
- I used to test, views, functions, models, urls, admin and forms to make the testing process faster.
- I used to document testing files to make the process of documenting faster
- I used to test the template logic and user accessibility.
- I used HTML validator for html testing, CSS validator for css testing and JSHINT for javascript testing.


## Deployment

The live deployed application can be found deployed on [Heroku](https://barber-booking-center-b87a4a734af4.herokuapp.com/).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | https://cloudinary.com/ |
| `DATABASE_URL` | https://www.postgresql.org/ |
| `GOOGLE_MAPS_API` | https://maps.googleapis.com/maps/api/geocode/json?address=city&key=API_KEY
 |
| `SECRET_KEY` | 34567ikjmnbvcarrgshggnb5tr |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn fadefinder.wsgi > Procfile`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")  # only if using Cloudinary

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/ZakariyeNor/FadeFinder).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/ZakariyeNor/FadeFinder.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://www.github.com/ZakariyeNor/FadeFinder)

**Please Note**: in order to directly open the project in Gitpod, you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/ZakariyeNor/FadeFinder).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

Throughout the development of this project, I have used various resources, tools, and references that have helped shape and improve the application. This section acknowledges the individuals, tutorials, open-source libraries, and documentation that contributed to the project’s success.

### Content

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | "How to Write a Git Commit Message" |
| [I Think Therefore I Blog](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Cloudinary API](https://cloudinary.com) | Cloud storage for static/media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [ChatGPT](https://chatgpt.com) | Help with code logic, help to make faster the testing process and explanations |
| [FontAwesome](https://fontawesome.com) | Icon library for scalable vector icons |
| [Flatpickr](https://flatpickr.js.org) | Lightweight and powerful date picker |
| [jQuery](https://jquery.com) | JavaScript library for simplifying HTML DOM manipulation |
| [Bootstrap](https://getbootstrap.com) | Front-end framework for responsive web design |
| [Django Tutorial Playlist](https://www.youtube.com/playlist?list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM) | Django tutorial series for beginners |

### Media

### Media Attribution

- **Logo**: The logo used in this project(about page"Baber booking center") is owned by me.
- **Cover Image**: The cover image used in this project is from the official [Django Walkthrough](https://github.com/ZakariyeNor/django-semi).
- The scissors logo in the large screen size is [Font Awesome](https://fontawesome.com).
- **Email**: The email connected to the contact us form (barberbooking@example.com) is owned and managed by me.

### Images & Content Sources

- **Images**  
  - [Pexels](https://www.pexels.com) - Free stock images  

- **Text & Content**  
  - Generated using ChatGPT 
  - Design Ideation: The concept of balanced typography, fonts, colors, sizing, and spacing was developed with the help of ChatGPT ideation.

- **Maps**  
  - [Google Maps](https://www.google.com/maps) - Integrated for location services  

### Contact Form

- **Contact Us Form**  
  - Powered by [Formspree](https://formspree.io) for handling form submissions

### Acknowledgements

I would like to acknowledge and thank those who have contributed to the success of this project. Their support, tools, and resources have been invaluable throughout my development process.

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
- I would like to thank God, who gave me the ability to do all of these and remain consistent.
