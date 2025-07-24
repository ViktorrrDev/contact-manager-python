from contact import Contact

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
    
    def list_contacts(self):
        if not self.contacts:
            print("There aren't contacts registered")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact}")
    
    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None