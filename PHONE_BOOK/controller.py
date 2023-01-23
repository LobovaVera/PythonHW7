import view
global action
action = 0 
global phone_book
phone_book = []

def start():
    commands = {1: 'Показать все контакты',
    2: 'Открыть файл',
    3: 'Сохранить файл',
    4: 'Новый контакт',
    5: 'Изменить контакт',
    6: 'Удалить контакт',
    7: 'Найти контакт',
    8: 'Выйти из программы'}

    print( f"Выберите пункт меню")
    print(f" {commands}")
    get_action()


def get_action():
    global action 
    try:
        action = int(input("Введите число команды: "))
    except ValueError:
        print("Введите число цифрами без пробелов")
    
def show_contacts():
    path = 'PHONE_BOOK\data.txt'
    with open(path, 'r', encoding = 'UTF-8') as file:
        data = file.readlines()
    for line in data:
        phone_book.append(line.strip().split(';'))
    for line in phone_book:
        print( f"{line} \n")

#  def open_():

