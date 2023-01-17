<h1  align="center">Digg: A Vinyl Collection Management System</h1>

View the live project [here](https://digg.herokuapp.com/).

Digg is a command line interface styled application that allows users to manage their home vinyl record collections. The app functions as a management system that allows users to easily access an overview of their collection and edit it, without having to manually dig through their home vinyl collection. Vinyl collections, especially if large, can be a challenge to manually search through (unlike books, CDs, or cassettes, for example, which have spines). The act of looking through ones vinyl collection, or searching through crates of vinyl in a record store, is known as ['digging' or 'crate digging'](https://en.wiktionary.org/wiki/cratedigger) in the vinyl-collecting community - hence the name 'Digg'. 

![enter image description here](https://github.com/SamarZiadat/Vinyl-Collection-Management-System/blob/main/documentation/supporting-images/mockup.png?raw=true)

## Table of Contents

-   User Experience (UX)
-   Features
-   Technology
-   Testing
-   Deployment
-   Credits

## User experience (UX)

### Design Prototype

The main objective of this project is to demonstrate competency in Python, however, adherence to high presentation standards is also key. With the application being a command line interface, choices in design were limited, but carefully planned and delivered. The very first design prototype was created using [Balsamiq](https://balsamiq.com/).

![Wireframe](https://github.com/SamarZiadat/Vinyl-Collection-Management-System/blob/main/documentation/supporting-images/wireframe.png?raw=true)
### Site Structure
Digg is a one-page website that has a command line interface in the centre. When the application stars the user is welcomed by a stylised terminal page that includes the name of the app, one line to describe the purpose of the app, and instructions on how to proceed. Keeping user experience in mind throughout, the user is given the opportunity to return to the menu at key stages. The application also features a static 'RESTART PROGRAMME' button which the user can press to restart the application at any time. 

### Python Logic

I created a flowchart to detail the logic flow of the application before I began coding. This was an essential tool that provided a detailed outline of how the user will navigate the application. The flowchart was created using [Lucidchart](https://www.lucidchart.com/).
![Flowchart](https://github.com/SamarZiadat/Vinyl-Collection-Management-System/blob/main/documentation/supporting-images/flowchart.jpeg?raw=true)
### Data Model
[Google Sheets](https://www.google.co.uk/sheets/about/)  was used to store the application data. This acted as a database where data would be sent to and also retrieved from. The Google Sheet that I created can be accessed [here](%5BGoogle%20Sheet%5D%28https://docs.google.com/spreadsheets/d/1VfUBCKy-KVL_C9G4xRcqCyoZqnXmzN99nohblpJxSrE/edit?usp=sharing%29). ![Google sheet](https://github.com/SamarZiadat/Vinyl-Collection-Management-System/blob/main/documentation/supporting-images/google-sheet.png?raw=true)
### Design Choices
 -   #### Typography
    
     ASCII art was used to create a logo that present on the start-up and exit display on the command line. It was a simple way to add interest to a paired back interface. [This](https://fsymbols.com/generators/carty/) text to ASCII art generator was used to produce the logo used.

 -   #### Imagery
    
     The background image is the only image used in the application, and it is a free stock image sourced from [Pexels](https://www.pexels.com/). 

## Features
### Existing Features
#### Startup Display
 - This is how the terminal will display when the user first loads the application 
 - ASCI art has been utilised to create a logo and to add visual interest 
 - A welcome message greets the user as well as informs them of the purpose of the application
 - The user easily proceeds to the main menu by entering the 'enter' key on their keyboard
 
![Startup display](https://github.com/SamarZiadat/Vinyl-Collection-Management-System/blob/main/documentation/supporting-images/start-up-image.png?raw=true) 

#### Menu 
 - This is the main application menu, which is displayed when the user travels from the startup display
 - The user is given 4 options to navigate through: adding a new vinyl to the management system, displaying the whole collection, editing the collection, and exiting the programme. 
 - In order to navigate through the menu the user is required to enter a number from 1 to 4 and then press the 'enter' key

![Menu display](https://github.com/SamarZiadat/Vinyl-Collection-Management-System/blob/main/documentation/supporting-images/menu-image.png?raw=true)

#### Add a new vinyl to the collection
 - If the user selects option '1' from the main application menu, this is what displays in the terminal
 - The user is walked through entering the new information for their vinyl record. Data collection includes the artist name, album name, and the album's year of release
 - Once the user has inputted their answer for these three pieces of data, the data is presented back to them and they have the choice to confirm this data as accurate, or start again in the process of data input
 - Once the data is confirmed to be correct, this information is added to the external Google Sheet. The user then has the option to return to the menu by pressing the 'enter' key 
 
![Add a new vinyl](https://github.com/SamarZiadat/Vinyl-Collection-Management-System/blob/main/documentation/supporting-images/addition-image.png?raw=true)
#### Display full collection
 - If the user selects option '2' from the main application menu, this is what displays in the terminal
 - The data collected about the vinyl collection is retrieved from the external Google Sheet and presented in a table format using tabulate
 - The user then has the option to return to the menu by pressing the 'enter' key 

![Display full collection](https://github.com/SamarZiadat/Vinyl-Collection-Management-System/blob/main/documentation/supporting-images/display-collection-image.png?raw=true)

#### Edit collection
 - If the user selects option '3' from the main application menu, this is what displays in the terminal
 - The data collected about the vinyl collection is retrieved from the external Google Sheet and presented in a table format using tabulate. 
 - The user is asked to identify which vinyl they would like to remove the management system. The vinyl is identified by the user through its row number
 - The user is given an opportunity to confirm if the vinyl they have selected is the one to be deleted. If they choose 'n', they are asked to try to pick a vinyl again. If they choose 'y', the user then has the option to return to the menu by pressing the 'enter' key 

![Edit collection](https://github.com/SamarZiadat/Vinyl-Collection-Management-System/blob/main/documentation/supporting-images/edit-image.png?raw=true)

#### Exit
- If the user selects option '4' from the main application menu, this is what displays in the terminal
- The ASCII logo is displayed, as well as message to let the user know that the programme has not been exited
- Instructions are given to the user on how to restart the programme

![Exit programme ](https://github.com/SamarZiadat/Vinyl-Collection-Management-System/blob/main/documentation/supporting-images/exit-image.png?raw=true)

### Future Features
There is a lot of room from expansion of features in this application. This includes building a user login function, as well as providing the option to edit a vinyl entry beyond deletion. This project is not required to be fully responsive, and so because of time limitations it is not fully responsive on all devices - making this a feature in the future would be crucial.

## Technology

### Technologies Used
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
### Python Packages

-   [GSpread](https://pypi.org/project/gspread/)  - Used to transfer data between google sheets.
-   [Colorama](https://pypi.org/project/colorama/)  - Used to add colours to the terminal.
-   [OS](https://docs.python.org/3/library/os.html)  - Used to provide a way of using operating system dependent functionality.
-   [Time](https://docs.python.org/3/library/time.html)  - Used to provide various time-related functions.
-   [Sys](https://docs.python.org/3/library/sys.html)  - Used to provide access to some variables used or maintained by the interpreter.
-   [Tabulate](https://pypi.org/project/tabulate/)  - Used to print data in a nice table format.
- [Re - Regular expression operations](https://docs.python.org/3/library/re.html#) - Used to validate user input.

## Testing
### Code Validation
The code has been validated by using online validation tools  [W3C HTML Validator](https://validator.w3.org/) and [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

-   W3C HTML Validator results:
![HTML validation](https://github.com/SamarZiadat/Vinyl-Collection-Management-System/blob/main/documentation/supporting-images/html-validation.png?raw=true)

- W3C CSS Validator results:
![CSS validation](https://github.com/SamarZiadat/Vinyl-Collection-Management-System/blob/main/documentation/supporting-images/css-validation.png?raw=true)

### Browser Compatibility
Testing has been carried out on the following browsers :
    -   Chrome Version 107.0.5304.87
    -   Edge Version 107.0.1418.24
    -   Firefox Version 94.0.1
    -   Safari on macOS (Safari Version 15.6)

### Manual Testing
I have conducted manual logic testing to make sure that the python code is working as intended:

 - **Startup Display**
	 - Verify that if the user enters the 'enter' key that they will navigate to the Menu.
 - **Main Menu**
	 - Verify that the user receives an invalid input message if their input doesn't pass validation 
	 - Verify that all menu options load as intended
   if the user enters the right key
 -  **Add a new vinyl to the collection**
	 -	Verify that the user receives an invalid input message if their input doesn't pass validation 
	 -	Verify that the data printed back to the user matches what they have entered
	 -	Verify that if the user enters a valid input message in response to confirming this addition that they are navigate to the right display
	 - Verify that if the user enters the 'enter' key that they will navigate to the Menu.
- **Display full collection**
	- Verify that the table presented matches that of the external spreadsheet
	- Verify that the table is tabulated as expected
	 -	Verify that if the user enters the 'enter' key that they will navigate to the Menu.
 -  **Edit collection**
	 - Verify that the table presented matches that of the external spreadsheet
	- Verify that the table is tabulated as expected, including displaying index numbers that match those of the external spreadsheet
	-Verify that the user receives an invalid input message if their input doesn't pass validation 
	- Verify that if the user enters a valid response, that the correct row is deleted 
	- Verify that if the user confirms deletion that they are receive a message to say that the spreadsheet has been updated
	- 	Verify that if the rejects confirmation for deletion that they are asked to enter a row index number again
    -	Verify that if the user enters the 'enter' key that they will navigate to the Menu.
   -   **Exit App**
		 - Verify that when the user exits the app, that they are presented with the logo, confirmation that the app has been exited, and instructions on how to restart the programme

## Deployment To Heroku

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

## Credits

### Content

- All content was written by the developer

### Code

-   Code to clear a python terminal with a call: https://www.geeksforgeeks.org/clear-screen-python/

-  Tutorial on the time.sleep() method: https://www.freecodecamp.org/news/python-sleep-time-sleep-in-python/
    
-   Documentation on __ main __: https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/

-   Stack Overflow answer on how to centre multi-line ASCII art: 
https://stackoverflow.com/questions/49745662/centering-ascii-graphics-python
    
### Media
    
- Background image was sources from Pexels: https://www.pexels.com/photo/vinyl-record-1374557/
     
### Acknowledgments

Thank you to my mentor Brian Macharia who gave me excellent advice and feedback on how to plan and execute this project and who provided me with lots of pointers and resources to help with design, coding and testing.   