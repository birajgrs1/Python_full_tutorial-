class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

# Traversal in singly linked list
class LinkedListTraverse:
    def __init__(self):
        self.head = None  # head is starting point of Linked List

    def Print(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n = n.link

#     Inserting at the beginning of the linked list

    def add_at_begin(self,data):
        new_node = Node(data)
        new_node.link=self.head   # First node of linked list now
        self.head=new_node

# Inserting at the end of linked list

    def add_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.link is not None:
                n=n.link
            n.link=new_node

#  Insertion at a Specific Position of the Singly Linked List
    def  add_at_specific_position(self,data,val):
        n = self.head

        while n is not None:
            if val == n.data:
                break
            n=n.link

        if n is None:
            print("Node is not present in Linked List!!!")
        else:
            new_node=Node(data)
            new_node.link = n.link
            n.link=new_node

#  Deletion at the Beginning of Singly Linked List

    def delete_at_begin(self):
        if self.head is None:
            print("Linked list is empty!!!")
        else:
            self.head = self.head.link

# Deletion at the End of Singly Linked List

    def delete_at_the_end(self):
        if self.head is None:
            print("Linked list is empty!!!")
        else:
    #  Goto 2nd last node and change link to none
            n = self.head
            while n.link.link  is not None:
                n=n.link
            n.link=None

#  Deletion at a Specific Position of Singly Linked List

    def delete_at_a_specific_position(self,val):
        if self.head is None:
            print("Linked list is empty!!!")
            return
        if val == self.head.data:
            self.head= self.head.link
            return

        n=self.head
        while n.link is not None:
            if val== n.link.data:
                break
            n=n.link
        if n.link is None:
            print("Node is not present !!!")
        else:
            n.link=n.link.link


'''
LL1=LinkedListTraverse()
# LL1.Print()

LL1.head = Node(10)
second = Node(20)
third = Node(30)

LL1.head.link = second
second.link = third

LL1.Print()

'''
# Insertion
# Inserting add_at_beginning
LL1=LinkedListTraverse()
LL1.add_at_begin(10)
LL1.add_at_begin(20)
LL1.add_at_begin(30)

LL1.Print()
print("\n")
# Inserting add_at_end
LL1.add_at_end(50)
LL1.Print()

print("\n")
# Inserting at specific position
LL1.add_at_specific_position(100,20)
LL1.add_at_specific_position(200,100)
LL1.add_at_specific_position(300,200)



LL1.Print()

print("\n")
# Deletion
# Delete add_at_beginning
LL1.delete_at_begin()
LL1.Print()

print("\n")
# Delete at the end
LL1.delete_at_the_end()

LL1.Print()

print("\n")

# Delete at a specific position
LL1.delete_at_a_specific_position(300)


LL1.Print()

