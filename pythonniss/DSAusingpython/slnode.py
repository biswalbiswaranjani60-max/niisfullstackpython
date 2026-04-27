class Node:
    def __init__(self, ele):
        self.data = ele
        self.next = None

# Function to create n nodes
def create_list(n):
    head = None

    for i in range(n):
        data = int(input("Enter data: "))
        curr = Node(data)

        if head is None:
            head = curr
        else:
            ptr.next = curr

        ptr = curr   # move pointer

    return head

# Function to display list
def display(head):
    ptr = head
    while ptr is not None:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
    print("NULL")

# Main
n = int(input("Enter number of nodes: "))
head = create_list(n)

print("Linked List:")
display(head)