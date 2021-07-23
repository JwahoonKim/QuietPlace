$(window).scroll(function(evt) {
    var y = $(this).scrollTop();
    if (y > 120) {
       $('.android-header').removeClass('border-added-header');
 
    } else{
       $('android-header').addClass('border-added-header');
    }
 });