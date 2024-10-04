# shopping_list_manager.py

import os

# Ensure file is not empty
if os.stat(__file__).st_size == 0:
    print("Error: The file is empty!")

# Function to display menu
def display_menu():
    print("\nShopping List Manager")  # Correct print statement
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

# Main function for managing shopping list
def main():
    # Initialize the shopping list as an array (list)
    shopping_list = []

    while True:
        # Call the display_menu function
        display_menu()

        # Try to capture user choice as a number
        try:
            choice = int(input("Choose an option (1-4): ").strip())
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue

        # Process the choice
        if choice == 1:
            # Add item
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")
        elif choice == 2:
            # Remove item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        elif choice == 3:
            # View the current shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("\nThe shopping list is empty.")
        elif choice == 4:
            # Exit
            print("Exiting Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
