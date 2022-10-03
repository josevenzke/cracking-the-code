class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Linkedlist:
    def __init__(self,val):
        self.head=Node(val)
    
    def appendToTail(self,val):
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
    
    def deleteNode(self,val):
        if self.head == val:
            self.head = self.head.next
            return 
        curr = self.head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                return
            curr = curr.next

#Runner technique

        