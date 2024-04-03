// script that adds the class red to the header tag 
// turn it red when the div#red_header tag is clicked

$('div#red_header').click(function () {
    $('header').addClass('red');
  });
