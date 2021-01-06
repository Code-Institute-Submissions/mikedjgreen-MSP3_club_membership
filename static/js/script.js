const clubBlue = "#D9E6F3";

/*
    jQuery for MaterializeCSS initialization
    Mobile sidebar...
    Date Picker...
    Select ...
    Carousel...... [Gallery]
    Modal....[Gallery]
    Materialbox...for enlarging images
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
    
    $(".materialboxed").materialbox();
});

/*
    Membership form client-side validation
    onchange event occurs when the element loses focus
    if a field in error, retrieving focus.
*/

function mem_name(field) {
    var x = document.getElementById(field).value;
    if ( x.length < 4 ) {
        document.getElementById(field).style.backgroundColor = "red";
        document.getElementById(field).focus();
    } else {
        document.getElementById(field).style.backgroundColor = clubBlue;
        document.getElementById(field).style.color = "black";
        document.getElementById(field).style.fontWeight = "bold";
    }
}

function mem_email() {
    var x = document.getElementById("email").value;
    var pattern = 	new RegExp("^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+).([a-zA-Z]{2,5})$");
    if ( pattern.test(x)) {
        document.getElementById("email").style.backgroundColor = clubBlue;
        document.getElementById("email").style.color = "black";
        document.getElementById("email").style.fontWeight = "bold";
        document.getElementById("emailerror").innerHTML = "";
    } else {
        document.getElementById("email").style.backgroundColor = "red";
        document.getElementById("email").focus();
        document.getElementById("emailerror").innerHTML = "format incorrect - e.g. no @ ?";
    }

}

function mem_phone() {
    var x = document.getElementById("phone").value;
    var pattern = 	new RegExp("[^0-9]","g");
    if ( pattern.test(x)) {
        document.getElementById("phone").style.backgroundColor = "red";
        document.getElementById("phone").focus();
    } else {
        document.getElementById("phone").style.backgroundColor = clubBlue;
        document.getElementById("phone").style.color = "black";
        document.getElementById("phone").style.fontWeight = "bold";
    }
}
/*
    Art Work buttons...
*/

function add_artwork() {
    $("#addartwork").css("display","block");
    $("#addartwork").css("position","sticky");
    $("#addartwork").css("z-index","+1");
}

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
}

function disableCRUD() {
    $(".crud-btn").css("display","none");
}

function setSession(username) {
    sessionStorage.setItem("logged",username);
}

/*
    Called by log_off page
*/  
function unsetSession() {
    sessionStorage.removeItem("logged");
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
            console.log("SUCCESS", response.status, response.text);
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
        "led_by": contactForm.led_by.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response.status, response.text);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  // To block from loading a new page
}