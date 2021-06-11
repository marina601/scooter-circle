$(document).ready(function(){
    $('.sidenav').sidenav({edge: 'right'});
    $('.carousel').carousel();
    $('#textarea1').val('Write Your Review Here..');
  M.textareaAutoResize($('#textarea1'));
  $('.carousel.carousel-slider').carousel({
    fullWidth: true,
    indicators: true
  });
  // select option for add product page
  $('select').formSelect();
  });