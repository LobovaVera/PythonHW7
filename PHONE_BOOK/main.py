

contact = 0
phone_book = []
path = 'PHONE_BOOK\data.txt'


def get_phone_book():
    global phone_book
    return phone_book


def get_path():
    global path
    return path 

def get_new_contact():
    global contact
    return contact

def activate_phone_book():
    global path
    global phone_book

    path = 'PHONE_BOOK\data.txt'
    with open(path, 'r', encoding = 'UTF-8') as file:
        data = file.readlines()
    for line in data:
        phone_book.append(line.strip().split(';'))

   
    
def show_contacts():
    global path
    global phone_book
    activate_phone_book()
    for i in range(0, len(phone_book)):
        print( f"{i+1} {phone_book[i]} \n")
    

def open_name():
    activate_phone_book()
    return "Вы открыли телефонную книгу"
    
    

def save_new_contact(contact):
    
    global path
    
    path = 'PHONE_BOOK\data.txt'
    with open(path, 'a', encoding = 'UTF-8') as file:
        data = file.writelines(contact + '\n')
    return "Контакт добавлен"


def change_contact():
    global contact
    global path
    num = 0 

    show_contacts()

    cont_num = input("Выберите контакт, введите номер контакта: ")
    try: 
        num = int(cont_num)
    except:
        print("Введите цифру")
        while True:
            continue

    changed_cont = phone_book[num-1]
    print(f"Изменим контакт {cont_num} {phone_book[num-1]}")



def delete_contact():
    global contact
    global path
    global phone_book
    num = 0 

    show_contacts()
    
    cont_num = input("Выберите контакт, введите номер контакта: ")
    try: 
        num = int(cont_num)
    except:
        print("Введите цифру")
        while True:
            continue

    
    print(f"Удалим контакт {cont_num} {phone_book[num-1]}?")
    try:
        temp_bool = int(input(" 1 - да, 0 - нет"))
    except ValueError:
        print("Введите цифру 0 или 1")
        while True:
            continue
    
    if temp_bool:
        phone_book.pop(num-1)
        with open(path, 'w', encoding = 'UTF-8') as file:
            data = file.writelines(phone_book)
        
        print(phone_book)




def search_contact():
    activate_phone_book()
    global phone_book

    search = input("Введите информацию для поиска: ")
    temp_bool = True
    for line in phone_book:
        for field in line:
            if search.lower() in field.lower(): 
                if len(line) >=3:
                    print(f'{line[0]} {line[1]} {line[2]} ')
                else:
                    print(*line)
                temp_bool = False
    if temp_bool:
        return "Ничего не найдено"
           


