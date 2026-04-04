class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.path = []
        self.walks(root)
        return self.path

    def walks(self, node):
        if node==None:
            return 
        self.walks(node.left)
        self.path.append(node.val)
   
        self.walks(node.right)
        
    