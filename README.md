[Tutoring Site Live Link](https://tutoring-hub.herokuapp.com/)
[Github Repository](https://github.com/sophiebatten123/Tutoring-Hub)

# TutoHub

(Developer: Sophie Batten)

TutorHub offers secondary school pupils world class tuition FREE as part of the education recovery plan. It is vital, now more than ever, that students are able gain a deeper relational understanding of concepts and understand the practical nature of STEM subjects, all of which have been set aside throughout the pandemic. Our tutors deliver their lesson via [Microsoft Teams](https://www.microsoft.com/en-gb/microsoft-teams/group-chat-software?rtc=1) which ensures no smart technology is required and gives all pupils regardless of their background the opportunity to learn.

The site is fully responsive and designed in a simplistic and easy to navigate manner. It has been coded using HTML, CSS, JavaScript, Python and Django using the MVC framework to scaffold the design process. Furthermore, the project went through continuos agile development to ensure features were working effectively.

![Am I Responsive?]()

# Table of Contents:

- [UX](#ux)
  - [User Stories](#user-stories)
  - [Agile Planning](#agile-planning)
  - [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
  - [Wireframes](#wireframes)
    - [Desktop Wireframes](#desktop-wireframe)
    - [Mobile Wireframes](#mobile-wireframe)
    - [Logic Function Wireframe](#logic-functions-wireframe)
    - [Site Improvements](#site-improvements)
  - [Features](#features)
    - [Register/ Login](#login)
    - [Create Student Profiles](#profiles)
    - [Book in Tutoring Lessons](#bookings)
    - [View/Cancel Upcoming Lessons](#view)
    - [Leave Tutor Reviews](#rate)
  - [Deployed Website](#deployed-website)
    - [Desktop Homepage](#desktop-home)
    - [Mobile Homepage](#mobile-home)
 - [Functionality](#functionality)
    - [Fixed Bugs and Errors](#fixed-bugs-and-errors)
    - [Technologies Used](#technologies-used)
    - [Programs Used](#programs-used)
- [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Automatic Testing](#automatic-testing)
    - [Wave Testing](#wave-testing)
- [Future Features](#future-features)
- [Deployment](#deployment)
- [Credits](#credits)

# UX

## User Stories

### First Time Visitor Goals:
1. As a First Time Visitor, I should be able to sign up for a student account.
2. As a First Time Visitor, I should be able to create a profile page based upon my subject needs.
3. As a First Time Visitor, I should have clear instructions on how tutoring sessions are ran.
4. As a First Time Visitor, I should be able to view the tutors profiles, qualifications and reviews.
5. As a First Time Visitor, I should be able to book in a tutoring session with one of the tutors.

### Returning Visitor Goals:
6. As a Returning Visitor, I should be able to view upcoming tutoring sessions on my profile page.
7. As a Returning Visitor, I should be able to cancel bookings that I am no longer able to attend.
8. As a Returning Visitor, I should be able to leave reviews on the tutor pages. 

### Frequent Visitor Goals:
9. As a Frequent Visitor, I should be able to access further learning through useful subject links and games.
10. As a Frequent Visitor, I should be able to edit my account in the event that my details change.

# Agile Planning Enviroment

## MoSCow Method

Throughout my project I frequently used the project board on GitHub ensuring I carefully followed the MoSCow method.

To ensure that the ideas I had for my project were realistic in the timeframe given it was important to:
- Ensure the 'Must Have' elements never exceeded 60% of the assigned tasks.
- Regularly update the project board and reflect upon each iteration.
- Refer to the project board regularly to keep focussed throughout the project.

Using the MoSCow technique was extremely useful and helped me to accomplish more during my project. 
Below is a screenshot of the Agile Planning enviroment that I used throughout my project:

![Agile-Planning](static/images/agile.png)

# Design

Throughout this project it was important that the design of the site was simplistic and carefully incorporated contrasting colours. 
This was accomplisheed by delicately adding turqouise and orange within the icons, button and header elements on the page. 

By using this technique the following criteria was accomplished:
- Foreground elements were never hindered by the background colours.
- Elements of importance stood out clearly on the page for the user. 
- Site navigation was clear, cohesive and easy to navigate.

## Colour Scheme

The colours for the site were selected through product research. It became clear that similar sites often use contrasting colours, making things 'pop' on the page. Furthermore it was important that the colours on the site allowed an easy flow of content throughout.

![Colour-Scheme](static/images/colours.png)

## Typography

Fonts were equally important on the site. The aim was to create a childish feeling to the site, complementing the cartoon imagery seen within the header image. Moreover, text colours were kept simple either black or white with only the icon colours changing. This was to ensure that the information was accessible to users who may be visaully impaired.

![Typography](static/images/navigation.png)
![Typography](static/images/text.png)

## Imagery

![Imagery](static/images/images.png)

# Wireframes

## Desktop Wireframes

<details>
    <summary>Desktop Wireframes - Click Here:</summary>
    <img src="static/images/desktop-home-wireframe.png" width="500">
    <img src="static/images/desktop-student-wireframe.png" width="500">
    <img src="static/images/desktop-tutor-wireframe.png" width="500">
    <img src="static/images/booking-wireframe.png" width="500">
</details>

## Mobile Wireframes

<details>
    <summary>Mobile Wireframes - Click Here:</summary>
    <img src="static/images/mobile-home-wireframe.png" width="500">
    <img src="static/images/mobile-student-wireframe.png" width="500">
    <img src="static/images/mobile-tutor-wireframe.png" width="500">
    <img src="static/images/booking-wireframe.png" width="500">
</details>

## Logic Function Wireframes

<details>
    <summary>Logic Function Wireframes - Click Here:</summary>
    <img src="static/images/lucid.png" width="700">
</details>

#
# Site Improvements

TutorHub has a few oppurtunities for devlopment that would complement the sites purpose. These include:

- Users would benefit from the option to 'rearrange' lesson bookings as opposed to just having the option to cancel them.
- Users would benefit from recieving email confirmation when a lesson has been successfully booked.
- Users would benefit from the ability to share good work on the site, this would help contribute to the community ethos.

# Features

## Register/ Login

- Upon entering the site users have the option to sign up for an account or, if already registered, login to their pre-existing accounts. (User Story 1)
- This feature allows the user to book in lessons, leave tutor reviews and share their work. 
- Furthermore, it allows the user to have a more personalised experience on the site showing their information and allowing them to keep track of any upcoming bookings. 
- The login and register pages use the 'Django Allauth Framework'. They have further been styled to blend with the design of the site using colours that complement the rest of the page.

## Create a Student Profile

## Book in Tutoring Lessons

## View/Cancel Upcoming Lessons

## Leave Tutor Reviews

# Deployed Website

## Desktop Homepage

![Desktop-Homepage]()

Above is a screenshot of the deployed webiste in desktop view. It was really important throughout the design process that the layout was simplistic and that the main focus of the site was to get users to book lessons hence why this was central to the page.

## Mobile Homepage

![Mobile-Homepage]()

A screenshot of the website from a mobile device can be seen above. The site remained easy to navigate on mobile devices and the design ensured that the content was clear.

# 
# Testing

## Manual Testing 

## Automatic Testing 

## Wave Testing

#
# Deployment

The website was deployed using Github and Heroku through the following steps:

## Github

- Created a new github repository page using the 'Code Institute Template'.
- Opened the new repository by clicking on the 'Gitpod' button.
- Intsalled the relevant apps and packages needed to deploy to HEROKU.

## Django and Heroku

The Django Framework was intalled and my project deployed to HEROKU using the Code Institute [Django Blog Cheatsheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf).


# Credits

## Content

- The images used on my site were taken from [Shutterstock]().
- The icons included throughout the website were taken from [Font-Awesome](https://fontawesome.com/).
- The colour theme was chosen using [coolors](https://coolors.co/).
- Help and support was given by the Code Institute Tutors on some of the logic functions within the website. 

Thank you to the tutors of code institute for the help given throughout this project.