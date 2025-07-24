from contact_book import ContactBook

def show_menu():
    print("--- Contacts Manager ---")
    print("\n")
    print("-------------------------")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Find contact by name")
    print("4. Delete contact")
    print("5. Exit")

def main():
    book = ContactBook()