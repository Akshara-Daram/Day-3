class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append({"name": name, "phone": phone})
        print("Contact added successfully.")

    def view_contacts(self):
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")

    def search_contacts(self, search_term):
        search_results = []
        for contact in self.contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                search_results.append(contact)
        
        print("Search results:")
        for i, result in enumerate(search_results, start=1):
            print(f"{i}. Name: {result['name']}, Phone: {result['phone']}")

contact_book = ContactBook()

while True:
    print("Choose an action:")
    print("1 - Add contact")
    print("2 - View contacts")
    print("3 - Search contacts")
    choice = input()
    
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contact_book.add_contact(name, phone)
    elif choice == '2':
        contact_book.view_contacts()
    elif choice == '3':
        search_term = input("Enter search term: ")
        contact_book.search_contacts(search_term)
    else:
        break
