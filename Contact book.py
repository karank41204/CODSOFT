
contacts = [ ]

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("✅ Contact added successfully!")


def view_contacts():
    if not contacts:
        print("\nNo contacts available.")
        return

    print( "\n------ Contact List ------")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")


def search_contact():
    if not contacts:
        print("\nNo contacts available.")
        return



    search = input("\nEnter Name or Phone Number to search: ").lower()

    found = False
    for contact in contacts:
        if search == contact["name"].lower() or search == contact["phone"]:
            print("\nContact Found")
            print("----------------------")
            print("Name    :", contact["name"])
            print("Phone   :", contact["phone"])
            print("Email   :", contact["email"])
            print("Address :", contact["address"])
            found = True

    if not found:
        print("❌ Contact not found.")



def update_contact():
    phone = input("\nEnter Phone Number of contact to update: ")

    for contact in contacts:
        if contact["phone"] == phone:
            print("\nLeave blank to keep old value.")

            new_name = input(f"New Name ({contact['name']}): ")
            new_phone = input(f"New Phone ({contact['phone']}): ")
            new_email = input(f"New Email ({contact['email']}): ")
            new_address = input(f"New Address ({contact['address']}): ")

            if new_name:
                contact["name"] = new_name
            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email
            if new_address:
                contact["address"] = new_address

            print("✅ Contact updated successfully!")
            return

    print("❌ Contact not found.")


def delete_contact():
    phone = input("\nEnter Phone Number to delete: ")

    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            print("✅ Contact deleted successfully!")
            return

    print("❌ Contact not found.")


while True:
    print("\n========== CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("\nThank you for using Contact Book!")
        break

    else:
        print("❌ Invalid choice! Please enter a number between 1 and 6.")