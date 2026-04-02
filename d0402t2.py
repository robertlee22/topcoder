from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pr = 0 
        pj = 0 

        M = len(matrix)
        N = len(matrix[0])
        
        top_line = 0
        right_line = 0 
        floor_line = 0 
        left_line = 0

        direction = 'right'
        move_count = 0

        result = []

        result.append(matrix[pr][pj])

        while True:

                        
            if move_count ==2:
                break

            if direction == 'right':
                if pj+1 <= N-1-right_line:
                    pj += 1
                    result.append(matrix[pr][pj])
                    move_count =0
                else:
                    move_count += 1
                    direction = 'down'
                    top_line += 1

            

            elif direction == 'down':
                if pr+1 <= M-1-floor_line:
                    pr += 1
                    result.append(matrix[pr][pj])
                    move_count =0
                else:
                    move_count += 1
                    direction = 'left'
                    right_line +=1
            
    
            elif direction == 'left':
                if pj-1 >= 0 + left_line:
                    pj -= 1
                    result.append(matrix[pr][pj])
                    move_count =0
                else:
                    move_count += 1
                    direction = 'up'
                    floor_line +=1
                        
          

            elif direction == 'up':
                if pr-1 >= 0 + top_line:
                    pr -= 1
                    result.append(matrix[pr][pj])
                    move_count =0
                else:
                    move_count += 1
                    direction = 'right'
                    left_line += 1
            # print(result)
        
        return result
    
s = Solution() 
r = s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print(r)
    
    
    
            
