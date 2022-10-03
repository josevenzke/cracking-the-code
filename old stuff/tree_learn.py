class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def preorder(root):
  return [root.val] + preorder(root.left) + preorder(root.right) if root else []

def inorder(root):
  return  inorder(root.left) + [root.val] + inorder(root.right) if root else []

def postorder(root):
  return  postorder(root.left) + postorder(root.right) + [root.val] if root else []


class Solution:
    def inorderTraversal(self, root: TreeNode):
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

def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
 
        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
 
# Iterative Method to print the
# height of a binary tree
from collections import deque
 
def printLevelOrder(root):
    # Base Case
    if root is None:
        return
 
    # Create an empty queue
    # for level order traversal
    queue = deque()
 
    # Enqueue Root and initialize height
    queue.append(root)
 
    while(len(queue) > 0):
 
        # Print front of queue and
        # remove it from queue

        print([x.data for x in list(queue)])
        node = queue.popleft()
 
        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)
 
        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)
 
 
# Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.right.left = Node(7)

#        1
#     2    3
#    4 5  7  6 



 
print("Level Order Traversal of binary tree is -")
printLevelOrder(root)

#PREORDER
#visit
#left
#right

#INORDER
#left     right
#visit    visit
#right    left

#POSTORDER
#left
#right
#visit