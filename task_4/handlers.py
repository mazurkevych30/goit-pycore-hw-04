
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def show_all(contacts: dict) -> None :
    print("Contacts:")
    for name, phone in contacts.items():
        print(f"{name} - {phone}")


def show_phone(contacts: dict, name: str) -> str: 
    phone = contacts.get(name)
    if phone: 
        return f"{name} - {phone}"
    
    return f"{name} not found."


def change_contact(args: list, contacts: dict) -> str:
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Does not have a contact by name: {name}."
