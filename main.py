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

    while True:
        show_menu()
        choice = input("Select an option: ")
        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            book.add_contact(name, phone, email)
            print("Contact added successfully.")

        elif choice == "2":
            print("Contacts list:")
            print("\n")
            book.list_contacts()

        elif choice == "3":
            name = input("Name to search: ")
            contact = book.find_contact(name)
            if contact:
                print("Contact found:", contact)
            else:
                print("Contact not found")        

        elif choice == "4":
            name = input("Name to delete: ")
            if book.delete_contact(name):
                print("Contact successfully deleted.")
            else:
                print("Contact not found.")

        elif choice == "5":
            print("Leaving the contact manager. ¡See you later!")
            break

if __name__ == "__main__":
    main()
