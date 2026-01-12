# list manager
# program allows the user to manage a list of items
# users can add, remove, and view items in the list

items = []
#initalize an empty list

while True:
    print("\nList Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Items")
    print("4. Exit")
#Menu loop - allowing the menu to loop until the user decides to exit

    choice = input("Enter choice (1-4):")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please try again.")
        continue
    #input validation: check if choice is one of the allowed options

    if choice == '1':
        new_item = input("Enter item to add:  ").strip()
        if new_item: #check that the input is not empty
            items.append(new_item)
            print(f'"{new_item}" has been added to the list.')
        else:
            print("You cannot add an empty item.")

    elif choice == '2':
        if not items:
            print("The list is empty. Nothing to remove.")
        else:
            remove_item = input("Enter item to remove: ").strip()
            if remove_item in items:
                items.remove(remove_item)
                print(f'"{remove_item}" has been removed from the list.')
            else:
                print(f'"{remove_item}" not found in the list.')

    elif choice == '3':
        if not items:
            print("The list is empty.")
        else:
            print("\n Current items:")
            #Using a loop to display items with their index
            for idx, item in enumerate(items, start=1):
                print(f"{idx}. {item}")

    elif choice == '4':
        print("List Manager exiting. Thank you!")
        break