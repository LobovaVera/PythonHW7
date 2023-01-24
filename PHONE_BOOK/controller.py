import view
import main

def start():


    view.main_menu()
    act = view.action()
    main.activate_phone_book()

    match act:
        case 1:
            main.show_contacts()
          
        case 2:
            main.open_name()
            view.show(main.open_name())
           
        case 3:
            
            view.show(main.save_new_contact(view.my_input()))
          
        case 4:
            view.create_contact()
            
        case 5:
            main.change_contact()
          
        case 6:
            main.delete_contact()
          
        case 7:
            main.search_contact()
        case 8:
            exit()
    start()
  
        

    
start()

