# MSP3_club_membership

A project to capture and collect membership details for an art club.
This will enable the art club to stay in touch with its members and organise activities that the members will be interested in.
It is hoped to be a help with the annual summer exhibition of member's works, providing a listing of each year's contributions.
A volunteer roster for the exhibition would be easier to set up.
Evening and weekend activities set up by the members, for the members, at other times of the year would be recorded.
Club administrators will be able to keep up-to-date contact details, creating, updating and deleting lapsed memberships.

## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

### User Stories:
- As an art enthusiast I would like to join like-minded people in my local community.
- As a member I would like to submit my work for the annual summer exhibition.
- As a member I would like to flag my interest in a forthcoming event.
- As a club administrator I would like to be able to contact paid members to inform of new activities and developments within the club.
- As a club administrator I would like to remind members of forthcoming club dues and subscriptions.

### Strategy

Provide the initial membership request form. 
From the request form the administrative processes of reporting, updating and, if need be, deleting art club members.
Administrators also need the ability to enter mebership details if the requestor does not have access to the web site.

### Scope

Following administrative CRUD procedures. Storing membership details with limited access. Associate the members with details, including stored images, of their work.


### Structure

The interaction design is to have a navigation bar for each page, with a header showing the identity of the art club, and a footer with links to social media and other sites of interest.
The information architecture is one of tables of data holding member details, another holding artwork details, another holding exhibition and activity details.

### Skeleton

A wireframe is provided.

### Surface

The backround colour will be the muted pale blue of #D9E6F3.
The font chose will be Roboto.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JavaScript](https://www.javascript.com/)
    - For dynamic, front-end interaction on HTML forms.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- [Python 3](https://www.python.org/about/)    
    - Programming language used to interact with a MongoDB database

- [Flask Framework](https://flask.palletsprojects.com/en/1.1.x/)
    - A python framework that uses JINJA template engine.

- [Materialize Framework](https://materializecss.com/)
    - A front-end, responsive design framework with a unified 'look and feel'.

- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
    -  Global cloud database service.

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from [Ely Art Society](https://www.elyartsociety.com/).
- Further help was found with [w3schools](https://www.w3schools.com/default.asp)
