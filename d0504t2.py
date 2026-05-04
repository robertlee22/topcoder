import bisect 
from typing import List 

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target) 
    
    def searchInsert2(self, nums: List[int], target: int) -> int:
        lf,rg = 0,len(nums)-1
        while lf < rg : 
            mid = (lf + rg) //2 
            if nums[mid] >= target: 
                rg = mid
            else: 
                lf = mid + 1
            print(lf, rg)
        if nums[rg] >= target:
            return rg 
        else: 
            return rg + 1