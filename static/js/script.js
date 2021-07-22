//jshint esversion: 6
/*globals $:false */

$(document).ready(function () {
  //Preloader, once the document loads fade out the preloader 
  $(".preloader").delay(1000).fadeOut('slow');

  /** Initializing Materialize components
   *   Initilize sidenav
   *   Open the sidenav to the right
   */

  $('.sidenav').sidenav({
    edge: 'right'
  });

  /** Initializing carousel
   * Set an Interval functions
   * which shows next item every 2 sec
   */
  $('.carousel').carousel();
  setInterval(function () {
    $('.carousel').carousel('next');
  }, 2000);

  // select option for add_product.html
  $('select').formSelect();

  //modal
  $('.modal').modal();

  // tooltip
  $('.tooltipped').tooltip();

  //validate select element from Materialize class
  // this code was taken from Task Manager walkthrough project 
  //https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/6449dcd23ca14016aa83dc7313d91a02/?child=first
  validateMaterializeSelect();

  function validateMaterializeSelect() {
    let classValid = {
      "border-bottom": "1px solid #4caf50",
      "box-shadow": "0 1px 0 0 #4caf50"
    };
    let classInvalid = {
      "border-bottom": "1px solid #f44336",
      "box-shadow": "0 1px 0 0 #f44336"
    };
    if ($("select.validate").prop("required")) {
      $("select.validate").css({
        "display": "block",
        "height": "0",
        "padding": "0",
        "width": "0",
        "position": "absolute"
      });
    }
    $(".select-wrapper input.select-dropdown").on("focusin", function () {
      $(this).parent(".select-wrapper").on("change", function () {
        if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
          $(this).children("input").css(classValid);
        }
      });
    }).on("click", function () {
      if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
        $(this).parent(".select-wrapper").children("input").css(classValid);
      } else {
        $(".select-wrapper input.select-dropdown").on("focusout", function () {
          if ($(this).parent(".select-wrapper").children("select").prop("required")) {
            if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
              $(this).parent(".select-wrapper").children("input").css(classInvalid);
            }
          }
        });
      }
    });
  }
  /**
   * Function which is for Products.html
   * on hover of the icon
   * Appends a new <span> element to HTML
   * Custom message for each icon is displayed
   * To tell the user what the icon represents
   * Then fade out method is used
   * to remove the last <span> element
   */
  $(".speed").hover(
    function () {
      $(this).append($("<span class='hover-effect disp-top'>max speed</span>"));
    },
    function () {
      $(this).find("span").last().toggle();
    }
  );
  $(".battery").hover(
    function () {
      $(this).append($("<span class='hover-effect disp-bottom'>charging time</span>"));
    },
    function () {
      $(this).find("span").last().toggle();
    }
  );
  $(".range").hover(
    function () {
      $(this).append($("<span class='hover-effect disp-bottom'>max range</span>"));
    },
    function () {
      $(this).find("span").last().toggle();
    }
  );
});