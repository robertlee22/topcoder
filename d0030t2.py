


from typing import Dict
from typing import List
class Solution:
    #https://leetcode.cn/problems/group-anagrams/?envType=study-plan-v2&envId=top-100-liked
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups :Dict[str, List[str]] = {}
        result = []
        for each in strs: 
            
            hsh = self.toAtom(each) 
            if hsh not in groups: 
                groups[hsh] = [each]
            else: 
                groups[hsh].append(each)
        
        for k in groups:
            result.append(groups[k])
        return result 
            

    def toAtom(self, s): 
        mps = {} 
        hsh = '' 
        for c in s:
            if c in mps: 
                mps[c] = 1+ mps[c] 
            else: 
                mps[c] = 1 
            
        
        for i in range(97,123):
            if chr(i) in mps: 
                hsh += 'b' + str(i-97) + 'c' + str(mps[chr(i)]) 
        
        return hsh 


