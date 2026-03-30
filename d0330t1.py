
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs_list = []
        max_len = 0
        for i1 in range(len(s)): 
            for i2 in range(i1+1, len(s)+1):
                sub = s[i1:i2]
                mps = {}
                valid = True  
                for c in sub: 
                    if c not in mps: 
                        mps[c] = 1 
                    else:
                        valid = False
                if valid: 
                    # subs_list.append(sub)
                    max_len = max(max_len, len(sub))
                else:
                    break
        
        return max_len 

# s = Solution() 

# print(r)
            
