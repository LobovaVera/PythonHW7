import view
import model

def start():

    view.model_menu()
    act = view.action()
    model.activate_phone_book()

    match act:
        case 1:
            a = model.activate_phone_book()
            view.show_contacts(a)
          
        case 2:
            model.open_name()
            view.show(model.open_name())
           
        case 3:
            view.show(model.save_new_contact(view.my_input()))
          
        case 4:
            model.create_contact()
          
        case 5:
            model.change_contact()
          
        case 6:
            model.delete_contact()

        case 7:
            model.search_contact()
        case 8:
            exit()
    start()
  
        

    


