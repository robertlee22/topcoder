from typing import List 
class Solution:
    def trap(self, height: List[int]) -> int:
        # 找到左柱
        acc_vol = 0 
        left_cur = 0 
        

        right_cur = left_cur + 1
        while left_cur < len(height) and right_cur < len(height):
            
            
            r_tallest = -1
            is_taller_found = False 
            co_idx = right_cur
            
            p1_black = 0 
            
            while right_cur < len(height):
                
                if height[right_cur] > r_tallest:
                    r_tallest = height[right_cur]
                    co_idx = right_cur
                if height[right_cur] > height[left_cur]:
                    is_taller_found = True  
                    break 
                    
                right_cur += 1
            
            for i in range(left_cur, co_idx):
                p1_black += min(height[i], r_tallest) 

            
            if is_taller_found:
               pass
                
            else:
                right_cur = co_idx 
                
            width = right_cur-left_cur 
            
            
            hgt = min(height[left_cur], height[right_cur])
            
            s = width * hgt - p1_black 
            # print(left_cur, right_cur, s)
            # print(width, hgt, p1_black, s, left_cur, right_cur)
            acc_vol += s 
            left_cur = right_cur 
            right_cur += 1

        return acc_vol 
    

        
"""
h_r >= h_l, 结算累加
h_r:rm < h_l，  
    找到次高的，结算累加
    找到连续下降的三角，结算。
换下一回合。


方法 2

dp(a,b) -> 这个区间可以装多少水


"""


