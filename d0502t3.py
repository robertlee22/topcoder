# Definition for a binary tree node.
from typing import Optional



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def myTest(self): 
        root = TreeNode(val=1, left=TreeNode(val=2))
        r = self.diameterOfBinaryTree(root) 
        return r
        pass 

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.global_dis = 0
        self.walk(root) 
        return self.global_dis 
        pass 

    def walk(self, root: TreeNode ): 
        
        if root.left is None:
            root.left_depth = 0 
        else:
            lfd = self.walk(root.left)["depth"]
            root.left_depth = 1 + lfd
        
        if root.right is None: 
            root.right_depth = 0 
        else:
            rgd = self.walk(root.right)["depth"]
            root.right_depth = rgd  + 1
        
        
        
        self.global_dis = max(self.global_dis, root.left_depth + root.right_depth)

        return {
            "depth":max(root.left_depth, root.right_depth)
        }
            
        

        
        
        