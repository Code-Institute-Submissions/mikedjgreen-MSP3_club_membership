- [MSP3_club_membership](#msp3-club-membership)
  * [UX](#ux)
    + [User Stories](#user-stories)
    + [Strategy](#strategy)
    + [Scope](#scope)
    + [Structure](#structure)
    + [Skeleton](#skeleton)
    + [Surface](#surface)
  * [Features](#features)
    + [Existing Features](#existing-features)
    + [Features Left to Implement](#features-left-to-implement)
  * [Technologies Used](#technologies-used)
  * [Testing](#testing)
  * [Deployment](#deployment)
    + [Cloning repository using command line](#cloning-repository-using-command-line)
    + [Preparation of configuration files.](#preparation-of-configuration-files)
    + [Creating an env.py file](#creating-an-envpy-file)
    + [Creating file .gitignore](#creating-file-gitignore)
    + [Deployment to Heroku.](#deployment-to-heroku)
    + [Heroku application to run](#heroku-application-to-run)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
    + [Acknowledgements](#acknowledgements)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


# MSP3_club_membership

A project designed to capture and collect membership details for an art club.
This will enable the art club to stay in touch with its members and organise activities that the members will be interested in.
It is hoped to be a help with the annual summer exhibition of member's works, providing a listing of each year's contributions.
A volunteer roster for the exhibition would be easier to set up.
Evening and weekend activities set up by the members, for the members, at other times of the year would be recorded.
Club administrators will be able to keep up-to-date contact details, creating, updating and deleting lapsed memberships.

## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

### User Stories
- As an art enthusiast I would like to join like-minded people in my local community.
- As a member I would like to submit my work for the annual summer exhibition.
- As a member I would like to flag my interest in a forthcoming event.
- As a club administrator I would like to be able to contact paid members to inform of new activities and developments within the club.
- As a club administrator I would like to remind members of forthcoming club dues and subscriptions.

### Strategy

Provide the initial membership request form. 
From the request form the administrative processes emerge of reporting, updating and, if need be, deleting art club members.
Administrators also need the ability to enter membership details if the requestor does not have access to the web site.

### Scope

Following administrative Create, Read, Update and Delete (CRUD) procedures. 
* Storing membership details with limited access. 
* Associate the members with details, including stored images, of their work.


### Structure

* The interaction design is to have a navigation bar for each page, with a header showing the identity of the art club, and a footer with links to social media and other sites of interest.
    - For accessibility the navigation will change to a sidebar for mobile viewports.
* The information architecture is one of tables of data holding member details, another holding artwork details, another holding exhibition and another activity details.

### Skeleton

* Public link to wireframes used as mockups : [Balsamiq](https://balsamiq.cloud/)
* [Wireframes in PDF](static/docs/club_administration.pdf) are provided covering a number of different sized viewports.

### Surface

* The backround colour will be the muted pale blue of #D9E6F3.
* The font chosen will be Roboto.


## Features

The project concerns club membership, club activities, exhibitions and a record of artists works.
 
### Existing Features
- Subscriptions - allows a logged-in user to gain a list of members whose subscriptions are due.
              This list excludes those marked in the database collection 'members' as paid or the members are guests (no subscription).
- Subscriptions - allows administrator to send email reminders to members when subscriptions are due.

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- A volunteer rosta for running the annual exhibition.

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JavaScript](https://www.javascript.com/)
    - For dynamic, front-end interaction on HTML forms.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation and initialise MaterializeCSS components.

- [EmailJS API](https://www.emailjs.com/)
    - Third party email service to help club administrators remind members when their subscriptions are due.    

- [Python 3](https://www.python.org/about/)    
    - Programming language used to interact with a MongoDB database
    - Password security via [werkzeug WSGI library](https://werkzeug.palletsprojects.com/en/1.0.x/utils/#module-werkzeug.security)
    - [PyMongo library](https://pymongo.readthedocs.io/en/stable/index.html) used to link Python with MongoDB Atlas.
    - [Docstring PEP 257](https://www.python.org/dev/peps/pep-0257/) documentation convention followed.

- [Flask Framework](https://flask.palletsprojects.com/en/1.1.x/)
    - A python framework that uses **[JINJA](https://www.fullstackpython.com/jinja2.html)** template engine.

- [Materialize Framework](https://materializecss.com/)
    - A front-end, responsive design framework with a unified 'look and feel'.
    - Using a [date picker](https://materializecss.com/pickers.html)
    - Using a [carousel](https://materializecss.com/carousel.html) for a gallery of art works.

- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
    -  Global cloud database service.

- [TOC for markdown](https://ecotrust-canada.github.io/markdown-toc/) to generate table of contents for README     

## Testing

For the sake of brevity, the testing documentation has been separated and linked to a [TESTING document](testing/TESTING.md).

### HTML Validated
[W3.org Validator](https://validator.w3.org/nu/?doc=https://mikedjgreen.github.io/MSP3_club_membership/templates/base.html).

### CSS Validated
[W3C Validator](https://jigsaw.w3.org/css-validator/validator?uri=https://github.com/mikedjgreen/MSP3_club_membership/tree/master/static/css/stylesheet.css).

### JavaScript tidied
Passed code through [JSHint](https://jshint.com/about/)

## Deployment

Developed on GitPod using git and GitHub.
Gitpod repository has already been created, MSP3_club_membership, master git branch.

### Cloning repository using command line
Following the process documented in [cloning a repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository ).

To run this code on your local machine, you would go to my repository at [My Repo](https://github.com/mikedjgreen/MSP3_club_membership) on GitHub :
``` https://github.com/mikedjgreen/MSP3_club_membership ```

On the home page on the right hand side just above all the files, you will see a button that says, "Code".
![CloneCode](/static/docs/screenshots/clone_inst_1.jpg)

This button will give you options to clone with HTTPS, SSH, GitHub CLI, open in desktop or download as a zip file.
I initially selected GitHub CLI.
![GitHub CLI](/static/docs/screenshots/clone_inst_2_cli.jpg)

I had downloaded GitHub CLI to the default : C:\Program Files\GitHub CLI\ on my Windows terminal, from [Download CLI](https://cli.github.com/).
You will need Windows 64bit to use the software, I had a 32bit laptop...

I have selected HTTPS instead.
![GitHup HTTPS](/static/docs/screenshots/clone_inst_2_https.jpg)

To continue with cloning, you would:
- Open Git Bash (GitPod's 'Terminal')
- Change the current working directory to the location where you want the cloned directory to be made. (e.g. /workspace/clone_test )
- Type git clone, and then paste the url copied from above, either GitHub CLI or HTTPS.
 ```git clone https://github.com/mikedjgreen/MSP3_club_membership.git```
Press Enter. Your local clone will be created.

![Test Clone](/static/docs/screenshots/clone_inst_3_bash.jpg)



### Preparation of configuration files.

- requirements.txt created within the gitpod terminal :``` $ pip3 freeze --local > requirements.txt ```
- Procfile (case-specific) created within the gitpod terminal:``` $ echo web: python club_admin.py > Procfile ```

Push these files to repository, as they will be picked up by the Heroku application below.

### Creating an env.py file

Environment variables needed by the server application need to be recorded.

```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "***************")
os.environ.setdefault("MONGO_URI", "mongodb+srv://<username>:*************@msp3cluster.pihdu.mongodb.net/msp3DB?retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "msp3DB") 
```

### Creating file .gitignore

The file above contains sensitive keys and passwords, so need to be ignored by GitHub's push.

```
core.Microsoft*
core.mongo*
core.python*
env.py
__pycache__/
*.py[cod]
```

### Deployment to Heroku.

Register a Heroku account.

Create new app ('msp3-club-membership') with an appropriately close region (Europe).

![msp3-club-membership](/static/docs/screenshots/Heroku_App.jpg)

From Heroku's deploy tab the GitHub deployment method was selected.

The github connection searched for mikedjgreen's repository 'MSP3_club_membership'.

From Heroku's settings tab, select 'Reveal Config Vars'.
Add the key:value pairs with the same settings as the 'env.py' file above. (No quotes).

- IP, 0.0.0.0
- PORT, 5000
- SECRET_KEY, <whatever>
- MONGO_URI, mongodb+srv://<username>:*************...
- MONGO_DBNAME, msp3DB

Back to Heroku's deploy tab to ensure that Heroku's app picks up the GitHub's latest repository.

![Enable Automatic Deploys](/static/docs/screenshots/Heroku_Auto_Deploy.jpg)



### Heroku application to run

[club membership app](https://msp3-club-membership.herokuapp.com/)


## Credits

### Content
- The text, for better or worse, is my own.

### Media
- The photos used in this site were obtained from my own work.

### Acknowledgements

- I received inspiration for this project from [Ely Art Society](https://www.elyartsociety.com/).
- The coding instruction was gratefully received from [Code Institute](https://codeinstitute.net/)
- Further help was found with [w3schools](https://www.w3schools.com/default.asp)
- More advanced MongoDB queries were garnered from [MongoDB University](https://university.mongodb.com/courses/M001/about)
