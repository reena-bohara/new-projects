from LinkedList_Node import Node

def deleteNthNodeFromEnd(head, n):
    k = 0
    curr = head

    while curr:
        curr = curr.next
        k += 1

    if k - n == 0:
        return head.next
    curr = head
    for _ in range(1,k-n):
        curr = curr.next

    curr.next = curr.next.next


    return head
if    __name__ ==  "__main__":
    head = Node(4)
    head.next = Node(8)
    head.next.next = Node(12)
    head.next.next.next = Node(16)
    head.next.next.next.next = Node(20)

    head = deleteNthNodeFromEnd(head,3)

    curr = head
    while curr:
        print(curr.data,end="->")
        curr = curr.next