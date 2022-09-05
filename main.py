import json
from enum import Enum
from Bank import Bank
from Client import Client, VIP, Premium
# from Client import Client
import os

class AdminActions(Enum):
    ADD_CLIENT = 1
    DEL_CLIENT = 2
    SEARCH = 3
    PRINT_ALL = 4
    BACK = 0

class ClientActions(Enum):
    WITHDRAW = 1
    DEPOSIT = 2
    TRANSFER = 3
    SHOW_BALANCE = 4
    BACK = 0

class MainMenu(Enum):
    CLIENT_LOGIN = 1
    ADMIN_LOGIN = 2
    EXIT = 0


bank = Bank()
DATA_FILE = 'clients.json'

def load():
    try:
        with open(DATA_FILE, 'r') as outfile:
            bank.json_clients = json.load(outfile)
            bank.json_to_obj()
    except: pass

def save():
    with open(DATA_FILE, 'w') as outfile:
        bank.sort_to_classes_and_convert_to_json()
        json.dump(bank.json_clients, outfile, indent = 4)

def menu(menu):
    if menu == 'main':
        for option in MainMenu:
            print(f'{option.value} for {option.name}')
    if menu == 'client':
        for option in ClientActions:
            print(f'{option.value} for {option.name}')
    if menu == 'admin':
        for option in AdminActions:
            print(f'{option.value} for {option.name}')

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    user_selection = ''
    load()
    # statrs the main loop, breaks on exit
    while user_selection != MainMenu.EXIT.value:
        cls()
        user_selection = ''
        menu('main')
        user_selection = int(input('Enter your choice: '))
        # admin controls starts here
        if user_selection == MainMenu.ADMIN_LOGIN.value:
            user_selection = ''
            while user_selection != AdminActions.BACK.value:
                cls()
                menu('admin')
                user_selection = int(input('Enter your choice: '))
                if user_selection == AdminActions.ADD_CLIENT.value: 
                    cls()
                    try:
                        bank.add_client(input('ID: '), input('Password: '), input('Name: '), 1000, globals()[input('Client/VIP/Premium(CAPs Sensitive!): ')])
                    except:
                        pass
                if user_selection == AdminActions.DEL_CLIENT.value: cls(), bank.remove_client(input("Enter client's ID: "))
                if user_selection == AdminActions.SEARCH.value: cls(), bank.search_client(input("Enter client's ID: "))
                if user_selection == AdminActions.PRINT_ALL.value: cls(), bank.print_all()
            user_selection = ''
        # client control starts here
        if user_selection == MainMenu.CLIENT_LOGIN.value:
            cls()
            user_selection = ''
            # user login 
            active_client_id = input('ID: ')
            active_client_pwd = input('Password: ')
            for client in bank.clients:
                if client.id == active_client_id and client.pwd == active_client_pwd:
                    # if login successful:
                    while user_selection != ClientActions.BACK.value:
                        cls()
                        print(f'Hi {client.name}, Welcome Back!')
                        menu('client')
                        user_selection = int(input('Enter your choice: '))
                        if user_selection == ClientActions.DEPOSIT.value: client.deposit(int(input('Enter ammount:')))
                        if user_selection == ClientActions.WITHDRAW.value: client.withdraw(int(input('Enter ammount:')))
                        if user_selection == ClientActions.SHOW_BALANCE.value: client.show_balance()
                        if user_selection == ClientActions.TRANSFER.value: client.transfer(input('Enter recepient ID: '), int(input('Enter ammount: ')), bank)
                    user_selection = ''
                    break  
    save()


if __name__ == '__main__':
    main()