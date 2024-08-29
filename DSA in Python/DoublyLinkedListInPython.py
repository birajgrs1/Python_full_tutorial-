class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL_Traverse:
    def __init__(self):
        self.head = None
        self.tail = None

    # Forward Traversal
    def printForwardTraversal(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.next
            print("None")

    # Backward Traversal
    def printBackwardTraversal(self):
        if self.tail is None:
            print("Linked list is empty!")
        else:
            n = self.tail
            while n is not None:
                print(n.data, "<---", end=" ")
                n = n.prev
            print("None")

    # Insertion in Doubly linked list

    def emptyInsertion(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
        else:
            print("Linked list is not empty!")

    # Add at beginning
    def add_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Add at end
    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.prev = n
            self.tail = new_node

    # Add after a specific node
    def add_after(self, data, x):
        if self.head is None:
            print("DLL is empty!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.next
            if n is None:
                print("Given node is not present in DLL.")
            else:
                new_node = Node(data)
                new_node.next = n.next
                new_node.prev = n
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node
                if new_node.next is None:
                    self.tail = new_node

    # Add before a specific node
    def add_before(self, data, x):
        if self.head is None:
            print("DLL is empty!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.next
            if n is None:
                print("Given node is not present in DLL.")
            else:
                new_node = Node(data)
                new_node.next = n
                new_node.prev = n.prev
                if n.prev is not None:
                    n.prev.next = new_node
                else:
                    self.head = new_node
                n.prev = new_node

# Creating the doubly linked list
print("\n ------------- \n")

ll1 = DLL_Traverse()

# Insert an element when list is empty
ll1.emptyInsertion(10)
ll1.printForwardTraversal()
ll1.printBackwardTraversal()

print("\n ------------- \n")
ll1.add_at_begin(20)
ll1.add_at_begin(30)

ll1.printForwardTraversal()
ll1.printBackwardTraversal()

print("\n ------------- \n")
ll1.add_at_end(40)
ll1.add_at_end(50)

ll1.printForwardTraversal()
ll1.printBackwardTraversal()

print("\n ------------- \n")
ll1.add_after(55, 30)
ll1.add_after(65, 40)

ll1.printForwardTraversal()
ll1.printBackwardTraversal()

print("\n ------------- \n")
ll1.add_before(15, 10)
ll1.add_before(25, 20)

ll1.printForwardTraversal()
ll1.printBackwardTraversal()
