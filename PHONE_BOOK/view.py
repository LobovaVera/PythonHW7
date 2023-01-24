import main

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

def main_menu():
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

def create_contact():
    global contact 
    contact = ''
    temp = input("Введите фамилию: ")
    contact += temp + ' '
    temp = input("Введите имя: ")
    contact += temp + ' '
    temp = input("Введите отчество: ")
    contact += temp + ';'
    temp = input("Введите номер: ")
    contact += temp + ';'
    temp = input("Введите комментарий: ")
    contact += temp + ';'

    print(f"Сохранить контакт {contact} ?")
    try:
        temp_bool = int(input(" 1 - да, 0 - нет"))
    except ValueError:
        print("Введите цифру 0 или 1")

    if temp_bool:
        
        print(main.save_new_contact(contact))
    else:
        print("Контакт не сохранен")

def my_input():
    return input("Введите информацию, чтобы сохранить: ")
