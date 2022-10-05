#Implementing a Stack:
class EmptyStack(Exception):
    pass


class StackNode:
    def __init__(self,data: int,next= None):
        self.data = data
        self.next = next
        self.min = data
    
class Stack:
    def __init__(self,node: StackNode = None):
        self.top = node
    
    #pop
    def pop(self):
        print(self.top)
        if not self.top:
            raise EmptyStack
        node = self.top
        self.top = self.top.next
        return node
    #push
    def push(self,val):
        node = StackNode(val)
        if self.top:
            node.min = min(self.top.min,node.min)
        node.next = self.top
        self.top = node

    def min(self):
        print(self.top.min)
    
    #peek
    def peek(self):
        if self.top:
            print(self.top.data)
        else:
            print('empty stack')
    #isempty
    def is_empty(self):
        return self.top == None

def teste():
    x = Stack()

    x.push(3)
    x.push(4)
    x.min()
    x.push(5)
    x.min()
    x.push(2)
    x.min()
    x.push(1)
    x.min()
    x.pop()
    x.pop()
    x.min()
    x.peek()
    x.pop()
    x.peek()
    x.pop()
    x.peek()
    x.is_empty()
    x.pop()
    x.is_empty()
    x.peek()
    x.pop()


#3.3 Stack of Plates: implement a set of stacks

class StackNode:
    def __init__(self,data: int,next= None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self,capacity=100):
        self.capacity = capacity
        self.size = 0 
        self.top = None


    def push(self,data) -> None:
        node = StackNode(data)
        node.next = self.top
        self.top = node
        self.size+=1
    
    def pop(self)-> StackNode:
        if self.is_empty():
            raise EmptyStack
        tmp = self.top
        self.top = self.top.next
        self.size -=1
        return tmp
    
    def is_full(self):
        return self.capacity == self.size
    
    def is_empty(self):
        return self.top == None

class SetOfStacks:
    def __init__(self,capacity):
        self.capacity = capacity
        self.stacks = Stack()
        self.stacks.push(Stack(self.capacity))

    def push(self,val):
        stack = self.stacks.top.data
        if stack.is_full():
            stack = self._add_stack()
        stack.push(val)

    def pop(self):
        stack = self.stacks.top.data
        stack.pop()
        if stack.is_empty():
            stack = self._remove_stack()
    
    def peek(self):
        stack = self.stacks.top.data
        print(stack.top.data)

    def pop_at(self,index):
        curr_idx = 0
        stack = self.stacks.top
        while stack:
            if curr_idx == index:
                return stack.data.pop()
            stack = stack.next
            curr_idx+=1
        print('out of range')

    def _add_stack(self):
        print('added new stack')
        self.stacks.push(Stack(self.capacity))
        return self.stacks.top.data
    
    def _remove_stack(self):
        print('removed empty stack')
        self.stacks.pop()
        return self.stacks.top.data

x = SetOfStacks(5)

x.push(1)
x.push(2)
x.push(3)
x.push(4)
x.peek()
x.push(5)
x.peek()
x.push(6)
x.push(7)
x.pop_at(1)
x.pop()
x.pop()
x.peek()
