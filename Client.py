import json

class Client:
    id = ''
    pwd = ''
    name = ''
    balance = 0
    tier = ''

    def __init__(self, id, pwd, name, balance = 1000, tier = ''):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.balance = balance
        self.tier = tier

    def deposit(self, ammount):
        self.balance += ammount
        print(f'Deposit successful!, New balance is {self.balance}')
        input('Press any key to continue')

    def withdraw(self, ammount):
        if self.balance >= ammount:
            self.balance -= ammount
            print(f'Withdraw successful!, New balance is {self.balance}')
            input('Press any key to continue')
        else:
            print('Insufficient funds!')
            input('Press any key to continue')
    
    def show_balance(self):
        print(f'Current balance is: {self.balance}')
        input('Press any key to continue')
    
    def transfer(self, recepient, ammount, bank_name):
        for client in bank_name.clients:
            if client.id == recepient:
                if self.balance >= ammount:
                    self.balance -= ammount
                    client.balance += ammount
                    print(f'Transfer successful!, New balance is {self.balance}')
                    input('Press any key to continue')
                    return
                else:
                    print('Insufficient funds!')  
                    input('Press any key to continue')
                    return
        print('Recepient not found!')
        input('Press any key to continue')
        return

    def to_json(self):
        return json.dumps({'ID': self.id, 'Password': self.pwd, 'Name': self.name, 'Balance': self.balance})

    def __str__(self):
        return {'ID': self.id, 'Password': self.pwd, 'Name': self.name, 'Balance': self.balance, 'Tier': self.tier}

class VIP(Client):
        def deposit(self, ammount):
            self.balance += ammount * 1.05
            print(f'Deposit successful!, VIP and Premium get extra 5% for deposits! New balance is {self.balance}')
            input('Press any key to continue')

class Premium(VIP):
        def withdraw(self, ammount):
            if self.balance - ammount >= -2000:
                self.balance -= ammount
                print(f'Withdraw successful!, Premiums are allowed to overdraft up to -2000, New balance is {self.balance}')
                input('Press any key to continue')
            else:
                print('Insufficient Credit!')
                input('Press any key to continue')
        