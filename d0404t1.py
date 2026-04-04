class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        is_found = False  
        for line in matrix:
            for c in line:
                if c==target:
                    is_found = True
        return is_found
        pass 