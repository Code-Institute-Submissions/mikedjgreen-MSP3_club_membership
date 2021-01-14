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

function mem_bio() {
    var x = document.getElementById("bio").value;
    if ( x.length < 10 ) {
        document.getElementById("bio").style.backgroundColor = "red";
        document.getElementById("bio").focus();
    } else {
        document.getElementById("bio").style.backgroundColor = clubBlue;
        document.getElementById("bio").style.color = "black";
        document.getElementById("bio").style.fontWeight = "bold";
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
    Add activity form client-side validation.
    'onchange' event occurs when the element loses focus
    if a field in error, retrieving focus.
*/

function act_name(field) {
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

function act_desc() {
    var x = document.getElementById("description").value;
    if ( x.length < 10 ) {
        document.getElementById("description").style.backgroundColor = "red";
        document.getElementById("description").focus();
    } else {
        document.getElementById("description").style.backgroundColor = clubBlue;
        document.getElementById("description").style.color = "black";
        document.getElementById("description").style.fontWeight = "bold";
    }
}

function act_dur() {
    var x = document.getElementById("activity_duration").value;
    var patHour = new RegExp(/hour/i);
    var patMin  = new RegExp(/min/i);
    if ( patHour.test(x)) {
        document.getElementById("activity_duration").style.backgroundColor = clubBlue;
        document.getElementById("activity_duration").style.color = "black";
        document.getElementById("activity_duration").style.fontWeight = "bold";
        document.getElementById("duration_error").innerHTML = "";
    } else if ( patMin.test(x) ) {
        document.getElementById("activity_duration").style.backgroundColor = clubBlue;
        document.getElementById("activity_duration").style.color = "black";
        document.getElementById("activity_duration").style.fontWeight = "bold";
        document.getElementById("duration_error").innerHTML = "";        
    } else {    
        document.getElementById("activity_duration").style.backgroundColor = "red";
        document.getElementById("activity_duration").focus();
        document.getElementById("duration_error").innerHTML = "Duration should contain hour and/or minute";
    }    
}

function act_loc() {
    var x = document.getElementById("activity_location").value;
    if ( x.length < 10 ) {
        document.getElementById("activity_location").style.backgroundColor = "red";
        document.getElementById("activity_location").focus();
    } else {
        document.getElementById("activity_location").style.backgroundColor = clubBlue;
        document.getElementById("activity_location").style.color = "black";
        document.getElementById("activity_location").style.fontWeight = "bold";
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
    artworks form client-side validation.
    'onchange' event occurs when the element loses focus
    if a field in error, retrieving focus.
*/

function art_title() {
    var x = document.getElementById("title").value;
    if ( x.length < 10 ) {
        document.getElementById("title").style.backgroundColor = "red";
        document.getElementById("title").focus();
    } else {
        document.getElementById("title").style.backgroundColor = clubBlue;
        document.getElementById("title").style.color = "black";
        document.getElementById("title").style.fontWeight = "bold";
    }
}

function art_image() {
    var x = document.getElementById("image").value;
    var pattern = 	new RegExp(/..\/static\/img\/gallery/);
    if ( pattern.test(x)) {
        document.getElementById("image").style.backgroundColor = "red";
        document.getElementById("image").focus();
    } else {
        document.getElementById("image").style.backgroundColor = clubBlue;
        document.getElementById("image").style.color = "black";
        document.getElementById("image").style.fontWeight = "bold";
    }
}

function art_artist() {
    var x = document.getElementById("artist").value;
    if ( x.length < 4 ) {
        document.getElementById("artist").style.backgroundColor = "red";
        document.getElementById("artist").focus();
    } else {
        document.getElementById("artist").style.backgroundColor = clubBlue;
        document.getElementById("artist").style.color = "black";
        document.getElementById("artist").style.fontWeight = "bold";
    }
}


function art_media() {
    var x = document.getElementById("media").value;
    if ( x.length < 5 ) {
        document.getElementById("media").style.backgroundColor = "red";
        document.getElementById("media").focus();
    } else {
        document.getElementById("media").style.backgroundColor = clubBlue;
        document.getElementById("media").style.color = "black";
        document.getElementById("media").style.fontWeight = "bold";
    }
}

function art_dim(field) {
    var x = document.getElementById(field).value;
    if ( x.length < 5 ) {
        document.getElementById(field).style.backgroundColor = "red";
        document.getElementById(field).focus();
    } else {
        document.getElementById(field).style.backgroundColor = clubBlue;
        document.getElementById(field).style.color = "black";
        document.getElementById(field).style.fontWeight = "bold";
    }
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

function enableRemind() {
    $(".remind-btn").css("display","block");
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
    Called from reminder.html
*/
function sendMail() {
    var target = document.getElementById("target").value;
    var fullname = document.getElementById("fullname").value;
    var fromName = document.getElementById("from_name").value;
    var fromEmail = document.getElementById("from_email").value;
    var duesInput = document.getElementById("dues").value;

    var btn = document.getElementById("btnRemind");
    var btnText = document.createTextNode("sendMail FAILED");

    emailjs.send("gmail", "msp3", {
        "to_email": target,
        "from_name": fromName,  // "Prickwillow Art Club",
        "from_email": fromEmail, //"prickwillowartclub@gmail.com",
        "to_member": fullname,
        "membership_dues": duesInput // "20.00"
    })
    .then(
        function(response) {
            btn.remove();
            document.getElementById("btnLand").innerHTML = "<b>REMINDED</b>";
            $("#btnSend").css("display","block");
        },
        function(error) {
            console.log("sendMail FAILED", error);
            btn.appendChild(btnText);
            $("#btnSend").css("display","none");
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
    var txt = document.getElementById("btnLand").innerHTML;
    var patRemind = new RegExp(/reminded/i);
    if ( patRemind.text(txt) ) {

    } else {

    }
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
            console.log("sendNews SUCCESS", response.status, response.text);
        },
        function(error) {
            console.log("sendNews FAILED", error);
        }
    );
    return false;  // To block from loading a new page
}