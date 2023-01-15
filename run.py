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


def padToCenter(l:list,w:int)->str:
    """Manual centering"""
    padding = ' '*(w//2)
    parts = [padding[0: (w-len(p))//2+1]+p for p in l]
    return '\n'.join(parts)


def welcome():
    """
    Prints welcome message
    """
    logo = '''\n\n
██████╗░██╗░██████╗░░██████╗░
██╔══██╗██║██╔════╝░██╔════╝░
██║░░██║██║██║░░██╗░██║░░██╗░
██║░░██║██║██║░░╚██╗██║░░╚██╗
██████╔╝██║╚██████╔╝╚██████╔╝
╚═════╝░╚═╝░╚═════╝░░╚═════╝░\n\n'''
    print(padToCenter(logo.splitlines(),80))
    print('Welcome to DIGG, your vinyl collection management system.'.center(80))
    input('Press enter to go to the main menu: '.center(80))


welcome()


def wipe():
    """
    Wipes the terminal between certain user interections to improve UX.
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def get_row():
    while True:
        row = input('Which vinyl would you like to delete? ').strip()
        if not int(row):
            print("\nInvalid, please enter a number")
            continue
        else:
            print(f"The vinyl you would like to delete is number {row}\n")
            break
    return row   

def edit_collection():
    """
    Deletes row from external spreadsheet on users command
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
            edit_collection()
        else:
            print("Invalid choice, please enter either y or n\n")

    print("\nYour vinyl collection has been successfully updated.")
    input('\nPress enter to go back to main menu: ')
    main()
    
def update_vinyl_worksheet(data):
    """
    Inserts new vinyl data from user to external spreadsheet
    """
    vinyl_worksheet = SHEET.worksheet("vinyls")
    vinyl_worksheet.append_row(data)
    print("\nYour vinyl collection has been successfully updated.")
    input('\nPress enter to go back to main menu: ')
    main()

def get_artist():
    while True:
        artist = input('Enter the artist name: ').strip()
        if re.match(r"[\s\S\?]", artist):
            print(f"The artist name is {artist}\n")
        else:
            print("Invalid name\n")
            continue
        return artist

def get_album():
    while True:
        album = input('Enter the album title: ').strip()
        if re.match(r"[\s\S\?]", album):
            print(f"The album title is {album}\n")
        else:
            print("Invalid album title\n")
            continue
        return album

def get_year():
    while True:
        year = input('What year was the album released (format YYYY)? ').strip()
        if not int(year):
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
    Gets data on new vinyl entry from user
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
            print("\nOkay, let's start again")
            add_to_collection()
        else:
            print("Invalid choice, please enter either y or n\n")

def display_collection():
    """
    Displays all sheet data from google doc
    """
    print('\nYour Vinyl Collection:')
    sheet_instance = SHEET.get_worksheet(0)
    records_data = sheet_instance.get_all_records()
    print(tabulate(
        records_data, headers='keys', tablefmt='rounded_grid'))

    input('\nPress enter to go back to main menu: ')
    main()

def main():
    def menu():
        """
        Print menu options
        """
        wipe()
        print("\n\n\n\n\n")
        print('Menu\n'.center(80))
        print('1. Add a new vinyl to the collection'.center(80))
        print('2. Display full collection'.center(80))
        print('3. Edit collection'.center(80))
        print('4. Exit'.center(80))

        option = input(
        '\n\nEnter a number from 1-4 to navigate through the menu: '.center(80)).strip()

        if option == "4":
            wipe()
            logo = '''\n\n\n\n
██████╗░██╗░██████╗░░██████╗░
██╔══██╗██║██╔════╝░██╔════╝░
██║░░██║██║██║░░██╗░██║░░██╗░
██║░░██║██║██║░░╚██╗██║░░╚██╗
██████╔╝██║╚██████╔╝╚██████╔╝
╚═════╝░╚═╝░╚═════╝░░╚═════╝░\n\n'''
            print(padToCenter(logo.splitlines(),80))
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
            print('Invalid option.')
            menu()
    menu()

if __name__ == '__main__':
    main()