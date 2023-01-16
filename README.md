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
     