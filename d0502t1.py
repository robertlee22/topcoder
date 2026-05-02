from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hsh = {} 
        
        for e in nums: 
            hsh[e] = hsh.get(e, 0) + 1 
        
        e_list = [] 
        for e in hsh : 
            e_list.append(Ele(e, hsh[e]))
        
        n_list = sorted(e_list, key=lambda x: -x.count)
        return n_list[0].val



class Ele: 
    def __init__(self, val,cnt):
        self.val = val
        self.count = cnt
    
