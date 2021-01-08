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

_[TOC](http://ecotrust-canada.github.io/markdown-toc/)_


# MSP3_club_membership

A project designed to capture and collect membership details for an art club.
This will enable the art club to stay in touch with its members and organise activities that the members will be interested in.
It is hoped to be a help with the annual summer exhibition of member's works, providing a listing of each year's contributions.
A volunteer roster for the exhibition would be easier to set up.
Evening and weekend activities set up by the members, for the members, at other times of the year would be recorded.
Club administrators will be able to keep up-to-date contact details, creating, updating and deleting lapsed memberships.

## UX
 
### User Stories
- As an art enthusiast I would like to join like-minded people in my local community.
- As a member I would like to submit my work for the annual summer exhibition.
- As a member I would like to flag my interest in a forthcoming event.
- As a club administrator I would like to be able to contact paid members to inform of new activities and developments within the club.
- As a club administrator I would like to remind members of forthcoming club dues and subscriptions.

### Strategy

A local collection of artists and art enthusiasts would like an online meeting, or focal point to share their enthusiasm.
With that in mind, provide an initial membership request form. 
From the request form the administrative processes emerge of reporting, updating and, if need be, deleting art club members.
Administrators also need the ability to enter membership details if the requestor does not have access to the web site.
- Initially upon opening the website, the browser would open with the membership form.
  _Upon review it is thought the browser should show artworks that would interest potential members._

### Scope

The minimum viable product would be the ability to record membership and show artwork in some easy to view way.
Following administrative Create, Read, Update and Delete (CRUD) procedures. 
* Storing membership details with limited access. 
* Associate the members with details, including stored images, of their work.
* Ability to display club members work.
* Facility to publicise events and activities run by club members.


### Structure

#### The interaction design 

This is to have a navigation bar for each page, with a header showing the identity of the art club, and a footer with links to social media and other sites of interest.
- For accessibility the navigation will change to a sidebar for mobile viewports.
- A coherent visual display across all pages should be presented to the browser of the site.

The membership application form's number of input fields will be kept to a minimum. 
This is to keep the applicant's experience as clear and concise as possible.
The onus then is on the administrator to 'fill in the blanks' when needed.

#### The information architecture

Will be one of collections of data holding member details, another holding artwork details, another holding exhibition and another activity details.
It was originally envisaged that there would be separate arrays of artworks associated with exhibitions and another array of artworks for a more general gallery.
This was reorganised into a collection of artworks with a Boolean indicators as to whether they were for exhibit as well as gallery.
- The original exhibition collection would contain details of the annual exhibition for that year.
- The activities collection will hold the date and time the activity will take place, an image to publicise the event, along with venue,
         duration and who will be leading the activity.
- With club administrators needing secured access to members details their login authentication details would be collected as 'users'.
- There will be a need for text indexes on collections to ease searches. [Create indexes](static/docs/indexes.md)
- Decision made to store images externally to the database, with the database holding the image location on the server.
      An example discussion of this issue [Images on database?](https://habiletechnologies.com/blog/better-saving-files-database-file-system/)

### Skeleton

* Public link to wireframes used as mockups : [Balsamiq](https://balsamiq.cloud/)
* [Wireframes in PDF](static/docs/club_administration.pdf) are provided covering a number of different sized viewports.

### Surface

* The backround colour will be the muted pale blue of #D9E6F3.
* The font chosen will be Roboto.
* The 'coherent visual display' will be provided by the MaterializeCSS framework.


## Features

The project concerns club membership, club activities, exhibitions and a record of artists works.
 
### Existing Features
- Membership application form. Both client and server side validation for 'belt-and-braces' defensive programming.
- Members list of club members details for club administrators, with search facility, if club becomes popular.
- Subscriptions - allows a logged-in user to gain a list of members whose subscriptions are due.
              This list excludes those marked in the database collection 'members' as paid or the members are guests (no subscription).
- Subscriptions - allows administrator to send email reminders to members when subscriptions are due.
- Applications - allows administrator to ascertain new applications and add information to become member.
- Flag interest in activities - displays a count against each activity of interest shown.
- Exhibition page showns images and artist names of all artworks flagged for exhibit in club's annual exhibition.
- Gallery page shows all artworks of members in a carousel, whether for exhibition, or not. 
    also shows whether an artwork has been sold.
- Search facility for members artworks, search against index of artist name or artwork title.

### Features Left to Implement
- A volunteer rosta for running the annual exhibition.
- An administrator's view of those interested in activities. To inform of cancelations, etc.
- A batch script to archive older artworks that have exhibited in previous years, have been sold, or by lapsed members.
- A cleaner, clearer procedure to ensure images arrive correctly on the server and recorded on artwork and member forms.
  Possibly utilizing an application such as [cloudinary](https://cloudinary.com/documentation).
- As the number of club activities increase, and the number of exhibition artworks increase, 
  there will be a need for limiting the intial page loads and implementation of pagination.

#### Features Testing has shown left to implement.    
- Further client-side confirmation of deletions (members, activities and artworks) for administrators.
- Date validation, especially validating against entering dates in the past.


## Technologies Used

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

- [Font Awesome](https://fontawesome.com/) 
    - to provide additional icons, especially 'facebook'.

- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
    -  Global cloud database service.

- [Online Image Compressor](http://jpeg-optimizer.com/)
    - to optimise speed of website loading on an image intensive site.    

- [TOC for markdown](https://ecotrust-canada.github.io/markdown-toc/) to generate table of contents for README     

## Testing

For the sake of brevity, the testing documentation has been separated and linked to a [TESTING document](testing/TESTING.md).

### HTML Validated
[W3.org Validator](https://validator.w3.org/nu/?doc=https://mikedjgreen.github.io/MSP3_club_membership/templates/base.html).

### CSS Validated
[W3C Validator](https://jigsaw.w3.org/css-validator/validator?uri=https://github.com/mikedjgreen/MSP3_club_membership/tree/master/static/css/stylesheet.css).

### JavaScript tidied
Passed [code](../static/js/script.js) through [JSHint](https://jshint.com/about/)
>There are 23 functions in this file.
>Function with the largest signature take 1 arguments, while the median is 0.
>Largest function has 10 statements in it, while the median is 1.
>The most complex function has a cyclomatic complexity value of 2 while the median is 1.

### PEP8 compliant python code
Passed code through [PEP8](http://pep8online.com/).
Especially for long lines [PEP8 long lines](https://www.python.org/dev/peps/pep-0008/#maximum-line-length)

#### Testing user login
To test the CRUD capabilities of the application a login is available: 
    **percival/zygote** 
    
## Deployment

Developed on GitPod using git and GitHub.
Gitpod repository has already been created, MSP3_club_membership, master git branch.

### Command line execution.
The application can be run in the workspace from python script club_admin.py :
``` python3 club_admin.py ```

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
- Thanks to mentor, Jonathan Munz, for pointing me to database image store debate article.