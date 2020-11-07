# Testing MSP3_club_membership

Separate testing documentations, linked to [README](../README.md)

## Initial Lighthouse Report

[Lighthouse report 1](../testing/lighthouse_20201104_1413.html)

- Adjusted the label font weight within css to fix:
    "Background and foreground colors do not have a sufficient contrast ratio."
    Introduced class ```inputlabel```.
- Added missing ```<alt>``` attributes to images.    
- ' Form elements do not have associated labels ' was fixed.
- A link from an image did 'not have a discernible name', amended to redirect to membership page.

## Navigation bar getting 'busy'.

In attempting to add menu options following CRUD processes for administrators, the navigation bars for both small and large viewports were getting congested.
A redesign of the navigation bar with further drop-down options is called for.

- [Large viewport navigation](../testing/screenshots/navbar_user_busy_1.jpg)

- [Small viewport navigation](../testing/screenshots/navbar_user_busy_2.jpg)



