## Simple calculator application
## This is a simple calculator application that performs basic arithmetic operations.
## function for addition
def add(x,y):
    return x+y
# function for subtraction
def subtract(x,y):
    return x-y
# function for multiplication
def multiply(x,y):
    return x*y
# function for division
def divide(x,y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
# function to display the menu
def display_menu():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
# function to get user input
def get_user_input():
    while True:
        try:
            choice = int(input("Enter choice (1/2/3/4/5): "))
            if choice in [1, 2, 3, 4, 5]:
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
# function to perform the selected operation
def perform_operation(choice):

    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return perform_operation(choice)

    if choice == 1:
        return add(x, y)
    elif choice == 2:
        return subtract(x, y)
    elif choice == 3:
        return multiply(x, y)
    elif choice == 4:
        return divide(x, y)
# Main function to run the calculator
def main():
    while True:
        display_menu()
        choice = get_user_input()
        if choice == 5:
            print("Exiting the calculator. Goodbye!")
            break
        result = perform_operation(choice)
        if result is not None:
            print(f"Result: {result}")
        print()  # Print a newline for better readability
if __name__ == "__main__":
    main()