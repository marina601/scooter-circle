//jshint esversion: 6
/*globals $:false */

$(document).ready(function () {
    /**
     * Function which on hover of the icon
     * Appends a new <span> element to HTML
     * Custom message for each icon is displayed
     * To tell the user what the icon represents
     * Then fade out method is used
     * to remove the last <span> element fast 
     */
    $(".speed").hover(
        function() {
            $(this).append($("<span class='hover-effect'>max speed</span>"));
        }, function() {
            $(this).find("span").last().fadeOut("fast");
        }
    );
    $(".battery").hover(
        function() {
            $(this).append($("<span class='hover-effect'>charging time</span>"));
        }, function() {
           $(this).find("span").last().fadeOut("fast");
        }
    );
    $(".range").hover(
        function() {
            $(this).append($("<span class='hover-effect'>max range</span>"));
        }, function() {
            $(this).find("span").last().fadeOut("fast");
        }
    );
});