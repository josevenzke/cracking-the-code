#Tree
class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.children = []

class Tree:
    def __init__(self,head):
        self.head = head


#Bynary Tree

#Complete binary three: filled in all levels, except the last one(if its full from left to right then its a full three otherwise it isnt)
#Full binary three: every node has either 0 or 2 children node
class BinaryNode:
    def __init__(self, val): 
        self.val = val  
        self.left = None  
        self.right = None 


    def __str__(self):
        return str(self.val) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def add(self, val):  
        if self.root == None:
            self.root = BinaryNode(val)
        else:
            current = self.root
         
            while True:
                if val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = BinaryNode(val)
                        break
                elif val > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = BinaryNode(val)
                        break
                else:
                    break
    
    def hasNum(self,val):
        if not self.root:
            return False
        curr = self.root
        while True:
            if curr.val == val:
                return True
            if val > curr.val:
                if curr.right:
                    curr= curr.right
                else:
                    return False
            elif val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    return False

    def height(self,root):
        if root:
            r = self.height(root.right)
            l = self.height(root.left)
            return max(r,l)+1
        return 0

    def teste(self):
        tree = BinarySearchTree()

        x = [5,3,6,7,8,4]
        for i in x:
            tree.add(i)



#Binary Heaps(min-heaps and max-heaps):

X = 'TO DO'



#Trie:
class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode("")
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True
        
    def dfs(self, node, prefix):
        """Depth-first traversal of the trie
        
        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        if node.is_end:
            self.output.append((prefix + node.char))
        
        for child in node.children.values():
            self.dfs(child, prefix + node.char)
        
    def query(self, word):
        """Given an input (a prefix), retrieve all words stored in
        the trie with that prefix
        """
        self.output = []
        node = self.root
        
        # Check if the prefix is in the trie
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []
        
        # Traverse the trie to get all candidates
        self.dfs(node, word[:-1])

        # Sort the results in reverse order and return
        return self.output

    def teste(self):
        t = Trie()
        t.insert("was")
        t.insert("word")
        t.insert("war")
        t.insert("what")
        t.insert("where")
        print(t.query("wh"))

from collections import deque


#Tree Traversal:

def visit(node):
    print(node.val)
#In-Order traversal: left -> visit -> right
def inOrderTraversal(node):
    if node:
        inOrderTraversal(node.left)
        visit(node)
        inOrderTraversal(node.right)
#Pre-Order traversal: visit -> left -> right
def preOrderTraversal(node):
        if node:
            visit(node)
            preOrderTraversal(node.left)
            preOrderTraversal(node.right)
#Post-Order traversal: left -> right -> visit
def postOrderTraversal(node):
        if node:
            postOrderTraversal(node.left)
            postOrderTraversal(node.right)
            visit(node)

def levelOrderTraversal(root):
    # base case
    if not root:
        return
 
    queue = deque()
    queue.append(root)
 

    while queue:
        curr = queue.popleft()
        print(curr.key)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)


tree = BinarySearchTree()
x = [5,3,2,7,6,8,4,9]
#      5
#   3     7
# 2   4  6  8
#             9
#               10
for i in x:
    tree.add(i)


#4.2 Minimal Tree: Given a sorted array write a tree with the minimal height

#start from the middle of array, and work 1 to left and 1 to right
#Node(mid)
#[1,2,3,4,5,6,7,8,9]


#4.3 List of Depths: create one linked list to all the nodes in each level of the tree

def levelOrderTraversal(root):
    # base case
    if not root:
        return
 
    queue = deque()
    queue.append((root,1))
    lists = {}
    while queue:
        curr = queue.popleft()
        if curr[1] in lists:
            lists[curr[1]].append(curr[0].val)
        else:
            lists[curr[1]] = [curr[0].val]
        
        if curr[0].left:
            queue.append((curr[0].left,curr[1]+1))
        if curr[0].right:
            queue.append((curr[0].right,curr[1]+1))

    print(lists)
levelOrderTraversal(tree.root)

#4.4 Check Balanced: check if a binary tree is balanced, each subtree of a node do not differ more than one in height

def height(root):
    if root:
        r = height(root.right)
        l = height(root.left)
        return max(r,l)+1
    return 0

def bfs(root):
    q = [root]
    while q:
        x=q.pop(0)
        l = x.left if x.left else 0
        r = x.right if x.right else 0
        if abs(height(l)-height(r))>1:
            return False
        if l: q.append(l)
        if r: q.append(r)
    return True

print(bfs(tree.root))



#4.5 Validate BST: validate if a binary tree is a binary search tree

x = BinaryNode(15)
x.left = BinaryNode(10)
x.right = BinaryNode(20)

y = BinaryNode(5)
y.left = BinaryNode(10)
y.right = BinaryNode(20)

z = BinaryNode(5)
z.right = BinaryNode(10)
z.right.right = BinaryNode(20)

def validateBST(root):
    arr = dfs_in_order(root,[])
    return is_ordered(arr)

#TC = O(n)
def is_ordered(arr):
    last = arr[0]
    for i in arr[1:]:
        if i>last:
            last=i
        else:
            return False
    return True

#SC = O(n)
#TC = O(n)
def dfs_in_order(root,arr):
    if root:
        dfs_in_order(root.left,arr)
        arr.append(root.val)
        dfs_in_order(root.right,arr)
    return arr

""" print(validateBST(x))
print(validateBST(y))
print(validateBST(z)) """

#4.7 Build Order: 

class Project:
    name = 'a'
    dependencies = []


#4.8 First Common Ancestor
