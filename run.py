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

def option1():
    """ 
    option 1
    """
    print('Option 1 has been called using a function')

def option2():
    """
    Displays all sheet data from google doc
    """
    print('\nYour Vinyl Collection:')
    sheet_instance = SHEET.get_worksheet(0)
    records_data = sheet_instance.get_all_records()
    print(tabulate(records_data, tablefmt='rounded_grid'))

menu()
option = int(input('\nEnter a number from 1-4 to navigate through the menu: ').strip())

while option != 4:
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        print('Option 3 has been called')
    else:
        print('Invalid option.')
        menu()

    print()
    option = int(input('\nEnter a number from 1-4 to navigate through the menu: ').strip())

print('You have now exited the programme.')