import sys

#My Solution:
#Space O(n)
#Time O(n+n) => O(n)
class Solution:
    def isValidBST(self, root) -> bool:
        inorder_tree = self.inorderTraversal(root)
        for i in range(len(inorder_tree)-1):
            if inorder_tree[i] >= inorder_tree[i+1]:
                return False
        return True
    
    def inorderTraversal(self,root) -> list:
        if root:
            return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
        return []


#Best Solution:
class Solution:
    def isValidBST(self, root) -> bool:
        INF = sys.maxsize
        
        def helper(node, lower, upper):
            if not node:
				# empty node or empty tree
                return True
            
            if lower < node.val < upper:
				# check if all tree nodes follow BST rule
                return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)

            else:
				# early reject when we find violation
                return False

        return helper( node=root, lower=-INF, upper=INF )