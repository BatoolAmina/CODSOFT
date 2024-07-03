contacts = {}

# Function to add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"Contact {name} added successfully!")

# Function to view all contacts
def view_contacts():
    if contacts:
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")
    else:
        print("No contacts found.")

# Function to search for a contact by name or phone number
def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search_term == name or search_term == details['phone']:
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

# Function to update a contact's details
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Enter new details (leave blank to keep current value):")
        phone = input(f"New phone number (current: {contacts[name]['phone']}): ") or contacts[name]['phone']
        email = input(f"New email (current: {contacts[name]['email']}): ") or contacts[name]['email']
        address = input(f"New address (current: {contacts[name]['address']}): ") or contacts[name]['address']
        
        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print(f"Contact {name} updated successfully!")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found.")

# User interface
def main():
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
