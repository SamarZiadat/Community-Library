<h1  align="center">Digg: A Vinyl Collection Management System</h1>

View the live project [here](https://digg.herokuapp.com/).

Digg is a command line interface styled application that allows users to manage their home vinyl record collections. The app functions as a management system that allows users to easily access an overview of their collection and edit it, without having to manually dig through their home vinyl collection. Vinyl collections, especially if large, can be a challenge to manually search through (unlike books, CDs, or cassettes, for example, which have spines). The act of looking through ones vinyl collection, or searching through crates of vinyl in a record store, is known as ['digging' or 'crate digging'](https://en.wiktionary.org/wiki/cratedigger) in the vinyl-collecting community - hence the name 'Digg'. 

## Table of Contents

-   [User Experience (UX)](#)
-   [Features](#)
-   [Technologies Used](#)
-   [Testing](#)
-   [Deployment](#)
-   [Credits](#)

## User experience (UX)
  **User Stories**
I want to...
 1. easily understand the main purpose of the app 
 2. be able to easily navigate through the app 
 3. add my vinyl collection to the management system
 4. view my full collection in a table format 
 5. remove vinyls from the management system

### Design Prototype

The main objective of this project is to demonstrate competency in Python, however, adherence to high presentation standards is also key. With the application being a command line interface, choices in design were limited, but carefully planned and delivered. The very first design prototype was created using [Balsamiq](https://balsamiq.com/). 

![Wireframe](https://github.com/SamarZiadat/Vinyl-Collection-Management-System/blob/main/documentation/supporting-images/wireframe.png?raw=true)
### Site Structure
Digg is a one-page website that has a command line interface in the centre. When the application stars the user is welcomed by a stylised terminal page that includes the name of the app, one line to describe the purpose of the app, and instructions on how to proceed. Keeping user experience in mind throughout, the user is given the opportunity to return to the menu at key stages. The application also features a static 'RESTART PROGRAMME' button which the user can press to restart the application at any time. 

### Python Logic

I created a flowchart to detail the logic flow of the application before I began coding. This was an essential tool that provided a detailed outline of how the user will navigate the application. The flowchart was created using [Lucidchart](https://www.lucidchart.com/).
![Flowchart](https://github.com/SamarZiadat/Vinyl-Collection-Management-System/blob/main/documentation/supporting-images/flowchart.jpeg?raw=true)
## Data Model
[Google Sheets](https://www.google.co.uk/sheets/about/)  was used to store the application data. This acted as a database where data would be sent to and also retrieved from. The Google Sheet that I created can be accessed [here](%5BGoogle%20Sheet%5D%28https://docs.google.com/spreadsheets/d/1VfUBCKy-KVL_C9G4xRcqCyoZqnXmzN99nohblpJxSrE/edit?usp=sharing%29). ![Google sheet](https://github.com/SamarZiadat/Vinyl-Collection-Management-System/blob/main/documentation/supporting-images/google-sheet.png?raw=true)
### Design Choices
-   #### Typography
    
     ASCII art was used to create a logo that present on the start-up and exit display on the command line. It was a simple way to add interest to a paired back interface. [This](https://fsymbols.com/generators/carty/) text to ASCII art generator was used to produce the logo used.

-   #### Imagery
    
     The background image is the only image used in the application, and it is a free stock image sourced from [Pexels](https://www.pexels.com/). 

## Technologies Used
-   [HTML5](https://en.wikipedia.org/wiki/HTML)  - Provides the content and structure for the website.
-   [CSS3](https://en.wikipedia.org/wiki/CSS)  - Provides the styling for the website.
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))  - Provides the functionality of the website.
-   [Favicon](https://favicon.io/)  - Used to create the favicon.
-   [Compressor](https://compressor.io/)  - Used to compress the images.
-   [VSCode](https://code.visualstudio.com/)  - Used to create and edit the website.
-   [GitHub](https://github.com/)  - Used to host and deploy the website.
-   [GitBash](https://en.wikipedia.org/wiki/Bash_(Unix_shell))  - Terminal used to push changes to the GitHub repository.
-   [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/)  - Used to test responsiveness and debug.
-   [Balsamiq](https://balsamiq.com/)  - Used to create the wire-frame.
-   [Lucidchart](https://www.lucidchart.com/)  - Used to create the logic flow chart.
-   [Google Sheets](https://www.google.co.uk/sheets/about/)  - Used to host the application data.
- [Tech Sini](https://techsini.com/multi-mockup/) - Used to generate the mockup of the app.
- [Fsymbols](https://fsymbols.com/generators/carty/) - Used to generate ASCII art.
- [Pexels](https://www.pexels.com/) - Used to source free stock image for background.
## Python Packages

-   [GSpread](https://pypi.org/project/gspread/)  - Used to transfer data between google sheets.
-   [Colorama](https://pypi.org/project/colorama/)  - Used to add colours to the terminal.
-   [OS](https://docs.python.org/3/library/os.html)  - Used to provide a way of using operating system dependent functionality.
-   [Time](https://docs.python.org/3/library/time.html)  - Used to provide various time-related functions.
-   [Sys](https://docs.python.org/3/library/sys.html)  - Used to provide access to some variables used or maintained by the interpreter.
-   [Tabulate](https://pypi.org/project/tabulate/)  - Used to print data in a nice table format.
- [Re - Regular expression operations](https://docs.python.org/3/library/re.html#) - Used to validate user input.

### Browser Compatibility

-   Testing has been carried out on the following browsers :
    -   Chrome Version 107.0.5304.87
    -   Edge Version 107.0.1418.24
    -   Firefox Version 94.0.1
    -   Safari on macOS (Safari Version 15.6)

# Deployment To Heroku

The project was deployed to  [Heroku](https://www.heroku.com/). The deployment process is as follows:

1.  Log in to Heroku or create an account if required.

2.  Click the button labeled New from the dashboard in the top right corner, just below the header and then select "Create new app".

3.  Enter a unique application name and then select your region. Once you are ready, click "Create app".

4.  This will bring you to the project "Deploy" tab. From here, click the "Settings" tab and scroll down to the "Config Vars" section and click on "Reveal Config Vars". In the KEY input field, enter "PORT" and in the VALUE input field, enter "8000". After that, click the "Add" button to the right.

5.  Scroll down to the buildpacks section of the settings page and click the button "Add buildpack". 

6.  Add both "Python" and "node.js" and make sure that Python is above node.js. If it isn't you can just drag it above.

7.  Scroll back to the top of the settings page, and navigate to the "Deploy" tab. Select Github as the deployment method.

8.  Search for the repository name and click the connect button next to the intended repository.

9.  From the bottom of the deploy page select your preferred deployment type. I personally enabled automatic deployments. After that, click "Deploy Branch".


     