from dataclasses import dataclass


class Node:
    def __init__(self, data: int,next:object = None) -> None:
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    
    def add(self,val:int):
        node = Node(val)
        if not self.first:
            self.first = node
        else:
            self.last.next = node
        self.last = node
    
    def remove(self):
        if not self.first:
            raise Exception
        tmp = self.first
        self.first = self.first.next
        if not self.first:
            self.last = None
        print('removed -> ',tmp.data)
        return tmp

    def peek(self):
        if self.first:
            print(self.first.data)

    def is_empty(self):
        print(self.first == None)

def teste():
    x = Queue()

    x.add(1)
    x.add(2)
    x.add(3)
    x.add(4)
    x.add(5)

    x.peek()
    x.remove()

    x.peek()
    x.remove()

    x.is_empty()

    x.peek()
    x.remove()

    x.peek()
    x.remove()

    x.peek()
    x.remove()

    x.is_empty()

