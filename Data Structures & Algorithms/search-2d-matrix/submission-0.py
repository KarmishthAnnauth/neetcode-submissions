class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows*cols-1

        while l <= r:
            m = (l+r)//2
            v = matrix[m//cols][m%cols]
            
            if v == target:
                return True
            elif v < target: 
                l = m + 1 
            else:
                r = m - 1
        
        return False
                