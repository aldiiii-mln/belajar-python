"""
CONTACTS BOOK PROJECT
"""
import json

def save_contact(contact_list):
    with open("contacts.json", "w") as f:
        json.dump(contact_list, f)


def load_contact():
    
    try:
        with open("contacts.json", "r") as f:
            contact_list = json.load(f)
        return contact_list
    except FileNotFoundError:
        return []

def add_contact(contact_list, name, number, email):
    contact_list.append({"Name" : name, "Number" : number, "Email" : email})

def find_contact(contact_list, name):
    check = False
    for contact in contact_list:
        if name.lower() == contact["Name"].lower():
            print(f"Name : {contact['Name']}, Number : {contact['Number']}, Email : {contact['Email']} ")
            check = True
        

    if not check:
        print("We dont find a name contact you have been searched")
    

def update_contact(contact_list, name):
    check = False
    for index, contact in enumerate(contact_list):
        if name.lower() == contact["Name"].lower():
            newname = input("Fill the new Name: ")
            newnumber = input("Fill the new Number: ")
            newemail = input("Fill the new Email: ")
            contact_list[index] = {"Name" : newname, "Number" : newnumber, "Email" : newemail}
            check = True
            break

    if not check:
        print("We dont find a name contact you have been searched to update")

def delete_contact(contact_list, name):
    check = False
    for contact in contact_list[:]:
        if name.lower() == contact["Name"].lower():
            contact_list.remove(contact)
            check = True

    if not check:
        print("We dont find a name contact you have been searched to delete")

def display_contact(contact_list):
    angka = 0
    for contact in contact_list:
        angka += 1
        print(f"{angka}. Name : {contact['Name']}, Number : {contact['Number']}, Email : {contact['Email']} ")
    

def menu(contact_list):
    while True:
        print("===================")
        print("Menu Contact Book")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Find Contact")
        print("4. Look all Contact List")
        print("5. Delete Contact")
        print("6. Out of the Program")
        input_menu = int(input("Choose a menu you want to do (1-6): "))
        if input_menu == 1:
            input_name = input("Fill the Name: ")
            input_number = input("Fill the Number: ")
            input_email = input("Fill the Email: ")
            add_contact(contact_list, input_name, input_number, input_email)
            save_contact(contact_list)

        elif input_menu == 2:
            name3 = input("What's a name of contact you want to find: ")
            update_contact(contact_list, name3)
            save_contact(contact_list)
            
        
        elif input_menu == 3:
           name2 = input("What's a name of contact you want to find: ")
           find_contact(contact_list, name2)

        elif input_menu == 4:
            display_contact(contact_list)

        elif input_menu == 5:
            name3 = input("What's a name of contact you want to delete: ")
            delete_contact(contact_list, name3)
            save_contact(contact_list)
        
        elif input_menu == 6:
            return 
        
        else:
            print("The Number of option you choose is wrong, try again!!!")

    


list_contact = load_contact()

menu(list_contact)
