from typing import List 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new_inter = sorted(intervals, key=lambda x: x[0])
        
        lf, rg = new_inter[0][0], new_inter[0][1] 
        ans = []

        for idx in range(1,len(new_inter)):
            each = new_inter[idx] 
            if rg < each[0]:
                ans.append([lf,rg])
                lf = each[0]
                rg = each[1]
            else:
                rg = max(rg, each[1])
        
        ans.append([lf,rg])
        return ans