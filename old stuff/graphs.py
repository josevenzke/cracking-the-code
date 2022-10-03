#A graph is a simple collection of nodes with edges between some of them
#Graphs can be either direceted or undirected, directed = one way - undirected = both ways
#A tree is a aciclyc graph

class Graph:
    def __init__(self) -> None:
        self.nodes = []

    def add(self,node):
        self.nodes.append(node)

class Node:
    def __init__(self,name) -> None:
        self.name = name
        self.adjacent = []
        self.visited = False

    def add(self,node):
        self.adjacent.append(node)

x = Node(1)
x.add(Node(2))
x.adjacent[0].add(Node(3))
x.add(Node(4))
x.adjacent[1].add(Node(5))
x.add(Node(6))
x.add(Node(7))
x.add(Node(8))


def visit(node):
    print(node.name)

#DFS:
#DFS is the same as tree in/pre/post order traversals, but in graphs we need to keep track of visited nodes so we do not end up in a cycle

def dsearch(node):
    visit(node)
    node.visited = True
    for n in node.adjacent:
        if not n.visited:
            dsearch(n)

#BFS:

def bsearch(node):
    queue = []
    node.visited = True
    queue.append(node)

    while queue:
        r = queue.pop(0)
        visit(r)
        for n in r.adjacent:
            n.visited = True
            queue.append(n)

dsearch(x)
print('-----')
bsearch(x)

#4.1 Route Between Nodes:

x = Node(1)
x.add(Node(2))
x.adjacent[0].add(Node(3))
y = Node(5)
x.adjacent[0].adjacent[0].add(y)
x.add(Node(6))
x.add(Node(7))
x.add(Node(8))


def isConnected(node1,node2):
    q = [node1]
    while q:
        print(q,node2.name)
        x = q.pop(0)
        x.visited = True
        if x.name == node2.name:
            return True
        for n in x.adjacent:
            if not n.visited:
                q.append(n)
    return False


print(isConnected(x,Node(10)))
