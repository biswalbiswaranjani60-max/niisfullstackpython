max_size = 5
queue = [None] * max_size
front = -1
rear = -1

def enqueue():
    global front, rear
    if (front == 0 and rear == max_size - 1) or (front == rear + 1):
        print("Queue Overflow")
    else:
        element = input("Enter element: ")
        if front == -1:
            front = rear = 0
        else:
            rear = (rear + 1) % max_size
        queue[rear] = element
        print(element, "inserted")

def dequeue():
    global front, rear
    if front == -1:
        print("Queue Underflow")
    elif front == rear:
        print("Deleted element:", queue[front])
        front = rear = -1
    else:
        print("Deleted element:", queue[front])
        front = (front + 1) % max_size

def display():
    if front == -1:
        print("Queue is empty")
    else:
        print("Queue elements:")
        i = front
        while True:
            print(queue[i])
            if i == rear:
                break
            i = (i + 1) % max_size

while True:
    print("\n1.Enqueue  2.Dequeue  3.Display  4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")