import json
from Client import VIP, Client, Premium

class Bank:

    clients = []
    json_clients = {'basic':[], 'vip':[], 'premium':[]}
    init_add = False

    def add_client(self, id, pwd, name, balance, tier):
        for client in self.clients:
            if client.id == id:
                print('ID already exists')
                input('Press Enter to continue')
                return  
        if tier == '': tier = Client  
        new_client = tier(id, pwd, name, balance, tier)
        self.clients.append(new_client)
        if self.init_add == False:
            print(f'New Client added: {new_client.__str__()}')
            input('Press Enter to continue')

    def remove_client(self, id):
        for client in self.clients:
            if client.id == id:
                self.clients.remove(client)
                print(f'{client.name} removed')
                input('Press Enter to continue')
                return
        print('Not found!')
        input('Press Enter to continue') 

    def search_client(self, id):
        for client in self.clients:
            if client.id == id:
                print(client.__str__())
                input('press Enter to continue')
                return
        print('Not found!')
        input('Press Enter to continue')    
    
    def print_all(self):
        for client in self.clients:
            print(client.__str__())
        input('press Enter to continue')

    def sort_to_classes_and_convert_to_json(self):
        self.json_clients = {'basic':[], 'vip':[], 'premium':[]}
        for client in self.clients:
            if client.tier == Client:
                self.json_clients['basic'].append(json.loads(client.to_json()))
            if client.tier == VIP:
                self.json_clients['vip'].append(json.loads(client.to_json()))
            if client.tier == Premium:
                self.json_clients['premium'].append(json.loads(client.to_json()))
        return self.json_clients
    
    def json_to_obj(self):
        self.init_add = True
        for client in self.json_clients['basic']:
            self.add_client(client['ID'], client['Password'], client['Name'], client['Balance'], Client)
        for client in self.json_clients['vip']:
            self.add_client(client['ID'], client['Password'], client['Name'], client['Balance'], VIP)
        for client in self.json_clients['premium']:
            self.add_client(client['ID'], client['Password'], client['Name'], client['Balance'], Premium)
        self.init_add = False


