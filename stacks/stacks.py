#Implementing a Stack:
class EmptyStack(Exception):
    pass


class StackNode:
    def __init__(self,data: int,next= None):
        self.data = data
        self.next = next
    
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
            node.next = self.top
            self.top = node
        else:
            self.top = node
            
    #peek
    def peek(self):
        if self.top:
            print(self.top.data)
        else:
            print('empty stack')
    #isempty
    def is_empty(self):
        return self.top == None

x = Stack()

x.push(1)
x.push(2)
x.push(3)
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