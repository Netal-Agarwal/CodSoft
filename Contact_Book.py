contact_list =[]

def display_menu(): 
    print("Contact Book Menu")
    print("1.Add a contact")
    print("2.Search for a contact")
    print("3.Update a contact")
    print("4.Delete a contact")
    print("5.Display all the details")
    print("6.Exit")
    
def add_contact():
    name = input("Enter the name of the person ")
    email = input("Enter the email of the person: ")
    phone = input("Enter the phone number of the person: ")
    address = input("Enter the address of the person:")
    contact = {"Name": name, "Email": email, "Phone": phone,"Address": address} 
    contact_list.append(contact)  
    print("Contact added.")

def search_contact():
    search_term = input("Enter the name or email of the contact to search: ")
    found_contacts = [] 
    for contact in contact_list:
        if search_term.lower() in contact["Name"].lower() or search_term.lower() in contact["Email"].lower():
            found_contacts.append(contact) 

    if found_contacts:
        print("Contacts found:")
        for contact in found_contacts: 
            print("Name:", contact["Name"])
            print("Email:", contact["Email"])
            print("Phone:", contact["Phone"])
            print("Address:", contact["Address"])
            print("-------------------")
    else:
        print("No contacts found.")
        
def update_contact():
    name = input("Enter the name of the contact to update: ") 
    found_contact = None 
    for contact in contact_list: 
        if contact["Name"].lower() == name.lower():
            found_contact = contact  
            break

    if found_contact:  
        print("Contact found. Enter new details:")
        found_contact["Name"] = input("Enter the new name: ")
        found_contact["Email"] = input("Enter the new email: ")
        found_contact["Phone"] = input("Enter the new phone number: ")
        found_contact["Address"]= input("Enter the address:")
        print("Contact updated.")
    else:
        print("Contact not found.")
        
def delete_contact():
    name = input("Enter the name of the contact to be deleted: ")  
    for contact in contact_list:  
        if contact["Name"].lower() == name.lower():  
            contact_list.remove(contact)  
            print("Contact deleted.")
            break
    else:
        print("Contact not found.")
        
def display_all_contacts():
    if contact_list:
        print("All Contacts:")
        for contact in contact_list:  
            print("Name:", contact["Name"])
            print("Email:", contact["Email"])
            print("Phone:", contact["Phone"])
            print("Address:",contact["Address"])
            print("-------------------")
    else:
        print("No contacts found.")
        
while True:
    display_menu()
    choice = input("What would you like to do?")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_all_contacts()
    elif choice == "6":
        print("Exit")
        break 
    else:
        print("Invalid choice. Please enter a valid choice (1-6).")
        
