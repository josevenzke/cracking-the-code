#3.1
#How to implement three stacks in a single array:


#3.2
#implement a stack that with addition of push and pop also has min as a O(1) operation
class Node:
    def __init__(self,val,min=None):
        self.val = val
        self.next = None
        self.min = min

class Stack:
    def __init__(self,top):
        self.top = Node(top,top)
    
    def push(self,val):
        new_node = Node(val)
        new_node.min = min(new_node.val,self.top.min)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.top:
            x = self.top
            self.top = self.top.next
            return x
    
    def min(self):
        if self.top:
            return self.top.min

    def print(self):
        curr = self.top
        while curr:
            print(curr.val)
            curr = curr.next
        return
    
#3.3
#Implement a set of stacks, where with a fixed size is exceeded a new stack is created, but order is maintained

class Node:
    def __init__(self,val,min=None):
        self.val = val
        self.next = None

class Stack:
    def __init__(self,capacity,top=None):
        if top:
            self.top = Node(top)
        else:
            self.top = None
        self.capacity = capacity
        self.size = 1

    def push(self,val):
        if not self.top:
            self.top = Node(val)
            return
        if self.capacity == self.size:
            return False
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
        self.size+=1

    def pop(self):
        if self.top:
            x = self.top
            self.top = self.top.next
            self.size -=1
            return x
    
    def is_full(self):
        return self.capacity == self.size

    def print(self):
        curr = self.top
        x = ''
        while curr:
            x += str(curr.val) + "->"
            curr = curr.next
        print(x)

class SetOfStacks:
    def __init__(self,capacity):
        self.capacity = capacity
        self.stacks = [Stack(capacity)]
    
    def push(self,val):
        if self.stacks[-1].is_full():
            self.stacks.append(Stack(self.capacity,val))
        else:
            self.stacks[-1].push(val)
    
    def pop(self):
        x = self.stacks[-1].pop()
        if self.stacks[-1].size ==0:
            self.stacks.pop()
        return x
    
    def popAt(self,index):
        return self.stacks[index].pop()

    def print(self):
        for i in self.stacks:
            i.print()

#3.4
#Implement a queue with two stacks
# -> [5,4,3,2,1] - >

class MyQueue:
    def __init__(self):
        self.stack = []
        self.popstack = []
    
    def push(self,num):
        self.stack.append(num)
        return True
    
    def pop(self):
        if self.popstack:
            return self.popstack.pop()
        for i in range(1,len(self.stack)+1):
            self.popstack.append(self.stack[-i])
        self.stack = []
        return self.popstack.pop()
    
    def print(self):
        if not self.popstack:
            print(self.stack)
            return
        print(self.popstack[::-1],self.stack)
    
    def test(self):
        x = MyQueue()
        for i in range(1,6):
            x.push(i)

        x.print()
        x.pop()
        x.pop()
        x.push(6)
        x.push(7)
        x.push(8)
        x.print()
        x.pop()
        x.pop()
        x.pop()
        x.pop()
        x.print()

#3.5
#Write a program to sort a stack, you can use a additional temporary stack but no arrays, only push,pop,peek are usable, smallest items on top
def sort_stack(s):
    r = []
    while s:
        tmp = s.pop()
        while r and r[-1]>tmp:
            s.append(r.pop())
        r.append(tmp)
    while r:
        s.append(r.pop())

#3.6
#Animal Shelter, write a class that returns the oldest dog,cat or any animal
class Node():
    def __init__(self,val,pos) -> None:
        self.val = val
        self.pos = pos
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        
    def enqueue(self,val,pos):
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(val,pos)
        else:
            self.head = Node(val,pos)
        return True
    
    def deque(self):
        if self.head:
            temp = self.head
            self.head = self.head.next
            return temp
        else:
            return False

    def peek(self):
        return self.head

    def print(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next

class Animal:
    def __init__(self,name,breed) -> None:
        self.name = name
        self.breed = breed
        
class Shelter:
    def __init__(self):
        self.cats = LinkedList()
        self.dogs = LinkedList()
        self.pos = 0
    
    def addAnimal(self,animal):
        if animal.breed == 'dog':
            self.dogs.enqueue(animal,self.pos)
        else:
            self.cats.enqueue(animal,self.pos)
        self.pos +=1
    
    def adoptDog(self):
        return self.dogs.deque()
    
    def adoptCat(self):
        return self.cats.deque()
    
    def adoptAny(self):
        cat_pos = self.cats.peek().pos
        dog_pos = self.dogs.peek().pos
        return self.cats.deque() if cat_pos<dog_pos else self.dogs.deque()

    def teste(self):
        a = Animal("a","dog")
        b = Animal("b","dog")
        c = Animal("c","cat")
        d = Animal("d","cat")

        x = Shelter()
        x.addAnimal(a)
        x.addAnimal(b)
        x.addAnimal(c)
        x.addAnimal(d)


        print(x.adoptCat().val.name)
        print(x.adoptDog().val.name)
        print(x.adoptDog().val.name)
        print(x.adoptAny().val.name)
        print(x.adoptDog().val.name)


