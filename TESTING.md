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

## Validation Results

- The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.
- I have also used JSHints for JavaScript and jQuery code.
- PEP8 has been used to ensure Python code is fully complient

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/)
  - The file passed without any errors

- [W3C Markup Validation](https://validator.w3.org/)
   - HTML code pass validation without major errors, type attribute has been removed from all texteria elements. Also `<a> type=submit` has been removed. 

- [W3C Link Checker](https://validator.w3.org/checklink)
   - All links have been checked and no errors have been detected, except on line 39 not a link has returned an error. I have checked all the anchor links in the **modal** and changed them to buttons. Also the issue was with anchor link for mobile navigation, I have added a `role="button"` to the anchor tag.
    
- [JSHint](https://jshint.com/)
   ### recipes.js 
      - has presented the error where some missing semicolons had to be added.
      - byCategory function error: unused variable, however, I am calling this function in HTML file once the 
             filter buttons are clicked. 
      - jshint warning: "Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. ($)"
           - Solved the error by adding const $ = window.$ to jquery files.
      - Which resulted in breaking the jQuery code in the main deployed version of the website. 
      - Has removed a declared variable and used /*globals $:false */ this instead. 
      -JSHints was able to read this and display the code without errors.
   ### contact.js
      - JShint displaying a warning: "emailjs" one undefined variable.
      - Could not declare a variable for emailjs due to this variable is taken from the emailJS installation code.

   #### All other pages have passed without errors.

##### back to [content](#table-of-content)