import view

contact = 0
global phone_book
phone_book = []
path = 'PHONE_BOOK\data.txt'


def activate_phone_book():
    global path
    global phone_book
    phone_book = []

    path = 'PHONE_BOOK\data.txt'
    with open(path, 'r', encoding = 'UTF-8') as file:
        data = file.readlines()
    for line in data:
        phone_book.append(line.strip().split(';'))
    return phone_book

def open_name():
    activate_phone_book()
    return "Вы открыли телефонную книгу"
    

def save_new_contact(contact: str):
    print(f"Сохранить контакт {contact} ?")
    try:
        temp_bool = int(input(" 1 - да, 0 - нет"))
    except ValueError:
        print("Введите цифру 0 или 1")

    if temp_bool:
        global path
        path = 'PHONE_BOOK\data.txt'
        with open(path, 'a', encoding = 'UTF-8') as file:
            data = file.writelines(contact + '\n')
        print("Контакт добавлен")  
    else:
        print("Контакт не сохранен")
  

def update_phone_book(book):

    global path
    path = 'PHONE_BOOK\data.txt'

    with open(path, 'w', encoding = 'UTF-8') as file:
        for el in book:
            for item in el:
                data = file.writelines(item)
                
                if el.index(item) != 2:
                    data = file.writelines(';')
        
            data = file.writelines('\n')


def change_contact():
    global contact
    global path
    global phone_book

    activate_phone_book()
    view.show_contacts(phone_book)
    cont_num = view.get_contact_num()

    print(f"Изменим контакт {cont_num} {phone_book[int(cont_num)-1]}")
    contact = []
    for i in range(1,4):
        contact.append(view.get_contact_info(i))

    phone_book.pop(int(cont_num)-1)
    phone_book.insert(int(cont_num)-1, contact)

    update_phone_book(phone_book)


def delete_contact():
    global contact
    global path
    global phone_book
    num = 0 

    view.show_contacts(phone_book)
    view.show_contacts(phone_book)
    cont_num = view.get_contact_num()
    

    print(f"Удалим контакт {cont_num} {phone_book[num-1]}?")
    temp_bool = view.get_approve()
    
    if temp_bool:
        phone_book.pop(num-1)
        update_phone_book()




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
           

def create_contact():
    global contact 
    contact = []
    for i in range(1, 4):
        contact.append(str(view.get_contact_info(i)) +';')

    save_new_contact(str(contact))

