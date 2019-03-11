
import sys 

clients = 'Lionel,Gerard,'

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name 
        add_comma()
    else: 
        print('Client already is in the client\'s list')


def update_client(client_name):
    global clients 

    if client_name in clients:
        updated_name = input('What is the updated client name ? ')
        clients = clients.replace(client_name + ',', updated_name + ',')
    else: 
        not_in_list_msg

def search_client(client_name):
    global clients

    clients_list = clients.split(',')
    for client in clients_list:
        if client_name != client:
            continue
        else:
            return True


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else: 
        not_in_list_msg()


def get_client_name():
    client_name = None

    while not client_name: 
        client_name = input('What is the client name ? ')

        if client_name == 'exit': 
            client_name = None
            break 

    if not client_name: 
        sys.exit()

def not_in_list_msg():
    print('Name is not in client\'s list')
    


def list_clients():
    print(clients)


def add_comma():
    global clients 

    clients += ','


def print_welcome():
    print('WELCOME PYTHON CRUD')
    print('*' * 50)
    print('What would you like to do today ?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


print_welcome()

command = input()
command = command.upper()

if command == 'C':
    client_name = get_client_name()
    create_client(client_name)
    list_clients()
elif command == 'U':
    client_name = get_client_name()
    update_client(client_name)
    list_clients()    
elif command == 'D':
    client_name = get_client_name()
    delete_client(client_name)
    list_clients()  
elif command == 'S':
    client_name = get_client_name()
    found = search_client(client_name)
    if found: 
        print('The client is in the client\'s list')
    else:
        print('The name {} is not in our client\'s list'.format(client_name))
else: 
    print('Invalid command')