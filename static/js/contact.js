//jshint esversion: 6

// declaring variables
var btn = document.getElementById('button');
var contactForm = document.getElementById('contact-form');
var userName = document.getElementById('from_name');

// declaring variables for serviceID and templateID
var serviceID = 'default_service';
var templateID = 'template_yz2jh7k';

/**
 * function which integrates emailJS service  
 * this code has been used from emailJS documents 
 * https://dashboard.emailjs.com/admin/integration
 */

(function () {

    emailjs.init('user_okiyBXoCAcvQ9Zao8GHSK');
})();

/**
 * Add event listener to the form element
 * on submit add an event listener to prevent 
 * default submission of the form
 * button value changes once the button is pressed 
 */

window.onload = function () {
    contactForm.addEventListener('submit', function (event) {
        event.preventDefault();
        btn.innerText = 'Sending...';

        /**
         * Submitting the form 
         * Submit button value changed to 'Sent' once the form is sent.
         * time out function to disable the submit button once the form has been submitted 
         * Alert letting the user know the message has been sent
         * Then the form will be cleared and reset
         * In case of an error 
         * Submit button is disabled 
         * Alert shows letting the user know the message has not been sent 
         */

        emailjs.sendForm(serviceID, templateID, this)
            .then(() => {
                btn.innerText = 'Sent';
                setTimeout(() => { btn.disabled = true; }, 1000);
                alert(`Thank you ${userName.value}. Your message has been sent! We will be in touch soon!`);
                contactForm.reset();

            }, (err) => {

                btn.innerText = 'Submit';
                btn.disabled = true;
                alert(alert(JSON.stringify(err)`Sorry ${userName.value} something went wrong`));
            });
        // To stop from loading a new page
        return false;
    });

};
