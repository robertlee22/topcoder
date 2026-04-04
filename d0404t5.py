class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.s(root)
        pass 

    def walks(self, node):
        if node==None:
            return 
        self.walks(node.left)
        self.path.append(node.val)
   
        self.walks(node.right)

    def s(self, node):
        if node is None:
            return 0 
        
        length = 1 
        return max( self.s(node.left), self.s(node.right) ) + 1
    
    
