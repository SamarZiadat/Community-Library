import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('vinyl_collection')

def menu():
    """
    Get menu option input from user
    """
    print('Menu')
    print('1. Add a new vinyl to the collection')
    print('2. Display full collection')
    print('3. Edit collection')
    print('4. Exit')

def option1():
    """ 
    option 1
    """
    print('Option 1 has been called using a function')

menu()
option = int(input('Enter a number from 1-4 to navigate through the menu: ').strip())

while option != 4:
    if option == 1:
        option1()
    elif option == 2:
        print('Option 2 has been called')
    elif option == 3:
        print('Option 3 has been called')
    else:
        print('Invalid option.')
        menu()

    print()
    option = int(input('Enter a number from 1-4 to navigate through the menu: ').strip())

print('You have now exited the programme.')


