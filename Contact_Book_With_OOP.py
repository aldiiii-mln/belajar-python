import json

class ContactsBook():
    def __init__(self):
        self.contact_list = []

    def save(self):
        with open("contact.json", "w") as f:
            json.dump(self.contact_list, f)

    def load(self):
        try:
            with open("contact.json", "r") as f:
                self.contact_list = json.load(f)
            
        except FileNotFoundError:
           self.contact_list = []

    def add_contactlist(self, name, number, email):
        self.contact_list.append({"Name" : name, "Number" : number, "Email" : email})
    
    def delete_contactlist(self, name):
        check = False
        for contact in self.contact_list[:]:
            if name.lower() == contact["Name"].lower():
                self.contact_list.remove(contact)
                check = True
        if not check:
            print("There is no account of contact you searched to delete")
    
    def update_contactlist(self, name):
        check = False
        
        for i, contact in enumerate(self.contact_list):
            if name.lower() == contact["Name"].lower():
                newname = input("What is Your New Name? ")
                number = input("What is Your New Number? ")
                email = input("What is Your New Email? ")
                self.contact_list[i] = {"Name" : newname, "Number" : number, "Email" : email}
                check = True
                break
        if not check:
            print("There is no account of contact you searched to update")
    
    def find_contactlist(self, name):
        check = False
        for contact in self.contact_list:
            if name.lower() == contact["Name"].lower():
                print(f"Name: {contact['Name']}, Number: {contact['Number']}, Email: {contact['Email']}")
                check = True
        if not check:
            print("There is no account of contact you searched")

    
    def display_contactlist(self):
        angka = 0
        for contact in self.contact_list:
            angka += 1
            print(f"{angka}. Name: {contact['Name']}, Number: {contact['Number']}, Email: {contact['Email']}")


def menu():
    book = ContactsBook()
    book.load()

    while True:
        print("===================")
        print("Menu Contact Book")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Find Contact")
        print("4. Look all Contact List")
        print("5. Delete Contact")
        print("6. Out of the Program")
        try:    
            input_menu = int(input("Choose a menu you want to do (1-6): "))
            
        except ValueError:
            print("Pick Option with number 1-6 and try again")
            continue
        if input_menu == 1:
            name = input("What is Your Name? ")
            number = input("What is Your Number? ")
            email = input("What is Your Email? ")
            book.add_contactlist(name, number, email)
            book.save()
        elif input_menu == 2:
            name_update = input("What is the name of account you want to update? ")
            book.update_contactlist(name_update)
            book.save()
        elif input_menu == 3:
            name_find = input("What is the name of account you want to find? ")
            book.find_contactlist(name_find)
        elif input_menu == 4:
            book.display_contactlist()
        elif input_menu == 5:
            name_delete = input("what is the name of account you want to delete? ")
            book.delete_contactlist(name_delete)
            book.save()
        elif input_menu == 6:
            return
        else:
            print("Error: You choose wrong option. Try Again!!!")

menu()
    
    