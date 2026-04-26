from typing import List 
import math 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = Dps() 
        dp.con = [nums[0]]
        dp.non_con = [nums[0]]

        for i in range(1, len(nums)): 
            dp = dp.iter(dp, nums[i])
        return dp.get_ans() 
        



class Dps: 
    def __init__(self):
        self.con = [] 
        self.non_con = []
        pass

    def iter(self, last_dp, e): 
        con = [each*e  for each in last_dp.con]
        non = last_dp.non_con
        self.con = con 
        self.non_con = non + [e]
        return self 
    
    def get_ans(self): 
       return max(self.con + self.non_con)
        

s = Solution() 
r = s.maxProduct([2,3,-2,4])
print(r)
"""
nums = [2,3,-2,4]

"""