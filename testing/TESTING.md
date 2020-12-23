- [Testing MSP3_club_membership.](#testing-msp3-club-membership)
  * [Initial Lighthouse Report.](#initial-lighthouse-report)
  * [Navigation bar getting 'busy'.](#navigation-bar-getting--busy-)
  * [Membership form validation.](#membership-form-validation)
  * [Adding artworks into Gallery collection.](#adding-artworks-into-gallery-collection)
    + [Findings of initial artwork entry test](#findings-of-initial-artwork-entry-test)
  * [Implementation of EmailJS API](#implementation-of-emailjs-api)
    + [Findings of initial EmailJS implementation](#findings-of-initial-emailjs-implementation)
    + [EmailJS fixes](#emailjs-fixes)
  * [Recording interest in club activites.](#recording-interest-in-club-activites)
    + [Findings of intiial activity interest flag.](#findings-of-intiial-activity-interest-flag)
  * [PEP8 compliant python code](#pep8-compliant-python-code)
  * [Second EmailJS for Activities News.](#second-emailjs-for-activities-news)
    + [Findings of initial EmailJS News implementation.](#findings-of-initial-emailjs-news-implementation)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Testing MSP3_club_membership.

Separate testing documentation, linked to [README](../README.md)

## Initial Lighthouse Report.

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

- ![Large viewport navigation](../testing/screenshots/navbar_user_busy_1.jpg)

- ![Small viewport navigation](../testing/screenshots/navbar_user_busy_2.jpg)


## Membership form validation.

Currently the membership entry form validates at the server side only. So any invalid entries are only caught once a submission is attempted.
Also only the initial input error is indicated, not many.

- ![First input error](../testing/screenshots/membership_validation_serverside_1.jpg) only error indicated on selecting Submit button.
- ![Second input error](../testing/screenshots/membership_validation_serverside_2.jpg) only shown once first input error has been amended and submitted.
- ![Third input error](../testing/screenshots/membership_validation_serverside_3.jpg) again only shown once previous errors amended and submitted.

## Adding artworks into Gallery collection.

Initially tested [MaterializeCSS Carousel](https://materializecss.com/carousel.html) of artwork images and details within the Gallery page and collection.
It is designed as an image slider and is touch compatible. The initial test had no direction buttons.
Mouse slide:
- ![Art works carousel](../testing/screenshots/Artworks_carousel_1.jpg)
- ![Art works carousel](../testing/screenshots/Artworks_carousel_2.jpg)
- ![Art works carousel](../testing/screenshots/Artworks_carousel_3.jpg)

Added initial artworks as an array into the Gallery documents, by using a [python script](../testing/artworks_insert.py). 
To work properly the script will have to be moved back to the IDE's root directory, rather than the testing subdirectory.

Added an artwork entry to an artworks array within a gallery document.

- ![Initial Modal form](../testing/screenshots/Add_artwork_1.jpg)
- ![Art work details filled](../testing/screenshots/Add_artwork_2.jpg)
- ![Successfully added](../testing/screenshots/Add_artwork_3.jpg)  viewed at 50% zoom.
- ![Gallery view](../testing/screenshots/Add_artwork_4.jpg) viewed at 50% zoom.
- ![Database view](../testing/screenshots/Add_artwork_5.jpg)

### Findings of initial artwork entry test
Although the entry form displayed well, it is too narrow for the image file entry.
On a normal monitor screen at 100% zoom, the screen estate is not used well, and depends upon vertical scrolling.
- ![Screen Estate issues](../testing/screenshots/Add_artwork_6.jpg)

This becomes more pronounced on the smallest viewports...
- ![Small viewport](../testing/screenshots/Add_artwork_7.jpg)

The art work was successfully added, as the flash message advises, but the user was not returned to  the gallery page.
The art work form can be closed without entry, but does not seem to take advantage of MaterializeCSS's documented process.

## Implementation of EmailJS API 
The emailJS implementation is in response to the user story: 'As a club administrator I would like to remind members of forthcoming club dues and subscriptions.
'. Simple process testing of the EmailJS showed some procedural and functional shortcomings.
The initial implementation attempted to use a personal gmail account. 
The API key was hardcoded into the javascript file, again not ideal.

The button to initiate email reminders appears on the membership page.
One problem is that this would appear to remind all members of their subscription renewals, whether they have paid, or not.
- ![Initial EmailJS appearance](../testing/screenshots/EmailJS_1.jpg)
The same email reminder button is also placed against each member entry.
- ![Each member entry](../testing/screenshots/EmailJS_2.jpg)
The  form that is opened by the button (against a paid member) contains the correct information, but is not labeled as such.
Also the email account used to send the email is a private email account.
- ![EmailJS form](../testing/screenshots/EmailJS_3.jpg)
Closing the reminder form returns the administrator to the members page correctly.

Selecting 'Membership Dues' button takes the administrator to the membership dues list where the reminder emails are to be used.
- ![Members due renewal](../testing/screenshots/EmailJS_4.jpg)

Selecting 'Send Reminders' now displays a member's details accurately, although the labels are still needed:
- ![Member due renewal form](../testing/screenshots/EmailJS_5.jpg)

For further testing of the email, the selected member's email account has been amended to one accessible for the test.
- ![Member received email](../testing/screenshots/EmailJS_6.jpg)

This compares with the club's EmailJS template for members renewals.
- ![EmailJS template](../testing/screenshots/EmailJS_7.jpg)

Unfortunately when another renewal member's email reminder is selected:
- ![Another member due renewal](../testing/screenshots/EmailJS_8.jpg)
..the first member on the due list is still selected..
- ![Not Gale](../testing/screenshots/EmailJS_9.jpg)

This leads to two failures, 
1. the inability to select members to remind by email.
2. once email sent, no flag set to stop duplicating email.

### Findings of initial EmailJS implementation
1. EmailJS email service, although still a 'personal service', should be connected to a more club oriented email account.
2. The API key subsequently received should be recorded privately, if possible.
3. The Email Reminder should only be accessed against the membership dues list.
4. The reminder should pick up the member's detail(s) in the context it was called.
5. The reminder form should be labeled.
6. The reminder sent successfully, a flag should be set indicating that the member has been emailed with a reminder.

### EmailJS fixes
1. The service is connected to a more club oriented account: ![Club email account](../testing/screenshots/EmailJS_10_fix.jpg).
4. The reminder should pick up the member in focus: ![Gale due](../testing/screenshots/EmailJS_12_fix1.jpg)
            ...which leads to:    ![Gale reminder](../testing/screenshots/EmailJS_12_fix2.jpg)
5. The reminder form has been reconfigured:  ![Reminder form](../testing/screenshots/EmailJS_11_fix.jpg).

## Recording interest in club activites.
Testing the ability to flag a member's interest in an upcoming club activity.

The activities page contains a button to help a viewer indicate their interest in an event.
- ![Activities Page flag interest](../testing/screenshots/Flag_interest_1.jpg)
The viewer is presented with a flag interest form.
- ![Flag Interest form](../testing/screenshots/Flag_interest_2.jpg)
The viewer elects to indicate interest.
- ![Returns message](../testing/screenshots/Flag_interest_3.jpg)
The collection activities' document for the selected activity has had an interest recorded.
- ![Activity document](../testing/screenshots/Flag_interest_4.jpg) 
The next interest shown in the activities overwrites the previous interest.
- ![Activity interest overwritten](../testing/screenshots/Flag_interest_5.jpg)

### Findings of intiial activity interest flag.
1. The form needs further styling.
2. The radio buttons do not record boolean values for membership.
3. A non-member's email entry is not recorded.
4. Once interest recorded, the user should be returned to the activities page.
5. The database entry should be organised in an array of interested parties.
6. The latest interest should not overwrite earlier interest in the activity.

## PEP8 compliant python code
[PEP8 report](../testing/pep8_check_20201223.txt)

## Second EmailJS for Activities News.
A user story has led to the need for a second EmailJS API implementation.
"As a club administrator I would like to be able to contact paid members to inform of new activities and developments within the club."
A personal email account was eschewed in favour of a generic club account name.
A button appears for a logged in administrative user for each activity.
- ![Email news](../testing/screenshots/EmailJS_news_1.jpg)

 This allows the administrator to view a form to be sent to each paid member of an activities details.
 - ![Email News Form](../testing/screenshots/EmailJS_news_2.jpg)

 The email is sent to the paid-up member of a new club activity's details.
 - ![Email news post](../testing/screenshots/EmailJS_news_3.jpg)

### Findings of initial EmailJS News implementation.
1. Unlike the initial members' dues reminder, the activity news email used a generic club email account.
2. The email news option only appears for a logged-in administrator against each activity.
3. The date of the activity could appear more 'human' in both the email form and the eventual posting.
4. Although the activity has a lead member/organiser identified on the email form, the name does not appear on the posting to the member.
5. A count of the members with a qualifier of 'paid = true' matched the number of members appearing on the email news form.
6. Although the news email is actioned for a member, there is no ready indicator that the member has been sent a news email.
7. The functionality currently only allows one email to be sent to one member at a time.



