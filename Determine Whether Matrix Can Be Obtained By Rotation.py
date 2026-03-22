class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
            n = len(mat)
        
            # assume all 4 rotations possible initially
            r0 = r90 = r180 = r270 = True
            
            for i in range(n):
                for j in range(n):
                    
                    # 0°
                    if mat[i][j] != target[i][j]:
                        r0 = False
                    
                    # 90°
                    if mat[i][j] != target[j][n-1-i]:
                        r90 = False
                    
                    # 180°
                    if mat[i][j] != target[n-1-i][n-1-j]:
                        r180 = False
                    
                    # 270°
                    if mat[i][j] != target[n-1-j][i]:
                        r270 = False
            
            return r0 or r90 or r180 or r270
