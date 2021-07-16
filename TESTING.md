# Scooter Circle - Testing details

[Main README.md file](README.md)

[View deployed site here](https://scooter-circle.herokuapp.com/)

# Table of Content

[**Testing**](#testing)
   - [**Validation Results**](#validation-results)
   - [**Testing User Stories**](#user-stories-testing)
        - [**First Time User**](#first-time-user)
        - [**Returning User**](#returning-user)
        - [**Frequent User**](#frequent-user)
        - [**Business Goals**](#business-goals)
   - [**Further Testing**](#further-testing)
      - [**Device Compatibility Table**](#device-compatibility-table)
      - [**Elements on Every Page**](#elements-on-every-page)
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

- [Extendclass](https://extendsclass.com/python-tester.html)
   - No syntax errors have been found

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

##### back to [content](#table-of-content)

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

##### back to [content](#table-of-content)

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

  - From *Profile* page, where all user reviews are displayed, the user may click on **Delete** button for a specific review.
  - Once the button is pressed a modal will appear which will ask the user to confirm their selection
  - If the user presses **Yes** the review will be deleted from the databese
  - The user will be informed 
    - "You review has been Deleted"
  - The deleted review will be deleted from the database and will not appear on the user profile page. 
  - If the user presses **No**, the modal will close and no chages will be made.

4.	As a frequent user, I want to read other user’s reviews.

  - The user may find out how many reviews each product has by going to **Products** page
  - Scooter image and short specification is displayed in the card format for each scooter in the database
  - Inside the scooter card the total number of reviews are displayed, therefore the user will be aware how many reviews each product has. 
  - The user can view the scooter reviews by clicking "View Full Details" link, which will lead them to *View Product* page, below add review form, they will be able to view all other product reviews created by users. 
  - If the product does not have any reviews the message will be displayed: 
    - "No Reviews Added Yet!"
  - A call to action is displayed for the user to add thier own reveiw with an anchor link to add-review form.
  - At the bottom of the page the user has another option to "Go Back To Products", which will them to the *Products* page.

5.	As a frequent user, I want to be able to contact the site and request other scooter models to be added to the list.

  - The user may contact the site owner by pressing on the link in the **Footer** which stays *Contact*.
  - The link will lead them to the *Contact Page*.
  - The user is welcomed with a short message, which explains to them how they can get in touch.
  - The user needs to fill in their: 
    - Name
    - Email
    - Query
  - Once all the input fields filled in correctly the user is able to submit the form.
  - If the input fields are not filled in correctly custom messages are displayed to guide the user through proccess.
  - Once the form has been submitted, the alert is displayed to the user letting them know their message has been sent.
  - Automated message is sent to the user at the same time to let them know somebody will be in touch shortly.
  - The user now have an option at the bottom of the page to press a button "Go Back To Home Page"
  - Which will redirect the user to the *Home Page*
  - The user may choose to press **Reset** button at any time to clear the form.

6.	As a frequent user, I want to know where I can purchase the product.

  - A frequent user may click on **Buy This Scooter** button in the *View Product Page* below the product description. 
  - The link will take the user to a different site, which will be open in the new tab, letting the user have easy access back to the site.
  - The user may choose to purchase the product from the the site the link leads to. 

7. As a frequent user, I want to be able to search for products by brand or model.

  - The user inside the *Producst Page* has an option to search for product brand or model inside the search bar. 
  - The user is informed with pre-filled text, what should be their search creterea. 
  - The use is also given an option to filter the products by categories. 

### Business goals

1.	As a business owner, I want to provide a platform for users where they can view and add reviews for electric scooters.

  - The user may add scooter review, when viewing full product details of specific scooter model. 
  - At this point the user will also see the other user reviews at the bottom of the page.
  - The user will be able to see how many reviews each product has by viewing all the products on the *Product* page. The total number of reviews presented to the user in the form of the card with product info.

2.	As a business owner, I want the user to be able to register with secure login details.

  - Scooter Circle has been designed to simplify registration process for the user and ensue the user details are stored securely.
  - For the user to register they have to provide the username
  - Also have to type thier choisen password twice, once both of the password fields match, the data gets stored in the database.
  - I have usede `generate_password_hash` method from `werkzeug.security` to hash the password in the database. 
  - The site owner who will have access to the database, will be able to see the username, however will not be able to see the user password which is stored securily. 
  - Username may access their account only when username and password match the database, upon the login attempt.

3.	As a business owner, I want the client to be able to use the site easily on any device.

 - Scooter Circle was carefully planned and designed to be responsive and work well on mobile, tablet and desktop devices.

4.	As a business owner, I want to provide useful links to users where they can purchase products and earn an affiliate commission.

   - The link 'Buy This Scooter' has been added to each product in *View Product Page* which leads to an external company, where the product can be purchased. 
   - The [Pure Electric](https://www.pureelectric.com/) do offer affiliate partnership, however this has not been implemented yet, as this project is for educational purposes at this moment in time.

5.	As a business owner, I want to be able to delete any reviews which I consider to be inappropriate or out of content.

  - An admin user has all the reviews visible on their profile page.
  - An admin user may delete any review they find innapropriate or out of content.
  - An admin user will not have access to edit any of the reviews which have not been created by themselfs.
  - This information is provided to the user in *Terms and Conditions Page*, which they have access to at all times by clicking a button in the footer.

6.	As a business owner, I want to be able to add additional new products to the site. 

  - An admin user has *Add Product* page available to them.
  - A simple form which guides the Admin to fill in all the input fields which are required to display full product information on the site.
  - All the input fields have required attributes with custom feedback to the user, to ensuer all the information is entered correctrly.
  - Once the **Submit** button is pressed the product will be added to the database. 
  - The user will be redirected to the *Products Page* and feedback will be provided.
  - An admin user may clear the form at any time by pressing the button **Clear**

7.  As a business owner, I want to be able to edit or delete products.

  - An admin user, in the *Product Page* at the bottom of the each product card, have two buttons to **Edit** or **Delete** a product.
  - If *Edit* option is chosen, the admin user may update product information
  - If *Delete* option is chosen, the admin user may delete the product from the database.
  - In the event of the *Delete* option, a modal will appear to ask the admin user to confim their decision.

8.  As a business owner, I want to provide the user with search and filter functionality for products to enable easy access to the database.

 - Scooter Circle has been designed with user experience in mind, providing a platform for users, not only to view the products and product reviews, but also search for a specific item.
 - Search funcitonality implemented to enable the user to search by scooter model or brand.
 - Also Filter function is implemented to let the user filter the results with their choisen category in mind. 
 - Only 4 categories are avaialbe for user to filter by at the moment, those categories have been chosed based on the importance of the their value to the product.
 
##### back to [content](#table-of-content)

## Further Testing

### Manual (logical) testing of all elements and functionality on every page.

### Device compatibility table


| Pages    |<strong>Laptop</strong>|<strong>Ipad</strong>|<strong>IphoneX</strong> | <strong>Nokia2.4</strong> | <strong>Sumsung</strong> |
|----------|:---------------------:|--------------------:|------------------------:|-----------------------:|-----------------------:|
| Home     | &check; | &check;| &check;| &check;| &check;|
| Login   | &check; | &check;| &check;| &check;| &check;|   
| Register    | &check; | &check;| &check;| &check;| &check;|
| Products | &check; | &check;| &check;| &check;| &check;|
| View Product | &check; | &check;| &check;| &check;| &check;|
| Edit Product | &check; | &check;| &check;| &check;| &check;|
| Add Product | &check; | &check;| &check;| &check;| &check;|
| Edit Review | &check; | &check;| &check;| &check;| &check;|
| Profile | &check; | &check;| &check;| &check;| &check;|
| 400.html | &check; | &check;| &check;| &check;| &check;|
    
##### back to [content](#table-of-content)

### Elements on Every Page 

- All steps on desktop were repeated on mobile, tablet and laptop screen sizes.

1. Navigation

- Hover over each link, confirm the hover effect works as expected.
- Click the Scooter Circle logo, confirm it takes the user to the home page.
- Click the Home link, confirm it takes the user to the home page.
- Click the Login link, confirm it takes the user to the login page.
- Click the Register link, confirm it takes the user to the register page.
- Log into Scooter Circle, confirm that the navbar no longer displays the Login or Register links,but does now display the Home, Products, Profile and Logout links instead.
  - Clcik on the Products link, confirm it takes the user to products page.
  - Click the Profile link, confirm it takes the user to their profile page.
  - Click the Log out link, confirm the user is logged out and the navbar returns to the logged out configuration.
- Log into Scooter Circle with Admin user details
  - Confirm Add Product link appears on the navbar
  - Click on Add Product link, confirm it takes the Admin user to the add product page.
- Go to the bottom of the page to make sure the navigation bar is sticky.

- Mobile and Tablet view:
  - Confirm Scooter Circle logo appears in the middle of the navbar as expected
  - Confirm burger button appears on the right hand side of the navbar
  - Click on the burger button, confirm navbar is collapsed with links available for home, login and register page.
  - Confirm Scooter Circle logo also appers in expanded view.
  - Click on the Scooter Circle logo in the expanded view, confirm takes the user to the home page.
  - Followed the same steps as above to determine all the links are working.
  - Flip the tablet and mobile devices to check responsiveness.

2. Footer

  - Hovered over each link, confirmed background colour changed as expected.
  - Click on contact link, confirmed it takes the user to the contact page.
  - Click on terms and conditions button, confirm the modal appears with terms and conditions of the site.
  - The footer is responsive on all window view sizes.

3. Preloader

 - Open any page and confirm that the preloader displays for 1 seconds as the page content is loaded.
 - Confirm the preloader animates as expected.

### Home Page

1. Hero Image
   - Confirm the background image loads in the reasonable time
   - Confirm the background image has fixed position by scorolling up the page

2. Testimony
   - Starting from the desktop view the testimony has a Materialize margin to the right class. Featuring the man on the scooter in the background. 
   - View the page in the tablet view the testimony still has a margin to the right, the user is still able to see the view of the man on the scooter.
   - Chance the screen size to mobile view, the testimony appears in the middle of the page. 
   - The testimony background contains *RGBA* colour with allowed a semi-transparent background for the use to be able to see the background image.
   - On the mobile device, `margin-bottom` has been implemented to let the user see the background image once they scroll.

4. Wecome Message 
   - View the wecome message on all devices, confirm the message appears in the center of the page.

3. Carousell 
   - View the carousels and confirm that they slide a comfortable speed and interval.
   - Confirm the carousel if viewed in 3d format on tablet and large screen devices.
   - Poin with the mouse on the carousel item, the pointer is displayed to let the user know the carousel item is clickable
   - Click on the image on the left, confirm the carousel stops and reverst to the image clicked
   - Click on the image on the right, confirm the carousel speeds up to the image clicked by the user
   - Move mouse away from carousel, confirm that carousel starts moving again.
   - Confrim each carousel image has the same width and height
   - Confrim each image has a `alt` description
   - Click on carousel image and confirm it directs a non logged in user to login page.
   - Login to Scooter Circle, click on any carousel image and confirm the link directs to view product page of the product chosen to view.

  - Above tests have been repeated on the tablet and mobile devices with a few exceptions:
    - Confrim the carusel is touch compatble by sliding the fingers to the left and right
    - On the mobile view confirm the carousel is viewed by one carousel item at the time.

5. Call to Action 

  - View all scooters call to action button appears at the bottom of the page.
  - Hover over the link, confirm background colour is changing as expected.
  - Click on the link, confirm it takes the not logged in user to the login page.
  - Custom message is displayed to tell the user they must be logged in to view this page. 
  - Login to Scooter Circle, click on the link, confirm it takes the user to the products page.
  - Confirm the link appears in the middle of the page on all screen size devices. 
  - All the steps above have been repeated on all screen sizes. 




## Bugs

### Add Review and Edit Review 
  - Whilst testing user stories, I realized the user is able to amend the product_model name, which would lead to review added not matching any products and only appearing on the user profile page. 
  - I have fixed it by including `readonly="readonly"` attribut to the **input** element.

### Navbar
  - Little but noticed during testing, Scooter Circle logo, when hovered, was displaying extra height. 
  - Fix: remove hight property in css

##### back to [content](#table-of-content)