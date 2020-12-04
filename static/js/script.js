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
        fullWidth: true,
        indicators: false,
    });

    $(".modal").modal();
    
    
});

/*
    Art Work buttons...
*/

function add_artwork() {
    $("#addartwork").css("display","block");
    $("#addartwork").css("position","sticky");
    $("#addartwork").css("z-index","+1");
}

/*
function edit_artwork() {
    $("#editartwork").css("display","block");
    $("#editartwork").css("position","sticky");
    $("#editartwork").css("z-index","+1");
    var btnedit = document.getElementById("btneditart")
    if ( btnedit.hasFocus() ) {
        btnedit.css("display","block")
    } else {
        btnedit.css("display","none")
    }
}
*/

function close_add_artwork() {
    $("#addartwork").css("display","none");
}

function close_edit_artwork() {
    $("#editartwork").css("display","none");
}

/*
    Carousel specific method calls with jQuery, though being 
    phased out by Materialize..
*/

function nextSlide() {
    $('.carousel').carousel('next');
}

function prevSlide() {
    $('.carousel').carousel('prev');
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
