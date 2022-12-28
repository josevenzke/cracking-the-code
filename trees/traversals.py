def get_tree():
    """
            1
        2       3
      4   5    6  7
    """
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    a= Node(1)
    b = Node(2)
    c = Node(3)
    a.left, a.right = b, c
    b.left, b.right = Node(4), Node(5)
    c.left, c.right = Node(6), Node(7)
    return a

#Iterative 

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

root = get_tree()

print(inorderTraversal(root))
print(postorderTraversal(root))
print(preorderTraversal(root))

#Recursive

def inorderTraversal(root):
    if root:
        return inorderTraversal(root.left) + [root.val] +inorderTraversal(root.right)
    else:
        return []

def postorderTraversal(root):
    if root:
        return postorderTraversal(root.left)+postorderTraversal(root.right)+[root.val]
    else:
        return []

def preorderTraversal(root):
    if root:
        return  [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)
    else:
        return []



root = get_tree()

print(inorderTraversal(root))
print(postorderTraversal(root))
print(preorderTraversal(root))