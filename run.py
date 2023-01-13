"""
Imported libraries supporting the application
"""
import gspread # To open and edit vinyl collection spreadsheet
from google.oauth2.service_account import Credentials
from tabulate import tabulate # To pretty-print tabular data in the command-line application
import sys # To provide a programme exit for the user
import re  # To support name and album validation

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

def menu():
    """
    Print menu options
    """
    print('Menu\n')
    print('1. Add a new vinyl to the collection')
    print('2. Display full collection')
    print('3. Edit collection')
    print('4. Exit')

    option = input(
        '\nEnter a number from 1-4 to navigate through the menu: ').strip()

    if option == "4":
        print('You have now exited the programme.')
        sys.exit(0)

    if option == "1":
        add_to_collection()
    elif option == "2":
        display_collection()
    elif option == "3":
        edit_collection()
    else:
        print('Invalid option.')
        menu()

    menu()

def wipe():
    """
    Wipes the screen clear between certain user interections to improve UX.
    """
    print('\033c')

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
    
def update_vinyl_worksheet(data):
    """
    Inserts new vinyl data from user to external spreadsheet
    """
    vinyl_worksheet = SHEET.worksheet("vinyls")
    vinyl_worksheet.append_row(data)
    print("\nYour vinyl collection has been successfully updated.")
    input('Press enter to go back to main menu: ')
    menu()


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
    print("\nAbout the latest addition to your collection:")
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
    print(f"The newest addition to your vinyl collection is {album} ({year}) by {artist}")
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

def main():
    menu()

if __name__ == '__main__':
    main()