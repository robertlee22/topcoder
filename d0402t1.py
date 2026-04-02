class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m2 = []
        for l1 in matrix: 
            s = [] 
            for e in l1: 
                s.append(e)
            m2.append(s)
        
        for r in range(len(m2)):
            for c in range(len(m2[r])):
                if m2[r][c] == 0:
                    for c0 in range(len(matrix[0])):
                        matrix[r][c0] = 0
                    for r0 in range(len(matrix)):
                        matrix[r0][c] = 0
        
        
                    
                