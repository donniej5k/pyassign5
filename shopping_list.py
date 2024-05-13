#2. The Shopping List Maker

#Objective:
#The aim of this assignment is to create a program that helps users make a shopping list.

#Task 1: Write a function that lets the user add items to a list.
#Task 2: Include a feature to remove items from the list.
#Task 3: Add a function that prints out the entire list in a formatted way.


# Task 1 Function to add items to the shopping list
def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"Added '{item}' to the shopping list.")

# Task 2 Function to remove items from the shopping list
def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed '{item}' from the shopping list.")
    else:
        print(f"'{item}' is not in the shopping list.")

# Task 3 Function to print the entire shopping list
def print_list(shopping_list):
    if shopping_list:
        print("Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Your shopping list is empty.")

# Main function
def main():
    shopping_list = []
    while True:
        print("\nOptions:")
        print("1. Add item to shopping list")
        print("2. Remove item from shopping list")
        print("3. Print shopping list")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(shopping_list, item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(shopping_list, item)
        elif choice == '3':
            print_list(shopping_list)
        elif choice == '4':
            print("Thank you for using the shopping list program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Entry point of the program
if __name__ == "__main__":
    main()
