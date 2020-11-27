/*
    jQuery for MaterializeCSS initialization
    Mobile sidebar...
    Date Picker...
    Select ...
    Carousel...... [Gallery]
    Modal....[Gallery]
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
    
    $("carousel").carousel();

    $(".carousel.carousel-slider").carousel({
        fullWidth: false,
        indicators: true
    });

    $(".modal").modal();
    
    
});

/*
    Art Work buttons...
*/

function add_artwork() {
    $(".modal").css("display","block");
    $(".modal").css("position","sticky");
}

function close_artwork() {
    $(".modal").css("display","none");
}

/*
    Carousel specific method calls with javascript, as jQuery being 
    phased out by Materialize..
*/

function nextSlide() {
    $(".carousel-item").next();
}

function prevSlide() {
    $(".carousel-item").prev();
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
