contacts = {
    "08065323876": "Precious",
    "09037695723": "Adam"
}

def show_app_menu():
    """
    show_app_menu This Function will display the app menu
    """
    print("1. View contacts")
    print("2. Add contact")
    print("3. Search contacts")
    print("4. Exit")
    
    select_app_name()
    
def select_app_name():
    repeat = True
    while repeat == True:
        try:
            option = int(input("Choose[1-4]: "))
        except ValueError:
            print("Please input number")
            # fill the option with value so the program won't error
            option = 0
        if option > 0 and option < 6: repeat = False
        
        if option == 1:
            showContacts()
            show_app_menu()
        elif option == 2:
            contact_str = str(input("Provide Contact Name and Number"))
            addContacts(contact_str=contact_str)
            show_app_menu()
        elif option == 3:
            contact_number = str(input("Provide Contact Number"))
            searchContacts(number=contact_number)
            show_app_menu()
        elif option == 4:
            print("Good bye!")
            break
        else:
            print("Option unavailable.")
            
def showContacts():
    """
    showContacts Print out All Contacts in our Contact Book
    """
    
    # manual numbering
    num = 1
    print("=====================================") #42
    print(" No. | Name        | Number         |")
    print("=====================================")
    for key, val in contacts.items():
        # forma to left-align and give some spacing
        print("|{no} .| {name:<15} | {number:<15}  |"
        .format(no = num, name = val,
                number = key))
        num += 1
    print("=====================================")
    
def addContacts(contact_str: str):
    """
    addContacts Adds a contacts to your contact book 

    Args:
        contact_str (str): Contact Name and Number Separated by coma (eg Hassanat, 123456)
    """
    name, number = contact_str.split(",")
    contacts[number] = name
    print("===== Contact Added Successfully======")
    
def searchContacts(number: str):
    record = contacts.get(number, None)
    if  not record:
        print("======= Contact does not exist in our contact book=====")
    else:
        num = 1
        print("=====================================")
        print("|No. | Name          | Number       |")
        print("=====================================")
        print("|{no} .| {name:<15} | {number:<15}  |"
            .format(no = num, name = record,
                    number = number))
        print("=====================================")

show_app_menu()