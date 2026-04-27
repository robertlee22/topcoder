class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2) 
        dp = [[0]*cols for _ in range(rows)] 

        for i in range(rows):
            dp[i][0] = 1 if text1[i]==text2[0] else dp[i-1][0]
        for j in range(cols): 
       
                  
            dp[0][j] = 1 if text1[0]==text2[j] else dp[0][j-1]
            
        
        for i in range(1,rows): 
            for j in range(1,cols): 
                if text1[i] == text2[j]: 

                        dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[rows-1][cols-1] 
    