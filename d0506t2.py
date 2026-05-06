# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional,List 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = [] 
        que = []
        if root is None :
            return ans 
        que.append(root)
        # self.walk_tag(root, 0)
        
        last_d = 0

        while len(que) != 0:
            cur_sub = []
            for _ in range(len(que)):
                top = que.pop(0)
                cur_sub.append(top.val)

                if top.left is not None :
                    que.append(top.left)
                if top.right is not None: 
                    que.append(top.right)

            # if top.depth > last_d :
            #     ans.append(cur_sub)
            #     cur_sub = []
            #     last_d = top.depth

            
            
            ans.append(cur_sub)
        return ans 
    
    def walk_tag(self, root: TreeNode, depth):
        root.depth = depth 
        if root.left is not None : 
            self.walk_tag(root.left, depth+1)
        if root.right is not None: 
            self.walk_tag(root.right, depth+ 1)