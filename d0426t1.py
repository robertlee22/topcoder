from typing import List 
import copy
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = Dps() 

        for i in range(len(nums)): 
            dp = dp.iter(nums[i], dp)
        
        return dp.get_out() 


    
class Dps: 
    def __init__(self):
        self.book = {}
        pass

    def iter(self, num, last_dp): 
        book = copy.deepcopy(last_dp.book)
        if num not in book: 
            book[num] = 1 
        for k in book: 
            if num > k: 
                book[num] = max(book[k]+1 , book[num] )
        self.book = book 
        return self 
    
    def get_out(self): 
        ans = 0 
        for k in self.book: 
            ans = max(self.book[k], ans ) 
        return ans 


s = Solution() 
r = s.lengthOfLIS([10,9,2,5,3,7,101,18])
print(r)
    
            
"""

dp[n] = dp[n-1] .append [ (nums[n], len) ]
ans = dp[n].lst.len.max 


dp[0] = num
dp[1] = 
"""