from operator import truediv


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
    def printList(self):
        curr = self.head
        vals = []
        while curr.next:
            vals.append(curr.val)
            curr = curr.next
        vals.append(curr.val)
        print(vals)


x = Linkedlist(3)
x.appendToTail(5)
x.appendToTail(8)
x.appendToTail(5)
x.appendToTail(10)
x.appendToTail(2)
x.appendToTail(1)

x.printList()


#2.1 Remove Dups: write code to remove duplicates from a linked list
def remove_dups(ll):
    curr = ll.head
    seen = {curr.val: True}
    while curr.next:
        if curr.next.val in seen:
            curr.next = curr.next.next
        else:
            seen[curr.val] = True
            curr = curr.next
    return 

def teste():
    remove_dups(x)
    x.printList()
    x.appendToTail(3)
    x.appendToTail(3)
    x.appendToTail(3)
    x.appendToTail(3)
    x.appendToTail(3)
    x.appendToTail(4)
    x.appendToTail(3)

    remove_dups(x)
    x.printList()

#2.2 Return kth to last:
def kth_last(ll,k):
    p1 = ll.head
    p2 = ll.head
    for i in range(k):
        if p1:
            p1 = p1.next
        else:
            return False
    while p1:
        p1 = p1.next
        p2 = p2.next
    print(p2,p2.val)

def teste():
    x.printList()
    kth_last(x,3)
    kth_last(x,1)
    kth_last(x,4)
    kth_last(x,5)
    kth_last(x,0)

#2.3 Delete the middle element of a linked_list
def del_mid_element(ll):
    prev = slow = fast = ll.head
    while fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
        print(slow.val, fast.val)
    prev.next = prev.next.next

def teste():
    del_mid_element(x)
    x.printList()
    del_mid_element(x)
    x.printList()

#2.4 Partition: Write code to partition a linked list aoround a value x
# Ex:
# 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 (partition: 5)
# 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

def partition(ll,x):
    curr = ll.head
    while curr.next:
        curr = curr.next
    last = curr
    curr = ll.head
    if curr.val >= x:
        last.next = curr
        ll.head = curr.next
        curr.next = None
        last = last.next
    while curr.next.next:
        print(curr.next.val)
        if curr.next.val >= x:
            last.next = curr.next
            curr.next = curr.next.next
            print(curr.val, '-->',curr.next.val)
            print(last.val)
            last = last.next
            last.next = None
            print(last.val, last.next)
        else:
            ll.printList()
            curr = curr.next

def teste():
    partition(x,8)
    x.printList()


#2.5 Sum Lists: Sum two lists(they are in reversed order)
# (7 -> 1 -> 6) + (5 -> 9 -> 2) This is 617+295
# = (2 -> 1 -> 9)

def add_lists(l1,l2,carry=0):
    pass

def teste():
    x.printList()
    d = add_lists(x.head,x.head)
    print(d)

teste()
#2.6 Is Palindrome: Check if LL is a palindrome
# Reverse a LL and then compare it
def is_palindrome(ll):
    curr = ll.head
    last = Node(curr.val)
    while curr:
        node = Node(curr.val)
        node.next = last
        last = node
        curr = curr.next
    curr = ll.head
    while node.next:
        if node.val != curr.val:
            return False
        node = node.next
        curr = curr.next
    return True

def teste():
    d = Linkedlist(1)
    d.appendToTail(2)
    d.appendToTail(3)
    d.appendToTail(2)
    d.appendToTail(1)
    print(is_palindrome(d))
    d = Linkedlist(1)
    d.appendToTail(2)
    d.appendToTail(2)
    d.appendToTail(1)
    print(is_palindrome(d))
    d = Linkedlist(1)
    d.appendToTail(2)
    d.appendToTail(3)
    d.appendToTail(4)
    print(is_palindrome(d))


#2.7: Has Intersection: Define if two single linked lists intersect with one another (basically share de same node)
def has_intersection(ll1: Linkedlist,ll2: Linkedlist):
    curr1= ll1.head
    curr2= ll2.head
    seen = {}
    while curr1.next:
        if curr1 in seen:
            return True
        seen[curr1] = True
        curr1 = curr1.next
    while curr2.next:
        if curr2 in seen:
            return True
        seen[curr2] = True
        curr2 = curr2.next
    return False

def teste():
    x = Linkedlist(1)
    t = Node(2)
    d = Node(3)
    y = Node(4)
    v = Node(5)
    z = Node(6)
    x.head.next = t
    t.next = d
    bb = Linkedlist(2)
    bb.head.next = y
    y.next = v
    print(has_intersection(x,bb))
    v.next = d
    d.next = z
    print(has_intersection(x,bb))

#2.8: Loop detection, check if a ll is cyclic (the last node points back to some other node)

def has_cycle(ll):
    slow = fast = ll.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            return True
    return False

#2.8.2: Loop detection, check if a ll is cyclic and return the node that is the beginning of the cycle
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 4

def has_cycle_n(ll):
    slow = fast = ll.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            break
    if not fast or not fast.next:
        return False
    slow = ll.head
    while slow!=fast:
        slow = slow.next
        fast = fast.next
    return fast 

def teste():
    x = Linkedlist(1)
    t = Node(2)
    d = Node(3)
    y = Node(4)
    v = Node(5)
    z = Node(6)
    x.head.next = t
    t.next = d
    d.next = y
    y.next = v
    x.printList()
    print(has_cycle(x))
    print(has_cycle_n(x))

    v.next = d
    print(has_cycle(x))
    print(has_cycle_n(x).val)


#2.9 Reverse a linked list:
# a -> b -> c -> d
# d -> c -> b -> a

def reverse_ll(ll):
    curr = ll.head
    prev = None
    while curr:
        next = curr.next 
        curr.next = prev 
        prev = curr
        curr = next

    ll.head = prev

def teste():
    reverse_ll(x)
    x.printList()

teste()