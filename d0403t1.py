from typing import List 
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        
        """
        (0,0) -> (0,2)
        (0,1) -> (1,2)
        (0,2) -> (2,2)

        def f(y, x, n) -> (y_, x_ , n) n>=2, n+=2 N=4
            

        for d [0, N//2]

            x_d_1, y_d_1  =  f(x_d_0, y_d_0 )
            
            x_r, y_r = transform(x_d , y_d)

            (x_r1, y_r1).  <-    (x_r0, y_r0)
            (x_r1, y_r1).  <-    (x_r0, y_r0)
            (x_r1, y_r1).  <-    (x_r0, y_r0)
            (x_r1, y_r1).  <-    (x_r0, y_r0)    
        
    """
        
        N = len(matrix)
        for d in range(0, N//2):
            n = N - 2*d 
            begin_es = [(0, e) for e in range(0, n-1)]
            for each in begin_es:
                y, x = each[0], each[1]


                yd, xd = self.f(y, x, n)
                origin_y, origin_x = self.g(y, x, n, d)
                dist_y, dist_x = self.g(yd, xd, n, d)
                
                t = matrix[dist_y][ dist_x] 
                matrix[dist_y][ dist_x]  = matrix[origin_y][origin_x]


                yd, xd = self.f(yd, xd, n)
                dist_y, dist_x = self.g(yd, xd, n, d)
                t2 = matrix[dist_y][ dist_x] 
                matrix[dist_y][ dist_x]  =  t 
                t = t2              

                yd, xd = self.f(yd, xd, n)
                dist_y, dist_x = self.g(yd, xd, n, d)
                t2 = matrix[dist_y][ dist_x] 
                matrix[dist_y][ dist_x]  =  t 
                t = t2   

                yd, xd = self.f(yd, xd, n)
                dist_y, dist_x = self.g(yd, xd, n, d)
                t2 = matrix[dist_y][ dist_x] 
                matrix[dist_y][ dist_x]  =  t 
                t = t2   
        
    
    # 旋转坐标
    def f(self, y, x, n): 

        yd= None 
        xd = None 
        if y==0 :
            xd = n-1
            yd = x 
        elif x== n-1:
            yd = n-1
            xd = n-1-y
        elif y==n-1:
            xd = 0
            yd = x
        else:
            yd = 0 
            xd = n-1 - y
        
        return (yd, xd)

    # 低纬度转高纬度
    def g(self, y,x, n, d):
        xd = x + d 
        yd = y + d 
        return (yd , xd )

    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        N = len(matrix)
        nc = N 
        while nc >1:
            gap = (N-nc)//2 
            lf = 0 + gap
            rg = N-1 - gap 

            top = 0 + gap 
            btm = N - 1 - gap 

            slot = [] 
            cur_slot = []
            
            # top
            for i in range(top, btm + 1):
                cur_slot.append( matrix[top][lf+i-top] )

            for i in range(top, btm + 1):
                slot.append(matrix[i][rg])
                matrix[i][rg] = cur_slot[i-top]
            

            # left 
            cur_slot = []
            for i in range(lf, rg+1):
                cur_slot.append( matrix[btm-(i-lf)][lf] )
            
           
            for i in range(lf, rg+1):
                matrix[top][i] = cur_slot[i-lf]
            
            # btm 

            cur_slot = []
            for i in range(top, btm+1):
                cur_slot.append( matrix[btm][lf+i-top] )
            for i in range(top, btm+1):
                matrix[lf][i] = cur_slot[i-top]
            
            # rg
            for i in range(lf, rg + 1):
                matrix[btm][i] = slot[len(slot)-1-(i-lf)]
            nc -= 2 
            pass 
    
    
        pass 

s = Solution() 
m = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.rotate(m)
print(m)

                