
import csv
import os

DISHES_TABLE = 'dishes.csv'
DISHES_SCHEMA = ['name', 'ingredients', 'high']

dishes = []

def initialize_dishes_from_storage():
    with open(DISHES_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=DISHES_SCHEMA)

        for row in reader: 
            dishes.append(row)

def save_dishes_to_storage():
    tmp_table_name = '{}.tmp'.format(DISHES_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=DISHES_SCHEMA)
        writer.writerows(dishes)

        os.remove(DISHES_TABLE)
        os.rename(tmp_table_name, DISHES_TABLE)

def create_dish(dish):
    global dishes

    if dish not in dishes:
        dishes.append(dish)
    else: 
        print('This dish already is in the list')


def update_dish(dish_id):
    global dishes

    for index, dish in enumerate(dishes):
        option = 0
        not_in_list = 0
        if dish_id != index:
            not_in_list += 1 
        else:
            while option != 4:
                print('[1] Update Name')
                print('[2] Update Ingredients')
                print('[3] Update High')
                print('[4] Exit Update')
                option = int(input())
                if option == 1: 
                    updated = input('What is the updated dish name ? ')
                    dish['name'] = updated
                elif option == 2: 
                    updated = input('What is the updated ingredients list ? ')
                    dish['ingredients'] = updated
                elif option ==3:
                    updated = input('What is the updated high ? ')
                    dish['high'] = updated

    if(not_in_list == index):
        not_in_list_msg()
        


def search_dish(dish_id):
    global dishes

    for index, dish in enumerate(dishes):
        if dish_id != index:
            continue
        else:
            return True


def delete_dish(dish_id):
    global dishes

    for index, dish in enumerate(dishes): 
        if dish_id == index:
            del dishes[dish_id]
        else: 
            not_in_list_msg()

def get_dish_field(field_name):
    field = None 

    while not field: 
        field = input('What is the dish {} ? '.format(field_name))

    return field


def get_dish_id():
    return int(input('What is the dish id ? '))


def not_in_list_msg():
    print('This dish is not in the list')
    

def list_dishes():
    print('ID | Name | Ingredients | High |')
    print('-' * 50)
    for index, dish in enumerate(dishes):
        print('{dish_id} | {name} | {ingredients} | {high} msnm'.format(
            dish_id = index,
            name = dish['name'],
            ingredients = dish['ingredients'],
            high = dish['high']
        ))


def print_welcome():
    print('WELCOME TO CENTRAL CRUD')
    print('*' * 50)
    print('What would you like to do today ?')
    print('[C]reate dish')
    print('[L]ist dishes')
    print('[U]pdate dish')
    print('[D]elete dish')
    print('[S]earch dish')
    print('[E]xit')

# MAIN

initialize_dishes_from_storage()

command = ''

while command != 'E':

    print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        dish = {
            'name': get_dish_field('name'),
            'ingredients': get_dish_field('ingredients'),
            'high': get_dish_field('high')
        }
        create_dish(dish)
    elif command == 'L':
        list_dishes()
    elif command == 'U':
        dish_id = get_dish_id()
        update_dish(dish_id)    
    elif command == 'D':
        dish_id = get_dish_id()
        delete_dish(dish_id) 
    elif command == 'S':
        dish_id = get_dish_id()
        found = search_dish(dish_id)
        if found: 
            print('The dish is in the list')
        else:
            print('The dish {} is not in our list'.format(dish_name))
    elif command == 'E':
        print('Thanks for use the system!')
    else: 
        print('Invalid command')

save_dishes_to_storage()