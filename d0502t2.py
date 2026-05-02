# Definition for a binary tree node.
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left == None:
            if root.right == None :
                return True 
            return False 
    
        if root.right == None:
            return False
        self.flipTree(root.left)
        return self.isTreeEqual(root.left, root.right)
 

    def flipTree(self, root: Optional[TreeNode]): 
        if root==None:
            return 
        left_tmp = root.left 
        root.left = root.right 
        root.right = left_tmp 

        self.flipTree(root.left)
        self.flipTree(root.right)

    def isTreeEqual(self, t1: Optional[TreeNode], t2:Optional[TreeNode]):
        if t1==None and t2==None: 
            return True 
        if t1 == None or t2==None:
            return False 
        return t1.val == t2.val and self.isTreeEqual(t1.left, t2.left) and self.isTreeEqual(t1.right, t2.right)