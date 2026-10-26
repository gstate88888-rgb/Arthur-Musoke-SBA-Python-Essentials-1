# Arthur Musoke
# Python Essentials 1 SBA - Contact Book

# Dictionary to store contacts
contacts = {}


# Add a contact
def add_contact():
    name = input("Enter contact name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    if name in contacts:
        print("Contact already exists.")
        return

    phone = input("Enter phone number: ").strip()

    if not phone.isdigit():
        print("Phone number must contain only digits.")
        return

    contacts[name] = phone
    print("Contact added successfully.")


# View all contacts
def view_contacts():
    if not contacts:
        print("Contact list is empty.")
        return

    print("\nContacts:")
    for name, phone in contacts.items():
        print(f"Name: {name}, Phone: {phone}")


# Search for a contact
def search_contact():
    search = input("Enter name to search: ").strip()

    found = False

    for name, phone in contacts.items():
        if search.lower() in name.lower():
            print(f"Name: {name}, Phone: {phone}")
            found = True

    if not found:
        print("No matching contact found.")


# Delete a contact
def delete_contact():
    name = input("Enter contact name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


# Main menu loop
while True:

    print("\n===== Contact Book Menu =====")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            add_contact()

        elif choice == 2:
            view_contacts()

        elif choice == 3:
            search_contact()

        elif choice == 4:
            delete_contact()

        elif choice == 5:
            print("Thank you for using Contact Book.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

    except ValueError:
        print("Invalid input. Please enter a number.")
