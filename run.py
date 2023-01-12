import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate

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
        option1()
    elif option == "2":
        option2()
    elif option == "3":
        print('Option 3 has been called')
    else:
        print('Invalid option.')
        menu()

    menu()

def option1():
    """ 
    Gets data on new vinyl entry from user
    """
    print("\nLet's add a new vinyl to the collection")
    artist_request = (input('Enter the artist name: ').strip().capwords())
    print(f"The artist name is {artist_request}")

def option2():
    """
    Displays all sheet data from google doc
    """
    print('\nYour Vinyl Collection:')
    sheet_instance = SHEET.get_worksheet(0)
    records_data = sheet_instance.get_all_records()
    print(tabulate(records_data, tablefmt='rounded_grid'))

def main():
    menu()

if __name__ == '__main__':
    main()