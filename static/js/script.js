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
        format: "yyyy-mm-dd",
        yearRange: 2,
        showClearBtn: true,
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 1, // Creates a dropdown of 15 years to control year
        setDefaultDate: true,
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

function checkLogin() {
    if ( sessionStorage.getItem("logged") ) {
         enableCRUD();
    }
}

function enableCRUD() {
    $(".crud-btn").css("display","block");
    var crud = document.getElementsByClassName("crud-btn");
    crud.css("display","block");
    displaySessionItems();
}

function setSession(username) {
    sessionStorage.setItem("logged",username);
}
function unsetSession() {
    sessionStorage.removeItem("logged");
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

/*
    Using EmailJS API to send reminder emails to members to renew their subscription.
    ServiceId = gmail
    TemplateID = msp3
*/
function sendMail(contactForm) {
    emailjs.send("gmail", "msp3", {
        "to_email": contactForm.target.value,
        "from_name": contactForm.from_name.value,
        "from_email": contactForm.from_email.value,
        "to_member": contactForm.fullname.value,
        "membership_dues" : contactForm.dues.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  // To block from loading a new page
}
/*
    Display the email reminder form to send dues
*/
function show_reminder() {
    $("#emailreminder").css("display","block");
    $("#emailreminder").css("position","sticky");
    $("#emailreminder").css("z-index","+1");
}

function close_reminder() {
    $("#emailreminder").css("display","none");
}

function display_reminder() {
    /* to display the button on the members page */
    $("#btnreminder").css("display","block");
    $("#btnreminder").css("position","sticky"); 
    $("#btnreminder").css("z-index","+1");
}

/*
    Using EmailJS API to send news of club activities to members.
    ServiceId = gmail
    TemplateID = template_3skPculZ
*/
function sendNews(contactForm) {
    emailjs.send("gmail", "template_3skPculZ", {
        "to_email": contactForm.target.value,
        "from_name": contactForm.from_name.value,
        "from_email": contactForm.from_email.value,
        "to_member": contactForm.fullname.value,
        "title": contactForm.title.value,
        "date": contactForm.date.value,   
        "time": contactForm.time.value,
        "duration": contactForm.duration.value,
        "location": contactForm.location.value,
        "led": contactForm.led.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  // To block from loading a new page
}