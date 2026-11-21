stack = []

# Push function
def push():
    n = int(input("Enter element to push: "))
    stack.append(n)
    print(n, "inserted into stack")

# Pop function
def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Deleted element:", stack.pop())

# Display function
def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements:", stack)

# Main program
while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
