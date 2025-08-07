from LinkedList_Node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:  #if value exist then True if null or none value then False (in this line we will check the value of head is none or not)
            self.head = new_node
        else:
            current = self.head 
            while current.next:
                current = current.next
            current.next = new_node


    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



#Example 1: Append integers
sll = SinglyLinkedList()
for i in [1,2,3,4]:
    sll.append(i)
sll.display()


#Example 2: append strings
sll2 = SinglyLinkedList()
for word in ["hello", "linked", "list"]:
    sll2.append(word)
sll2.display()


#Example 3: mixed data
sll3 = SinglyLinkedList()
for item in [True, 3.14, "node"]:
    sll3.append(item)
sll3.display()


#Example 4: Display empty list
sll4 = SinglyLinkedList()
sll4.display()