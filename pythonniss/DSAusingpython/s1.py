max_size = 5
stack = [None] * max_size
top = -1
def push():
    global top
    if top == max_size - 1:
        print("Stack Overflow")
    else:
        element = input("Enter element to push: ")
        top = top + 1
        stack[top] = element
        print(element, "pushed to stack")

def pop():
    global top
    if top == -1:
        print("Stack Underflow")
    else:
        print("Popped element:", stack[top])
        top = top - 1

def peek():
    if top == -1:
        print("Stack is empty")
    else:
        print("Top element:", stack[top])

def display():
    if top == -1:
        print("Stack is empty")
    else:
        print("Stack elements:")
        for i in range(top, -1, -1):
            print(stack[i])

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