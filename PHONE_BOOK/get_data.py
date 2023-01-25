# while True:
#     cont_num = 0
#     cont_num = input("Выберите контакт, введите номер контакта: ")
#     try: 
#         num = int(cont_num)
#     except:
#         print("Введите цифру")
#         continue
# def update_phone_book():
#     global phone_book
#     activate_phone_book()



# def change_contact():
#     global contact
#     global path
#     global phone_book
#     num = 0 
#     activate_phone_book()
#     view.show_contacts()
#     cont_num = view.get_contact_num()

#     changed_cont = phone_book[num-1]
#     print(f"Изменим контакт {cont_num} {phone_book[num-1]}")
#     contact = ''
#     for i in range(0,2):
#         contact += view.get_contact_info(i) +' '
#     for i in range(2,6):
#         contact += view.get_contact_info(i) +';'
#     # save_new_contact(contact)
#     phone_book.pop(cont_num)
#     phone_book.insert(cont_num, contact)
#     print(phone_book)