/*
    jQuery for MaterializeCSS initialization
    Mobile sidebar...
    Date Picker...
*/

$(document).ready(function () {
    $(".sidenav").sidenav({edge: "left"});

    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 2,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
    
});
