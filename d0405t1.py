from typing import List
class Solution:
    # def numIslands2(self, grid: List[List[str]]) -> int:
     
    #     self.island = 0 
    #     self.grid = grid
       
    #     self.lookup = {} 
    #     M = len(self.grid) 
    #     N = len(self.grid[0]) 
    
    #     for row in range(len(grid)): 
    #         for col in range(len(grid[row])): 
    #                 if (grid[row][col] == '0' ) or ( row*N + col in self.lookup ):
    #                      continue 
                    
    #                 self.island +=1
    #                 self.walks(row, col, self.island)

    #     return self.island

    def numIslands(self, grid: List[List[str]]) -> int:
        uf = UnionFind(grid)

        M= len(grid)
        N = len(grid[0])

        for i in range(M):
             for j in range(N):
                  k1 = i*N + j
                  if grid[i][j] == '1':
                       grid[i][j] = '0'
                       for x,y in [(i+1, j) , (i-1,j) , (i,j+1), (i,j-1)]:
                            if 0<=x<M and 0<=y<N and grid[x][y] == '1':
                                 k2 = x*N + y
                                 uf.union(k1, k2)
        return uf.islands        

    def walks(self, row, col, no_island):
        M = len(self.grid) 
        N = len(self.grid[0]) 
        key =  row*N + col 
        # print(row, col)
        # print(no_island)
        self.lookup[key] = {'no': no_island}

        next_row = row + 1
        next_col = col 
        key = next_row * N  + next_col
        if  next_row < M and \
            next_col < N and \
            next_row >= 0 and \
            next_col >= 0 and \
                self.grid[next_row][next_col] == '1' and key not in self.lookup:
            self.walks(next_row, next_col, no_island)
            
        
        # if col + 1 < N and self.grid[row][col+1] == '1':
        #      self.walks(row, col + 1, no_island)
        #      pass 
        next_row = row 
        next_col = col + 1
        key = next_row * N  + next_col
        if  next_row < M and \
            next_col < N and \
            next_row >= 0 and \
            next_col >= 0 and \
                self.grid[next_row][next_col] == '1' and key not in self.lookup:
            self.walks(next_row, next_col, no_island)

        
        next_row = row-1
        next_col = col 
        key = next_row * N  + next_col
        if  next_row < M and \
            next_col < N and \
            next_row >= 0 and \
            next_col >= 0 and \
                self.grid[next_row][next_col] == '1' and key not in self.lookup:
            self.walks(next_row, next_col, no_island)
       
        
        next_row = row
        next_col = col - 1 
        key = next_row * N  + next_col
        if  next_row < M and \
            next_col < N and \
            next_row >= 0 and \
            next_col >= 0 and \
                self.grid[next_row][next_col] == '1' and key not in self.lookup:
            self.walks(next_row, next_col, no_island)


class UnionFind: 
    def __init__(self, grid):
          M = len(grid)
          N = len(grid[0])
          size = M*N 
          self.islands = 0 
          self.parent = list(range(size)) 
          self.rank = [0] * size 

          for i in range(M):
               for j in range(N):
                    if grid[i][j] == '1':
                         self.islands += 1
          
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
          rootx = self.find(x) 
          rooty = self.find(y)  

          if rootx != rooty:
               self.parent[rootx] = rooty
               self.islands -= 1
          
       
s = Solution() 
r = s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
print(r)