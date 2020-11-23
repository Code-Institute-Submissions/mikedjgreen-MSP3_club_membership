/*
    jQuery for MaterializeCSS initialization
    Mobile sidebar...
    Date Picker...
    Select ...
    Carousel...... [Gallery]
*/

$(document).ready(function() {

    $(".sidenav").sidenav({edge: "left"});

    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 2,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
    
    $("select").formSelect();
    
    $(".carousel").carousel();

    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true
    });
    
});

/*
    Carousel specific method calls with javascript, as jQuery being 
    phased out by Materialize..
*/

function nextSlide() {
     var instance = M.Carousel.getInstance(elem);
     return instance.next();
}

function prevSlide() {
     var instance = M.Carousel.getInstance(elem);
     return instance.prev();
}

/*
        once logged in successfully and loading members page,
        displaying any buttons classed as 'crud-btn'.
        So that known users can create,edit and delete records.
*/
function enableCRUD() {
    
        $(".crud-btn").css("display","block");

}

function displaySessionItems() {
  var i;
  document.getElementById("demo").innerHTML = "";
  for (i = 0; i < sessionStorage.length; i++) {
    x = sessionStorage.key(i);
    y = sessionStorage.getItem(x);
    document.getElementById("demo").innerHTML += x + ":" + y + "<br>";
  }
}
