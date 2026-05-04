class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {} 
        pre = 0
        count = 0 
        mp[0] = 1 
        for e in nums: 
            pre += e 
            if pre-k in mp: 
                count += mp[pre-k]
            mp[pre] = mp.get(pre, 0) + 1
        return count 