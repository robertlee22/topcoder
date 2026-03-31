
from typing import List 


class Solution:
    # https://leetcode.cn/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-100-liked
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height)-1
        current_max = 0 
        while left < right:
            now_vol = (right-left) * min(height[left], height[right])
            current_max = max(now_vol, current_max)
            
            if height[left] < height[right]:
                left += 1
            else: 
                right -=1 
        return current_max

# s = Solution() 

# print(r)
            
