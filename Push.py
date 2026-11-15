stack = []

def push():
    element = int(input("Enter element to push: "))
    stack.append(element)
    print(element, "inserted into stack")

def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements:", stack)


# Main program
while True:
    print("\n1. Push")
    print("2. Display")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()

    elif choice == 2:
        display()

    elif choice == 3:
        print("Program ended")
        break

    else:
        print("Invalid choice")
