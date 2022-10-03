class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self,head):
        self.head = head
    
    def append(self,val):
        head = self.head
        while head.next:
            head = head.next
        head.next = Node(val)
    
    def push(self,val):
        x = Node(val,self.head)
        self.head = x

    def remove(self,val):
        head = self.head
        old = head
        while head:
            if head.val == val:
                old.next = head.next
            old = head
            head = head.next

    def invert(self):
        curr = self.head
        prev = None
        nxt = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def to_string(self):
        s = ''
        head = self.head
        while head:
            s+= str(head.val)+"-->"
            head = head.next
        return s

x = LinkedList(Node(5))
print(x.to_string())
x.append(10)
x.append(16)
print(x.to_string())
x.push(1)
x.append(23)
print(x.to_string())
x.invert()
print(x.to_string())
x.remove(23)
x.remove(1)
x.remove(10)
print(x.to_string())

