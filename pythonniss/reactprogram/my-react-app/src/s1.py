# Stack implementation without OOP

stack = []

# Push operation
def push():
    element = input("Enter element to push: ")
    stack.append(element)
    print(element, "pushed to stack")

# Pop operation
def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Popped element:", stack.pop())

# Peek operation
def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])

# Display stack
def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements:", stack)

# Main menu
while True:
    print("\n--- Stack Menu ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Exiting program")
        break
    else:
        print("Invalid choice")