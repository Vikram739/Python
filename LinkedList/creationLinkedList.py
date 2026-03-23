# this program show's how to create linkedlist...

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        



# creating linked list nodes...
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)


#connecting nodes...
node1.next = node2
node2.next = node3
node3.next = node4

# setting head 
head = node1
# traversing linkedlist...
current = head

while current:
    print(current.data, end='->')
    current = current.next
print("None")  

