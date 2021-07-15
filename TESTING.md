# Scooter Circle - Testing details

[Main README.md file](README.md)

[View deployed site here](https://scooter-circle.herokuapp.com/)

# Table of Content

[**Testing**](#testing)
   - [**Validation Results**](#validation-results)
   - [**Testing User Stories**](#user-stories-testing)
   - [**Further Testing**](#further-testing)
      - [**Device Compatibility Table**](#device-compatibility-table)
      - [**Home Page**](#home-page)
      - [**Registration Page**](#registration-page)
      - [**Login Page**](#login-page)
      - [**Profile Page**](#profile-page)
      - [**Edit Review**](#edit-review)
      - [**Products Page**](#products-page)
      - [**View Product**](#view-product) 
      - [**Add Product**](#add-product) 
      - [**Edit Product**](#edit-product) 
      - [**Contact Page**](#contact-page) 
      - [**404.html**](#404.html)
      - [**500.html**](#500.html)
   - [**Google Lighthouse Testing**](#google-lighthouse-testing)
   - [**Cross Browser Compatibility Table**](#cross-browser-compatibility-table)
   - [**Bugs**](#bugs)

## Validation Results

- The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.
- I have also used JSHints for JavaScript and jQuery code.
- PEP8 has been used to ensure Python code is fully complient

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/)
  - The file passed without any errors

- [W3C Markup Validation](https://validator.w3.org/)
   - HTML code pass validation without major errors.
   - Type attribute has been removed from all texteria elements. 
   - Also `<a> type=submit` has been removed.

   ### Profile Page

   ### View Product

   #### All other pages have passed without errors.

- [W3C Link Checker](https://validator.w3.org/checklink)
   - All links have been checked and no errors have been detected, except on line 39 a link has returned an error. I have checked all the anchor links in the **modal** and changed them to buttons. Also the issue was with anchor link for the mobile navigation, I have added a `role="button"` to the anchor tag.
    
- [JSHint](https://jshint.com/)
   ### script.js 
      - No issues detected in this file.
      
   ### contact.js
      - JShint displaying a warning: "emailjs" one undefined variable.
      - Could not declare a variable for emailjs due to this variable is taken from the emailJS installation code.

- [PEP8](http://pep8online.com/)
   - The code passed through validation without errors
   

##### back to [content](#table-of-content)

## User stories testing

### Testing user stories from UX section of [README.md](README.md)

#### First Time User

1.	As a first time user, I want to understand what this site is about.

  - The site is designed with a simple and easy to understand content.
  - Scooter logo in the header tells the user this site is about scooters.
  - A hero image clearly tells the user the site is about scoooters 
  - A testimony positioned on the right hand side explains to the user why electric scooters are 
  a environmentaly friendly and a fast way to travel.

2.	As a first time user, I want to view a collection of products available on site.

  - Once the user scrolls down the page is presented with a welcome message
  - Telling the user what they can do on this site: 
    - View latest scooter models
    - View user reviews 
    - Add your review
  - Collection of products are presented in the carousel format, which moves to the next slide in 2 seconds intervals.

3.	As a first-time user, I want to be able to see more products and user reviews.

  - The user can view full selection of scooters by clicking on the button, at the bottom of the page 
  *"View All Scooters"*
  - The first-time user will be redirected to the *Login* Page, where the message at the top of the page will tell them "You must be logged in to view this page". 
  - If the user does not have account yet, they can click a button *Regester Here* at the bottom of the form and proceed to the registraction page.
  - A first time user may register by filling up a simple form, which is asking for their username and password. 
  - Once the user is registered they will be redirected to their profile page.
  - Once the user is logged in, they are able to view all the products in the *Products* page
  - The products are presented in the form of the cards, with a few categories and the number of the reviews each product has.
  - Once a specific product has been selected, they may click on the link to *View Full Details* whic will lead them to full product specification and individual products reviews.

4.  As a first-time user, I want to view the terms and conditions of the site.

  - The user may click on the button in the footer of any page, the user is able to click a button "Terms and Conditions" which will open a modal with full terms and conditions of the site. 
  - The user has 2 options, either press the button to "Agree", which will close the modal.
  - Or the user may want to contact the site owners and ask more questions, the button "Contact" is presented next to "Agree" button in the modal, which will redirect the user to the *Contact Page*.

#### Returning User 

1.	As a returning user, I want to be able to login into my account

 - A returning user from *Home Page* may navigate to *Login Page* by pressing login link at the top of the navigation bar.
 - A form is pressented to the user which is asking for their username and password.
 - If the login attempt is successfull they will redirected to their profile page, where a wecome message will be displayed.
 - If one of the fields entries are innacurate, the message will be displayed to let them know either username of password is incorrect. 
 - The login form will be cleared and they user may try again.

2.	As a returning user, I want to view the full specification of a product

 - As a returning user, once the user have logged in, they are able to view full product details by: 
   - From the *Home* page by clicking on the image of the a scooter in the carousel 
   - From the *Products* page by clicking on the "View Full Details" link for one of the scooters, the user may view full product specifications and product reviews.

3.	As a returning user, I want to add my review to the product

 - Once the user logs in to their account, they will be redirected to the profile page.
 - A user which have not submitted any reviews will be presented with the message:
   - "Your have not reviewed any products yet!"
   - "Once you have reviewed some scooters, you will be able to manage your reviews here"
 - A link "View All Scooters" will derect them to *products* page.
 - When the user selects a specific scooter and views product details, after the product description, an open form is presented to the user with call to action "Review This Product"
 - The user may submit their review easily by filling in the form and pressing on the **Submit** button
 - Once the review has been submitted, the user will be redirected to their profile page. 
 - Feedback will be displayed to the user to let them know the "Your Review Has Been Added"
 - The user will be able to view the review which they added inside their *Profile* page.

4.	As a returning user, I want to be able to filter the product by category 
  
  - A returning user, may filter products from the *Products* page by: 
    - Range
    - Charging Time
    - Speed 
    - Price 
  - The results are presented to the user in the acsending or descending order, depending on the option picked by user. 

5.	As a returning user, I want to be able to search for products by brand or model.

  - A returning user may use search function, on the *Products* page, they may search products by brand or model
  - If the user searches for something that does not match any database query, the message will be displayed 
    - "No Results Found"
  - The user may choose to reset their search bar or filter options by pressing "Reset" button, which will display all the products in the database again.


#### Frequent User

1.	As a frequent user, I want to be able to view my reviews.

  - As a frequent user, upon successfull login attempt, the user may view all their reviews on their *Profile* page 

2.	As a frequent user, I want to be able to update my review. 

  - As a frequent user, they are able to update thier product review by clicking **Edit** in the review card.
  - The user will redirected to the **Edit Review Page**, where the user will be presented with a pre-filled form with their review.
  - The user may delete something text or add some text to their review. 
  - Once the user presses *Submit* button they will be redirect to their profile page
  - Feedback will be displayed:
    - "Your Review Has Been Succsefully Updated"
  - The user may view updated review in their *Profiel* page.
  - If the user presses on **Cancel** button when updating their review, it will redirect them back to the *Profile* page and no changes will be made to their original review.

3.	As a frequent user, I want to be able to delete my review. 
4.	As a frequent user, I want to read other user’s reviews.
5.	As a frequent user, I want to be able to contact the site and request other scooter models to be added to the list.
6.	As a frequent user, I want to know where I can purchase the product.
7.  As a frequent user, I want to be able to search for products by brand or model.

### Business goals

1.	As a business owner, I want to provide a platform for users where they can view and add reviews for electric scooters.
2.	As a business owner, I want the user to be able to register with secure login details.
3.	As a business owner, I want the client to be able to use the site easily on any device.
4.	As a business owner, I want to provide useful links to users where they can purchase products and earn an affiliate commission.
5.	As a business owner, I want to be able to delete any reviews which I consider to be inappropriate or out of content.
6.	As a business owner, I want to be able to add additional new products to the site. 
7.  As a business owner, I want to be able to edit or delete products.
8.  As a business owner, I want to provide the user with search and filter functionality for products to enable easy access to the database.

##### back to [content](#table-of-content)


##### back to [content](#table-of-content)