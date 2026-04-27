# Queue implementation without OOP using front and rear

max_size = 5
queue = [None] * max_size
front = -1
rear = -1

# Enqueue operation6
def enqueue():
    global rear, front
    if rear == max_size - 1:
        print("Queue Overflow")
    else:
        element = input("Enter element to insert: ")
        if front == -1:
            front = 0
        rear = rear + 1
        queue[rear] = element
        print(element, "inserted into queue")

# Dequeue operation
def dequeue():
    global front
    if front == -1 or front > rear:
        print("Queue Underflow")
    else:
        print("Deleted element:", queue[front])
        front = front + 1

# Peek operation
def peek():
    if front == -1 or front > rear:
        print("Queue is empty")
    else:
        print("Front element:", queue[front])

# Display queue
def display():
    if front == -1 or front > rear:
        print("Queue is empty")
    else:
        print("Queue elements:")
        for i in range(front, rear + 1):
            print(queue[i])

# Main menu
while True:
    print("\n--- Queue Menu ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Exiting program")
        break
    else:
        print("Invalid choice")