import json
import os
import csv
import re

CONTACTS_FILE = 'contacts.json'
CSV_FILE = 'contacts.csv'

# Load contacts from JSON file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save contacts to JSON file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Validate phone number (10-digit number)
def is_valid_phone(phone):
    return re.fullmatch(r'\d{10}', phone) is not None

# Validate email address format
def is_valid_email(email):
    return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Get valid phone input
def input_valid_phone():
    while True:
        phone = input("Enter phone (10 digits): ").strip()
        if is_valid_phone(phone):
            return phone
        print("❌ Invalid phone number. Please enter exactly 10 digits.")

# Get valid email input
def input_valid_email():
    while True:
        email = input("Enter email: ").strip()
        if is_valid_email(email):
            return email
        print("❌ Invalid email format. Please enter a valid email (e.g. name@example.com).")

# Add a new contact
def add_contact():
    name = input("Enter name: ").strip()
    phone = input_valid_phone()
    email = input_valid_email()
    address = input("Enter address: ").strip()

    contacts = load_contacts()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print("✅ Contact added successfully!")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print(f"Name   : {contact['name']}")
        print(f"Phone  : {contact['phone']}")
        print(f"Email  : {contact['email']}")
        print(f"Address: {contact['address']}")

# Search contact by name
def search_contact():
    name = input("Enter name to search: ").strip().lower()
    contacts = load_contacts()
    found = [c for c in contacts if c['name'].lower() == name]
    if found:
        for contact in found:
            print(f"\nName   : {contact['name']}")
            print(f"Phone  : {contact['phone']}")
            print(f"Email  : {contact['email']}")
            print(f"Address: {contact['address']}")
    else:
        print("Contact not found.")

# Edit contact
def edit_contact():
    name = input("Enter name of contact to edit: ").strip().lower()
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Leave blank to keep current value.")
            new_name = input(f"New name ({contact['name']}): ").strip()
            new_phone = input(f"New phone ({contact['phone']}): ").strip()
            new_email = input(f"New email ({contact['email']}): ").strip()
            new_address = input(f"New address ({contact['address']}): ").strip()

            if new_phone:
                while not is_valid_phone(new_phone):
                    print("❌ Invalid phone number. Please enter exactly 10 digits.")
                    new_phone = input("New phone: ").strip()
            if new_email:
                while not is_valid_email(new_email):
                    print("❌ Invalid email format.")
                    new_email = input("New email: ").strip()

            contact['name'] = new_name or contact['name']
            contact['phone'] = new_phone or contact['phone']
            contact['email'] = new_email or contact['email']
            contact['address'] = new_address or contact['address']

            save_contacts(contacts)
            print("✅ Contact updated successfully!")
            return
    print("Contact not found.")

# Delete contact
def delete_contact():
    name = input("Enter name of contact to delete: ").strip().lower()
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c['name'].lower() != name]
    if len(new_contacts) == len(contacts):
        print("Contact not found.")
    else:
        save_contacts(new_contacts)
        print("✅ Contact deleted successfully!")

# Export contacts to CSV
def export_to_csv():
    contacts = load_contacts()
    if not contacts:
        print("No contacts to export.")
        return
    with open(CSV_FILE, 'w', newline='') as csvfile:
        fieldnames = ['name', 'phone', 'email', 'address']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)
    print(f"✅ Contacts exported to {CSV_FILE} successfully!")

# Main menu
def main():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Export to CSV")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            edit_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            export_to_csv()
        elif choice == '7':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
