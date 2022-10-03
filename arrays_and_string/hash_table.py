import random, string

class HashTable:
    def __init__(self,size):
        self.array = [LinkedList()]*size


    def __setitem__(self,key,val):
        index = self._hash(key)
        self.array[index].append(key,val)

    def __getitem__(self,key):
        index = self._hash(key)
        item = self.array[index].search(key)
        return item
        
    def _hash(self,key):
        h = 0
        for char in key:
            h+=ord(char)
        return h%100


class Node:
    def __init__(self,key:int,val: int):
        self.key = key
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self,head=None):
        self.head = head
    
    def append(self,key,val)-> None:
        if not self.head:
            self.head = Node(key,val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(key,val)

    def search(self,key):
        curr = self.head
        while curr:
            if curr.key == key:
                return curr.val
            curr=curr.next
        return None


ht = HashTable(100)

ht['a'] = 1
ht['b'] = 2
ht['c'] = 3
ht['d'] = 4
ht['e'] = 5
ht['9PHR'] = 10
ht['BUEG'] = 11

print(ht['a'])
print(ht['b'])
print(ht['e'])
print(ht['9PHR'])
print(ht['BUEG'])


def teste(key):
    h = 0
    for char in key:
        h+=ord(char)
    hashed = h%100
    if seen.get(hashed):
        print(key, seen[hashed])
        return True
    seen[hashed] = key
    return False

def testing():
    seen = {}
    x= True
    while x:
        if teste(''.join(random.choices(string.ascii_uppercase + string.digits, k=4))):
            x = False



