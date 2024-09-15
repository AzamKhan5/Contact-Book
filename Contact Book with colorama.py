import os
from colorama import Fore, Style, init

# Initialize Colorama
init()

# Data storage for contacts
names = ["John", "Doe", "Alex", "Jim"]
numbers = [9825844310, 9875423681, 7854690314, 8945061293]

# Function to display the menu
def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''
    {Fore.CYAN}-----------------Contact Manager-----------------{Style.RESET_ALL}
    {Fore.YELLOW}Press 1 to store a new contact
    Press 2 to search for a contact
    Press 3 to update a contact
    Press 4 to delete a contact
    Press 5 to show all contacts
    Press 0 to exit the program{Style.RESET_ALL}
    {Fore.CYAN}--------------------------------------------------{Style.RESET_ALL}
    ''')

# Function to store a new contact
def store_contact():
    name = input(f"{Fore.GREEN}Enter Name: {Style.RESET_ALL}").title()
    try:
        number = int(input(f"{Fore.GREEN}Enter Number: {Style.RESET_ALL}"))
    except ValueError:
        print(f"{Fore.RED}Invalid number input! Please enter a valid number.{Style.RESET_ALL}")
        return

    if name in names:
        print(f"{Fore.RED}{name} already exists. Try with a different name.{Style.RESET_ALL}")
    elif number in numbers:
        print(f"{Fore.RED}{number} is already assigned. Try with a different number.{Style.RESET_ALL}")
    else:
        names.append(name)
        numbers.append(number)
        print(f"{Fore.GREEN}Contact saved successfully.{Style.RESET_ALL}")

# Function to search for a contact
def search_contact():
    print(f'''
    {Fore.YELLOW}Press A to search by Name
    Press B to search by Number{Style.RESET_ALL}
    ''')
    choice = input(f"{Fore.GREEN}Enter choice: {Style.RESET_ALL}").upper()

    if choice == 'A':
        name = input(f"{Fore.GREEN}Enter name to search: {Style.RESET_ALL}").title()
        if name in names:
            idx = names.index(name)
            print(f"{Fore.GREEN}Contact Number of {name}: {numbers[idx]}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Name '{name}' not found.{Style.RESET_ALL}")
    
    elif choice == 'B':
        try:
            number = int(input(f"{Fore.GREEN}Enter number to search: {Style.RESET_ALL}"))
        except ValueError:
            print(f"{Fore.RED}Invalid number input! Please enter a valid number.{Style.RESET_ALL}")
            return

        if number in numbers:
            idx = numbers.index(number)
            print(f"{Fore.GREEN}{names[idx]} is the owner of {number}.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Number '{number}' not found.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Invalid choice. Please enter A or B.{Style.RESET_ALL}")

# Function to update a contact
def update_contact():
    name = input(f"{Fore.GREEN}Enter current name of the contact: {Style.RESET_ALL}").title()
    if name in names:
        idx = names.index(name)
        print(f"{Fore.YELLOW}Current contact: {name}, {numbers[idx]}{Style.RESET_ALL}")
        new_name = input(f"{Fore.GREEN}Enter new name: {Style.RESET_ALL}").title()
        names[idx] = new_name
        print(f"{Fore.GREEN}Contact updated: {new_name}, {numbers[idx]}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Name '{name}' not found.{Style.RESET_ALL}")

# Function to delete a contact
def delete_contact():
    print(f'''
    {Fore.YELLOW}Press A to delete by Name
    Press B to delete by Number{Style.RESET_ALL}
    ''')
    choice = input(f"{Fore.GREEN}Enter choice: {Style.RESET_ALL}").upper()

    if choice == 'A':
        name = input(f"{Fore.GREEN}Enter name to delete: {Style.RESET_ALL}").title()
        if name in names:
            idx = names.index(name)
            names.pop(idx)
            numbers.pop(idx)
            print(f"{Fore.GREEN}Contact '{name}' deleted successfully.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Name '{name}' not found.{Style.RESET_ALL}")
    
    elif choice == 'B':
        try:
            number = int(input(f"{Fore.GREEN}Enter number to delete: {Style.RESET_ALL}"))
        except ValueError:
            print(f"{Fore.RED}Invalid number input! Please enter a valid number.{Style.RESET_ALL}")
            return

        if number in numbers:
            idx = numbers.index(number)
            names.pop(idx)
            numbers.pop(idx)
            print(f"{Fore.GREEN}Contact with number {number} deleted successfully.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Number '{number}' not found.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Invalid choice. Please enter A or B.{Style.RESET_ALL}")

# Function to display all contacts
def show_contacts():
    if not names and not numbers:
        print(f"{Fore.RED}Contact list is empty.{Style.RESET_ALL}")
    else:
        print(f"{Fore.CYAN}--------------- Contact List ---------------{Style.RESET_ALL}")
        for name, number in zip(names, numbers):
            print(f"{Fore.YELLOW}{name:20} : {number}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}--------------------------------------------{Style.RESET_ALL}")

# Main loop
while True:
    display_menu()
    try:
        choice = int(input(f"{Fore.GREEN}Enter your choice: {Style.RESET_ALL}"))
    except ValueError:
        print(f"{Fore.RED}Invalid input! Please enter a number.{Style.RESET_ALL}")
        continue

    if choice == 0:
        print(f"{Fore.GREEN}Exiting program...{Style.RESET_ALL}")
        break
    elif choice == 1:
        store_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        update_contact()
    elif choice == 4:
        delete_contact()
    elif choice == 5:
        show_contacts()
    else:
        print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")
    
    input(f"\n{Fore.GREEN}Press Enter to continue...{Style.RESET_ALL}")  # Pause before returning to the menu





