
import sys 

dishes = ['Orilla', 'Desierto Rojo']

def create_dish(dish_name):
    global dishes

    if dish_name not in dishes:
        dishes.append(dish_name)
    else: 
        print('This dish already is in the list')


def update_dish(dish_name):
    global dishes

    if dish_name in dishes:
        index = dishes.index(dish_name)
        updated_name = input('What is the updated dish name ? ')
        dishes[index] = updated_name
    else: 
        not_in_list_msg


def search_dish(dish_name):
    global dishes

    for dish in dishes:
        if dish != dish_name:
            continue
        else:
            return True


def delete_dish(dish_name):
    global dishes

    if dish_name in dishes:
        dishes.remove(dish_name)
    else: 
        not_in_list_msg()


def get_dish_name():
    dish_name = None

    while not dish_name: 
        dish_name = str(input('What is the dish name ? '))

        if dish_name == 'exit': 
            dish_name = None
            break 

    if not dish_name: 
        sys.exit()

    return dish_name


def not_in_list_msg():
    print('This dish is not in the list')
    


def list_dishes():
    for index, dish in enumerate(dishes):
        print('{}: {}'.format(index, dish))


def print_welcome():
    print('WELCOME PYTHON CRUD')
    print('*' * 50)
    print('What would you like to do today ?')
    print('[C]reate dish')
    print('[L]ist dishes')
    print('[U]pdate dish')
    print('[D]elete dish')
    print('[S]earch dish')


print_welcome()

command = input()
command = command.upper()

if command == 'C':
    dish_name = get_dish_name()
    create_dish(dish_name)
    list_dishes()
elif command == 'L':
    list_dishes()
elif command == 'U':
    dish_name = get_dish_name()
    update_dish(dish_name)
    list_dishes()    
elif command == 'D':
    dish_name = get_dish_name()
    delete_dish(dish_name)
    list_dishes()  
elif command == 'S':
    dish_name = get_dish_name()
    found = search_dish(dish_name)
    if found: 
        print('The dish is in the list')
    else:
        print('The dish {} is not in our list'.format(dish_name))
else: 
    print('Invalid command')