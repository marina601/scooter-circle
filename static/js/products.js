$(document).ready(function () {
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