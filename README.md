# Scooter Circle

![Scooter Circle](/assets/images/responsive-design.png "Am I Responsive Image") 

[View the website on GitHub Pages](https://mar)

I have created this site as part of my Milestone 3 project for Code Institute, 
focusing on Fulls Stack Frameworks using Python, Flask and Mongo DB.

This app is for young adults between the age of 25-34, who are focused on environmentally friendly, easy to use and cost effective personal tranportation.


This website will enable the user to share their own experience, view other users experience and find the best scooter based on their everyday needs.


# Table of Content

1 [**Project Goals**](#project-goals)

2 [**UX**](#ux)
   - [**User Goals**](#user-goals)
   - [**Scope**](#scope)

3 [**Structure of the app**](#structure-of-the-app)
   - [**View for a guest user**](#view-for-a-guest-user)
   - [**View for logged in user**](#view-for-logged-in-user) 
   - [**View for admin**](#view-for-admin)
   - [**User Stories**](#user-stories)
   - [**Business goals**](#business-goals)

4 [**User Requirements and Expectations**](#user-requirements-and-expectations)
   - [**Requirements**](#requirements)
   - [**Expectations**](#expectations)

5 [**Design**](#design)

6 [**Wireframes Flowchart and Data Model**](#wireframes-flowchart-and-data-model)
   - [**Wireframes**](#wireframes)
   - [**Database model**](#database-model)
   - [**Flow Chart**](#flow-chart)

7 [**Features**](#features)

  - [**Features Implemented**](#features-implemented)
    - [**All Pages**](#all-pages)
    - [**Landing Page**](#landing-page)
    - [**Registration Page**](#registration-page)
    - [**Login Page**](#login-page)
    - [**Profile Page**](#profile-page)
    - [**Add Review**](#add-review) 
    - [**Add Product**](#add-product) 
    - [**Terms and Conditions**](#terms-and-conditions) 
    - [**Affiliate Disclaimer**](#affiliate-disclaimer) 
    - [**404.html**](#404.html)
  - [**Features Left to Implement**](#features-left-to-implement)

8 [**Technology Used**](#technology-used)
   - [**Languages Used**](#language-used)
   - [**Frameworks Libraries and Programs Used**](#frameworks-libraries-and-programs-used) 

9 [**Testing**](#testing)
   - [TESTING.md file](TESTING.md)

10 [**Deployment**](#deployment)
   - [**Local Deployment**](#local-deployment)
   - [**Clone this project**](#clone-this-project)
   
11 [**Credits**](#credits)
   - [**Code**](#code)
   - [**Media**](#media)
   - [**Acknowledgement**](#acknowledgement)

12 [**Disclaimer**](#disclaimer)

## Project Goals 

Following the market research, the demand for electrical and affordable transportation has risen in April 2021 by 3.8% from LY in the UK.
At the end of 202, and electric scooters were at the top of many Christmas lists, with sales trebling within a year and Halfords reporting that October alone saw sales of the zippy personal transport gadgets up a massive 450% on the previous year.

This app will provide a user with the possibility to view the scooters on the market, check out customer reviews of the product and add their personal experience. 

##### back to [content](#table-of-content)

## UX

### User Goals:

- The website has to be easy to navigate and be responsive across all screen size devices
- Login procedure should be simple and feedback should be given when appropriate
- Registration process should be clear, easy to follow and feedback should be given when appropriate 
- The product information should be presented in a clear format and easy to understand 
- The reviews should be easy to see and add 
- The current user should be able to update and delete their reviews 
- The website should provide information on where the product can be purchased if the user decides to buy it.

##### back to [content](#table-of-content)


### Scope

- An easy to navigate and responsive website that allows users to perform CRUD operations. 
- Users can register and once log in can view full product details, other users reviews and share their own experience by adding a review to an appropriate product. 
- These users manage their reviews, meaning they can update or delete them when they want. 
- In the user profile, they will be able to see the collection of products they have reviewed. 
- The user may contact the site owner and suggest adding new products to the site. 
- The site owner in a form of an Admin user will be able to complete this operation directly on the website. 

##### back to [content](#table-of-content)

## Structure of the app

### View for a guest User:

-	A user which is not logged in and/or registered will be greeted with a hero image of the electric scooters and a couple of quotes about why electrical transportation is a better way to travel. 
-	A guest user can view the recent products at the bottom of the page which with the minimum specification. 
-	A guest user will only have 3 option visible to them in terms of navigation (Home, Login, Register)
-	A guest user will have a call to action button at the bottom of the page "View all Scooters” which will take them to the Login Page.
-	If a guest user did not register yet, they will be able to click on the "Register" button at the bottom of the form to go to the registration page. 
-	A guest user will be able to complete the form and register to access the full side. 

##### back to [content](#table-of-content)

### View for logged in User:

-	A logged-in user will benefit from the full functionality of the site. 
-	The navigation links will contain (Products, Profile, Add Review, Logout)
-	Logged in user can view the full range of products available on the site
-	Logged in user can add a review by clicking on the product, where an empty text field will be provided for them
-	Logged in user can view other users reviews for the selected product 
-	Logged in user can Edit or Delete their review 
-	Logged in user can see all the products which they have reviewed on their profile page 

##### back to [content](#table-of-content)

### View for Admin: 

-	The navigation links for Admin user will contain (Products, Profile, Add Product, Add Review, Logout)
-	Admin user will be able to add the product to the database by clicking on the link "Add Product" and fill in the pre-populated form 
-	Admin user will reserve the right to delete any inappropriate or offensive reviews from users if they breach the term and conditions of the site.

##### back to [content](#table-of-content)

### User Stories 

#### First Time User

1.	As the first time user, I want to understand what this site is about
2.	As the first time user, I want to view the most recent products 
3.	As a first-time user, I want to be able to see more products and user reviews.

#### Second Time User 

1.	As a second-time user, I want to be able to login into my account 
2.	As the second time user, I want to view the full specification of a specific product
3.	As the second time user, I want to add my review to the product
4.	As the second time user, I want to be able to filter the product by category 
5.	As a second-time user, I want to be able to search product by brand or model.

#### Frequent User

1.	As a frequent user, I want to be able to view the products which I have reviewed.
2.	As a frequent user, I want to be able to update my review. 
3.	As a frequent user, I want to be able to delete my review. 
4.	As a frequent user, I want to read other user’s review.
5.	As a frequent user, I want to be able to contact the site and request other scooter models to be added to the list.
6.	As a frequent user, I want to know where I can purchase the product.

##### back to [content](#table-of-content)

### Business goals

1.	As a business owner, I want to provide a platform for users where they can view and add reviews on electric scooters
2.	As a business owner, I want the user to be able to register with secure login details.
3.	As a business owner, I want the client to be able to use the site easily on any device.
4.	As a business owner, I want to provide useful links to users where they can purchase products and earn an affiliate commission.
5.	As a business owner, I want to be able to delete any reviews which I consider to be inappropriate or out of content 
6.	As a business owner, I want to be able to add additional products to the site. 

##### back to [content](#table-of-content)

## User Requirements and Expectations

### Requirements:

-	Easy to navigate the site by using buttons
-	Appealing profile page with a functional overview
-	Easy way to view other users reviews 
-	Easy way to add their review 
-	Ability to edit and delete their entities 

##### back to [content](#table-of-content)

### Expectations: 
 
-	Full specifications of the product
-	Ability to filter product by category 
-	Ability to search the database for a specific product name or brand
-	Ability to read other users reviews and add their own 
-	Ability to contact the site owner and suggest other scooters models be added to the database

##### back to [content](#table-of-content)

## Design 

### Colour Scheme 

### Typography
      
 [Google Fonts](https://fonts.google.com/) have been used on this page 
    - To give consistency to the users, the consistent font has been used throughout the site:

    - All the headings are displayed in font-family:
    - All other elements are displayed in font-family:

### Imagery

    - All the imagery is imported from 
[Pixabay](https://pixabay.com/)
    

     - Favicon icon has been sourced from 
[icons8](https://icons8.com/icons/set/cocktail)
    
##### back to [content](#table-of-content)

## Wireframes, Database and Flow Chart

### Wireframes 

##### back to [content](#table-of-content)

### Database model

##### back to [content](#table-of-content)

### Flow Chart

##### back to [content](#table-of-content)

## Features 

### Features Implemented 

Based on the user stories and expectations, the following features have been implemented:

### All pages:  
  
- Dynamic navigation menu collapses on the mobile screen view.
- The navigation is also custom based on the login details of the user 
  
- Contain sticky navigation allows the user to access the menu at any time.
  
- The website has a responsive design based on the screen view.
    
- All pages have call-to-action buttons to give the user easy access to the 
  
next page, without the need to choose from the navigation menu.
- Logo image on the left-hand side is presented throughout the pages and lead to the Home page if the user is not logged in, otherwise leads the user to the product page.
-Favicon Icon to improve user experience 

##### back to [content](#table-of-content)

### Landing Page: 

- The user is presented with a hero image which tells the user what to expect from the site
- Call to action button leads the user to log in before they can perform any actions or view any products

##### back to [content](#table-of-content)

### Registration Page: 

- Post the user data to the database
- Using a salt method to encrypt the password
- Checks the database if the user name exists
- The input fields have specific parameters to ensure correct user information is entered.
- If the user fails to comply with parameters, the relevant message will be displayed 
- Once the submit button is pressed the user will be redirected to their profile page

##### back to [content](#table-of-content)

### Login Page: 

- Request the data from the database
- Checks if the username matches the database
- Checks if the password matched the database
- Checks if the username and password match the correct user-id 
- If one of the checks fails, then the relevant message will be displayed asking the user to try again 
- Alternatively, if the user is not registered they can click “Register Button”, which will direct them to the registration page.

##### back to [content](#table-of-content)
 
### Profile Page: 
  
- The user is welcomed with a welcome message, which uses their username for identification 
- Once the user has reviewed some products, the products will appear on their profile page

Products Page: 
- Filter method has been implemented to let the user filter the products by product category 
- Search method has been introduced to let the user search by a brand of the scooter or model 
- Call to action buttons at the bottom of the product description one for “Full Details” which leads the user to view more information and add a review.
- “Shop” button will lead to an Affiliate Amazon site where the user can purchase this product 

##### back to [content](#table-of-content)

### Add Review

- Once the product is selected, it will appear on the add review page with a full description. 
- Textarea element prompts the user to add and submit the review 
- Once the review has been submitted, the user can see their review appearing in the carousel at the bottom of the page 
- The current user can delete or update their review 
- If the user chooses for the review to be deleted, a prompt will appear asking with the following message “You are about the delete your review. Are you sure?”
- The user can navigate through the reviews by touch or click on the left and right arrows 
- Admin user can delete any review found inappropriate to the site 

##### back to [content](#table-of-content)

### Add Product

- This option is only available for Admin user.
- The form is being populated for the Admin to enter the new products into the database
- The Admin can choose to reset the form by clicking on the “Reset Button”
- The Admin can choose to submit the form by clicking on the “Submit Button”
- All the fields will have the required attribute to ensure all the full information is submitted. 
Contact Page: 
- Once the user navigates to the contact page, a short message will appear telling the user why they might choose to get in touch with an admin
- The contact form is powered by EmailJS
- The contact form contains the required field to be filled in, it will not submit a black form 
- Once the Submit button has been pressed, the message will appear “Your message has been sent” 
- The form will refresh once the form has been submitted

##### back to [content](#table-of-content)

### Terms and Conditions 
- Populated by a modal, lets a user read the terms and conditions of the website
- The modal will closed by clicking on the “X” button at the right-hand corner 

##### back to [content](#table-of-content)

### Affiliate Disclaimer 
- Tells the user that the website has an affiliate income coming from the sale of any product purchased by clicking on the link “Shop”

##### back to [content](#table-of-content)

### 404.html
  
- Custom 404.html page has been created in case of an incorrect URL entered.
- The page contains a link that will lead the user back to the home page. 

##### back to [content](#table-of-content)

### Features Left to Implement 

##### back to [content](#table-of-content)

## Technology Used

### Language Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python]

##### back to [content](#table-of-content)

### Frameworks Libraries and Programs Used 

1. [Monitize 4.3]()
 - Mainly for responsive grid layout. 


2. [CSS tricks](https://css-tricks.com/perfect-full-page-background-image/) 
- Used to create a full background image for the main site and 404.html page.

3. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Akava and Prata' fonts into the style.css file which is used on all pages throughout the project.

4. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.

5. [jQuery](https://api.jquery.com/)
    - jQuery library has been used to target HTML elements and assign event listeners throughout JavaScript files.     

6. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

7. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git.

8. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process.

9. [TinyPng:](https://tinypng.com/)
   - TinyPng was used to compress the size of the images and improve loading time.

10. Lucid Chart to create a flow chart and database structure 

11. [Email-JS](https://www.emailjs.com/)
   - API is used to submit a contact form and send automated emails to the user.

12. [Grammarly](https://www.grammarly.com/)
    - Used to fix the thousands of grammar errors across the project.

13. [Gitpod](https://www.gitpod.io/)
    - Used as the development enviroment.

14. [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
    - Used as a primary method of fixing spacing issues, finding bugs, and testing responsiveness during the project development.

15. [Befunky](https://www.befunky.com/)
    - Online platform used to resize and crop images.
    
##### back to [content](#table-of-content)


## Testing

You can find testing information in [TESTING.md](TESTING.md)

##### back to [content](#table-of-content)

## Deployment

### Local Deployment

- I have created Scooter Circle using Github, from there I used Gitpod to write my code. Then I used commits to git followed by "git push" to my GitHub repository. I've deployed this project to Heroku and used "git push Heroku master" to make sure my pushes to GitHub were also made to Heroku.

- This project can be run locally by following the following steps: ( I used Gitpod for development, so the following steps will be specific to Gitpod. You will need to adjust them depending on your IDE. You can find more information about installing packages using pip and virtual environments [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

##### back to [content](#table-of-content)

### Clone this project:

-  From the application's repository, click the "code" button and download the zip of the repository. Alternatively, you can clone the repository using the following line in your terminal: git clone https://github.com/marina601/scooter-circle.com
-  Access the folder in your terminal window and install the application's required modules using the following command: pip3 install -r requirements.txt
-  Sign-in or sign-up to MongoDB and create a new cluster
-  Within the Sandbox, click the collections button and after click Create Database (Add My Own Data) called scooter_circle
-  Set up the following collections: users, products and reviews. Click to see the exact Database Structure
-  Under the Security menu on the left, select Database Access.
-  Add a new database user, and keep the credentials secure
-  Within the Network Access option, add IP Address 0.0.0.0
-  In your IDE, create a file containing your environmental variables called env.py at the root level of the application. It will need to contain the following lines and variables: import os

-

     os.environ  ["PORT"] = "5000"
     os.environ  ["SECRET_KEY"] = "YOUR_SECRET_KEY" 
     os.environ  ["DEBUG"] = "True"
     os.environ  ["MONGO_URI"] = "YOUR_MONGODB_URI"
     os.environ  ["MONGO_DBNAME"]= "DATABASE_NAME"


- Please note that you will need to update the SECRET_KEY with your secret key, as well as the MONGO_URI and MONGO_DBNAME variables with those provided by MongoDB. Tip for your SECRET_KEY, you can use a Password Generator to have a secure secret key.
- I recommend a length of 24 characters and exclude symbols. To find your MONGO_URI, go to your clusters and click on connect. Choose to connect your application and copy the link provided. 

- Don't forget to update the necessary fields like password and database name. If you plan on pushing this application to a public repository, ensure that env.py is added to your .gitignore file.

-	The application can now be run locally. In your terminal, type the following command python3 app.py.
To deploy your project on Heroku, use the following steps:
-	Login to your Heroku account and create a new app. Choose your region.
-	Ensure the Procfile and requirements.txt files exist are present and up-to-date in your local repository.

### Requirements:
    - pip3 freeze --local > requirements.txt

### Procfile:

    - echo web: python app.py > Procfil

- The Procfile should contain the following line:

      - web: python app.py

- And then:
	- Scroll down to the "deployment method"-section. Choose "Github" for automatic deployment.
	- From the inputs below, make sure your GitHub user is selected, and then enter the name for your repo. Click "search". When it finds the repo, click the "connect" button.
	- Scroll back up and click "settings".
	- Scroll down and click "Reveal config vars".
	- Set up the same variables as in your env.py (IP, PORT, SECRET_KEY, MONGO_URI and MONGODB_NAME):!You shouldn't set the DEBUG variable is under config vars, only in your env.py to prevent DEBUG from being active on the live website.

	     - PORT = 5000
	     - SECRET_KEY = YOUR_SECRET_KEY
	     - MONGO_URI = YOUR_MONGODB_URI
	     - MONGO_DBNAME = DATABASE_NAME

•	Scroll back up and click "Deploy". Scroll down and click "Enable automatic deployment".
•	Just beneath, click "Deploy branch". Heroku will now start building the app. When the build is complete, click "view app" to open it.
•	To commit your changes to the branch, use git push to push your changes.

##### back to [content](#table-of-content)

## Credits 

### Code

##### back to [content](#table-of-content)

### Media

##### back to [content](#table-of-content)

### Acknowledgement 

##### back to [content](#table-of-content)

## Disclaimer 
This website has been created for educational purposes only 

##### back to [content](#table-of-content)