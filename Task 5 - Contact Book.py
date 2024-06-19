from streamlit import *
from pandas import *

# Initialize the contact book if not already present
if 'contacts' not in session_state:
    session_state.contacts = []

# Function to add a new contact
def add_contact(name, phone, email, address):
    contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
    session_state.contacts.append(contact)

# Function to search for contacts by name or phone number
def search_contact(query):
    return [contact for contact in session_state.contacts if query.lower() in contact["Name"].lower() or query.lower() in contact["Phone"].lower()]

# Function to update a contact
def update_contact(index, name, phone, email, address):
    session_state.contacts[index] = {"Name": name, "Phone": phone, "Email": email, "Address": address}

# Function to delete a contact
def delete_contact(index):
    del session_state.contacts[index]

def main():
    title("Contact Book")
    
    menu = ["Add Contact", "View Contacts", "Search Contact", "Update Contact", "Delete Contact"]
    choice = sidebar.selectbox("Menu", menu)
    
    if choice == "Add Contact":
        subheader("Add New Contact")
        name = text_input("Name")
        phone = text_input("Phone")
        email = text_input("Email")
        address = text_input("Address")
        
        if button("Add Contact"):
            add_contact(name, phone, email, address)
            success(f"Contact {name} added successfully")
    
    elif choice == "View Contacts":
        subheader("View Contacts")
        if session_state.contacts:
            contacts_df = DataFrame(session_state.contacts)
            table(contacts_df)
        else:
            info("No contacts found")
    
    elif choice == "Search Contact":
        subheader("Search Contact")
        query = text_input("Search by name or phone number")
        if button("Search"):
            results = search_contact(query)
            if results:
                results_df = DataFrame(results)
                table(results_df)
            else:
                info("No contacts found")
    
    elif choice == "Update Contact":
        subheader("Update Contact")
        contact_names = [contact["Name"] for contact in session_state.contacts]
        selected_contact = selectbox("Select contact to update", contact_names)
        index = contact_names.index(selected_contact)
        contact = session_state.contacts[index]
        
        name = text_input("Name", contact["Name"])
        phone = text_input("Phone", contact["Phone"])
        email = text_input("Email", contact["Email"])
        address = text_input("Address", contact["Address"])
        
        if button("Update Contact"):
            update_contact(index, name, phone, email, address)
            success(f"Contact {name} updated successfully")
    
    elif choice == "Delete Contact":
        subheader("Delete Contact")
        contact_names = [contact["Name"] for contact in session_state.contacts]
        selected_contact = selectbox("Select contact to delete", contact_names)
        index = contact_names.index(selected_contact)
        
        if button("Delete Contact"):
            delete_contact(index)
            success(f"Contact {selected_contact} deleted successfully")

if __name__ == "__main__":
    main()