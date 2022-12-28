class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

a= Node(1)
b = Node(2)
c = Node(3)
a.left, a.right = b,c
d, e = Node(4), Node(5)
f, g = Node(6), Node(7)
b.left, b.right = d,e
c.left, c.right = f,g



def inorderTraversal(root):
    res = []
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()  # the last element
        if node:
            if visited:
                res.append(node.val)
            else:  # inorder: left -> root -> right
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
    return res

def postorderTraversal(root):
    res = []
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()  # the last element
        if node:
            if visited:
                res.append(node.val)
            else:  # inorder: left -> root -> right
                stack.append((node.right, False))
                stack.append((node.left, False))
                stack.append((node, True))
    return res

def preorderTraversal(root):
    res = []
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()  # the last element
        if node:
            if visited:
                res.append(node.val)
            else:  # inorder: left -> root -> right
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
    return res

x = inorderTraversal(a)
print(x)
y = postorderTraversal(a)
print(y)
z = preorderTraversal(a)
print(z)
