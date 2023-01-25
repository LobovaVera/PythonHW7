

contact =''

#я не понимаю зачем get new contact
# def get_new_contact():
#     global contact
#     return contact

my_action = 0 

# и это 
# def get_action():
#     global my_action
#     return my_action
global phone_book
phone_book = []
path = 'PHONE_BOOK\data.txt'


def model_menu():
    command = {1: 'Показать все контакты',
    2: 'Открыть файл', 
    3: 'Сохранить файл',
    4: 'Новый контакт',
    5: 'Изменить контакт',
    6: 'Удалить контакт',
    7: 'Найти контакт',
    8: 'Выйти из программы'}

    print("Выберите пункт меню: ")
    
    for a, b in command.items():
        print( f"{a} {b} \n")

def action():
    global my_action 
    try:
        my_action = int(input("Введите число команды: "))
        return my_action
    except ValueError:
        print("Введите число цифрами без пробелов")
        while True:
            continue

def show(data):
    print(data)


def get_contact_info(num):
    global temp
    temp = []
    match num:
        case 1:
            temp.append(input("Введите фамилию имя и отчество: ") )
        case 2:
            temp.append(input("Введите номер: "))
        case 3:
            temp.append(input("Введите комментарий: "))
    
    return temp


def my_input():
    return input("Введите информацию, чтобы сохранить: ")

def get_contact_num():
    while True:
        cont_num = input("Выберите контакт, введите номер контакта: ")
        try: 
            num = int(cont_num)
            return cont_num
        except:
            print("Введите цифру")
            continue

def show_contacts(book):
    for i in range(0, len(book)):
        print( f"{i+1} {book[i]} \n")

def get_approve():
    our_bool = True
    while True:
        try:
            a =  int(input(" 1 - да, 0 - нет"))
            if a:
                our_bool = True
            else:
                our_bool = False
            return our_bool
        except ValueError:
            print("Введите цифру 0 или 1")
        continue
    