class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [None] * max_size
        self.top = -1

    # Push operation
    def push(self):
        if self.top == self.max_size - 1:
            print("Stack Overflow")
        else:
            element = input("Enter element to push: ")
            self.top += 1
            self.stack[self.top] = element
            print(element, "pushed to stack")

    # Pop operation
    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            print("Popped element:", self.stack[self.top])
            self.top -= 1

    # Peek operation
    def peek(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Top element:", self.stack[self.top])

    # Display stack
    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Stack elements:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])


# Create object
s = Stack(5)

# Menu-driven program
while True:
    print("\n--- Stack Menu ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        s.push()
    elif choice == 2:
        s.pop()
    elif choice == 3:
        s.peek()
    elif choice == 4:
        s.display()
    elif choice == 5:
        print("Exiting program")
        break
    else:
        print("Invalid choice")