"""
Imported libraries supporting the application
"""
import gspread # To open and edit vinyl collection spreadsheet
from google.oauth2.service_account import Credentials
from tabulate import tabulate # To pretty-print tabular data in the command-line application
import sys # To provide a programme exit for the user
import re  # To support name and album validation
import os # To support clearing the terminal for improved UX 
from os import system, name
import time # To create delays before certain functionalities

# define the scope
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# add credentials to account 
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# authorise the sheet 
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# get the instance of the sheet
SHEET = GSPREAD_CLIENT.open('vinyl_collection')


def pad_to_centre(l, w):
    """
    Manual centering of ASCI art logo
    """
    padding = ' '*(w//2)
    parts = [padding[0: (w-len(p))//2+1]+p for p in l]
    return '\n'.join(parts)

def logo():
    """
    Prints ASCI art logo
    """
    logo = '''\n\n
██████╗░██╗░██████╗░░██████╗░
██╔══██╗██║██╔════╝░██╔════╝░
██║░░██║██║██║░░██╗░██║░░██╗░
██║░░██║██║██║░░╚██╗██║░░╚██╗
██████╔╝██║╚██████╔╝╚██████╔╝
╚═════╝░╚═╝░╚═════╝░░╚═════╝░\n\n'''
    print(pad_to_centre(logo.splitlines(),80))

def welcome():
    """
    Prints welcome message
    """
    logo()
    print('Welcome to DIGG, your vinyl collection management system.'.center(80))
    input('Press enter to go to the main menu'.center(80))
welcome()

def wipe():
    """
    Wipes the terminal between certain user interections to improve UX
    This code is from a Geeks for Geeks tutorial: https://www.geeksforgeeks.org/clear-screen-python/
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def get_row():
    """
    Provides a question to the user asking:
    What is the row number of the vinyl you would like to delete?
        Params:
            While loop requests user to input a number from a range of existing row numbers
            If not valid, user is given error message and asked to try again
            Else selected row is printed back to user and while loop breaks
        Returns:
            row: used within edit_collection()
    """
    sheet_instance = SHEET.get_worksheet(0)
    records_data = sheet_instance.get_all_records()
    rowIDs = list(range(2, len(records_data) + 2))

    while True:
        row = input('What is the row number of the vinyl you would like to delete? ').strip()
        if not row.isdigit() or not int(row) in rowIDs:
            print("\nInvalid, please enter a listed row number")
            continue
        else:
            print(f"The vinyl you would like to delete is number {row}\n")
            break
    return row   

def edit_collection():
    """
    Prints the only worksheet in the external google sheet.
    Matches index numbers for each row in the tabulated table with that of the index numbers in the external spreadsheet.
    Provides a question asking user to confirm their row selection
        Params:
            While loop requests user to input y or n
            If y is chosen, while loop breaks and row is deleted. Confirmation message prints.
            If n is chosen, user is told to start again and loop runs again
            Else requests the user tries again
    """
    print('\nYour Vinyl Collection:')
    
    sheet_instance = SHEET.get_worksheet(0)
    records_data = sheet_instance.get_all_records()
    rowIDs = list(range(2, len(records_data) + 2))
    print(tabulate(
        records_data, headers='keys', showindex=rowIDs, tablefmt='rounded_grid'))
    row = get_row()

    while True:
        user_confirm = input("Is this correct? y/n ").strip().lower()
        if user_confirm == "y":
            sheet_instance.delete_rows(int(row))
            break
        elif user_confirm == "n":
            print("\nOkay, let's start again")
            time.sleep(2)
            edit_collection()
        else:
            print("Invalid choice, please enter either y or n\n")

    print("\nYour vinyl collection has been successfully updated.")
    input('\nPress enter to go back to main menu.')
    main()
    
def update_vinyl_worksheet(data):
    """
    Inserts new vinyl data from user to external spreadsheet
    This user data is collated in add_to_collection()
    Printed message lets user know addition is successful
    """
    vinyl_worksheet = SHEET.worksheet("vinyls")
    vinyl_worksheet.append_row(data)
    print("\nYour vinyl collection has been successfully updated.")
    input('\nPress enter to go back to main menu.')
    main()

def get_artist():
    """
    Provides a question to the user asking:
    Enter the artist name:
    Prints artist name back to user
        Returns:
        artist: used within add_to_collection
    """
    artist = input('Enter the artist name: ').strip()
    print(f"The artist name is {artist}\n")
    return artist

def get_album():
    """
    Provides a question to the user asking:
    Enter the album title:
    Prints album title back to user
        Returns:
        album: used within add_to_collection
    """
    album = input('Enter the album title: ').strip()
    print(f"The album title is {album}\n")
    return album

def get_year():
    """
    Provides a question to the user asking:
    What year was the album released (format YYYY)?
        Params:
            While loop validates if numbers are inputted using re
            If exclusively numbers are not used, while loop breaks and user is asked to try again
            If exclusively numbers are used, then it is checked if the string. length is 4. 
            If not valid, user is asked to try again. If valid, year is printed back to user.
        Returns:
            year: used within add_to_collection
    """
    while True:
        year = input('What year was the album released (format YYYY)? ').strip()
        if not re.match('^[0-9]+$', year): 
            print("\nInvalid year, please only enter numbers")
            continue
        elif len(year) != 4:
            print("\nInvalid answer, please use format YYYY\n")
            continue
        else:
            print(f"The album was released in {year}\n")
        return year

def add_to_collection():
    """ 
    Provides steps for the user to follow to add a new vinyl to the management system
    Global functions are called in a logical order
    These functions return values that are compiled into a list and printed back to the user
    While loop is used to ask the user to confirm the details are correct:
        If user confirms yes, update_vinyl_worksheet() is called and external worksheet is updated
        If user inputs no, add_to_collection() starts again
        If user does not enter y or n, error appears and they are asked to try again
    """
    print("About the latest addition to your collection:\n")
    artist = get_artist()
    album = get_album()
    year = get_year()
    
    # List collate the returned values from functions to confirm new vinyl entry
    new_addition = [
        artist,
        album,
        year
        ]
    
    # Confirm entry is correct with user 
    print(f"The latest addition to your vinyl collection is {album} ({year}) by {artist}")
    # While loop to either confirm entry or restart
    # If input is not valid, error message will user to try again
    
    while True:
        user_confirm = input("Is this correct? y/n ").strip().lower()
        if user_confirm == "y":
            update_vinyl_worksheet(new_addition)
            break
        elif user_confirm == "n":
            wipe()
            print("\nOkay, let's start again")
            time.sleep(1)
            add_to_collection()
        else:
            print("Invalid choice, please enter either y or n\n")

def display_collection():
    """
    Displays all sheet data from google doc using tabulate
    """
    print('\nYour Vinyl Collection:')
    sheet_instance = SHEET.get_worksheet(0)
    records_data = sheet_instance.get_all_records()
    print(tabulate(
        records_data, headers='keys', tablefmt='rounded_grid'))

    input('\nPress enter to go back to main menu.')
    main()

def main():
    """
    Provides a Main Menu with 4 choices.
    Params:
        Requests user to input a number between 1-4
        If statements execute a functions dependent on input
        1: add_to_collection()
        2: display_collection()
        3: edit_collection()
        3: exits system using sys.exit()
        Else requests the user tries again
    """
    wipe()
    print("\n\n\n\n\n")
    print('Menu\n'.center(80))
    print('1. Add a new vinyl to the collection'.center(80))
    print('2. Display full collection'.center(80))
    print('3. Edit collection'.center(80))
    print('4. Exit'.center(80))

    option = input(
    '\n\nEnter a number from 1-4 to navigate through the menu: ').strip()

    if option == "4":
        wipe()
        logo()
        print('You have now exited the programme.'.center(80))
        print('To restart the programme, press the restart button.'.center(80))
        sys.exit(0)

    if option == "1":
        wipe()
        add_to_collection()
    elif option == "2":
        wipe()
        display_collection()
    elif option == "3":
        wipe()
        edit_collection()
    else:
        print('Invalid option, please enter a number from 1-4.')
        time.sleep(2)
    main()

if __name__ == '__main__':
    # Execute main Python function
    main()