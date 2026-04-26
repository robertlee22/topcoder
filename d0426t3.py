class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True 
            if i+1 < len(s):
                if s[i] == s[i+1]:
                    dp[i][i+1] = True 

        for w in range(1, len(s)): 
            for i in range(len(s)):
                # odd 
                lf = i-w 
                rg = i+w 

                if lf < 0 or rg >= len(s):
                    continue 
                
                
                if s[lf] == s[rg] and dp[lf+1][rg-1]:
                    dp[lf][rg] = True 
                else :
                    dp[lf][rg] = False 
                
                # even
                lf = i-w 
                rg = i+1 + w 
                if lf < 0 or rg >= len(s):
                    continue 
                if s[lf] == s[rg] and dp[lf+1][rg-1]:
                    dp[lf][rg] = True 
                else :
                    dp[lf][rg] = False 

        ans = ""
        alen = 0 

        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i][j]: 
                    if alen < j-i+1 : 
                        alen = j-i+1 
                        ans = s[i:j+1]
        return ans 
    
    def longestPalindrome2(self, s: str) -> str:
        ans = "" 
        alen = 0 
        for i in range(len(s)-1+1): 
            for j in range(i+1, len(s)+1): 
                sub = s[i:j] 

                if self.isPalindrome(sub):
                    if len(sub)> alen: 
                        ans = sub 
                        alen = len(sub)
        return ans 
                          
        pass    
    def isPalindrome(self, s):
        ans = True
        for i in range(len(s)//2):
            j = len(s)-i-1  
            if s[i] != s[j]:
                ans = False
                break 
        return ans 
    
s = Solution() 
r = s.longestPalindrome("cabaccab")
# cabaccab
print(r)


"""
 c a b a c c a b

 dp(i,j) -> dp(0,n-1)

 dp(i,j) 

 dp[2,2]=true , s[1] = s[3] -> dp[1,3] = true 
                !=  d[1,3] = false 


for i in range()

[
[True, False, False, False, False, False, False, False], 
[False, True, False, False, False, False, False, False], 
[False, False, True, False, False, False, False, False], 
[False, False, False, True, False, False, False, False], 
[False, False, False, False, True, True, False, False], 
[False, False, False, False, False, True, False, False], 
[False, False, False, False, False, False, True, False], 
[False, False, False, False, False, False, False, True]]
"""