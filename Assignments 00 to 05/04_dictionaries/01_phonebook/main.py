def main():
    # Create an empty dictionary to store phonebook information
    phonebook = {}

    while True:
        # Ask the user to choose an action
        print("\nPhonebook Menu:")
        print("1. Add contact")
        print("2. Search contact")
        print("3. View all contacts")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            # Add contact to the phonebook
            name = input("Enter the contact name: ")
            phone = input("Enter the phone number: ")
            phonebook[name] = phone
            print(f"Contact for {name} added successfully.")
        
        elif choice == '2':
            # Search for a contact by name
            name = input("Enter the contact name to search: ")
            if name in phonebook:
                print(f"{name}'s phone number is {phonebook[name]}")
            else:
                print("Contact not found.")
        
        elif choice == '3':
            # Display all contacts
            if phonebook:
                print("\nAll Contacts:")
                for name, phone in phonebook.items():
                    print(f"{name}: {phone}")
            else:
                print("No contacts in phonebook.")
        
        elif choice == '4':
            # Exit the program
            print("Exiting phonebook.")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == '__main__':
    main()
