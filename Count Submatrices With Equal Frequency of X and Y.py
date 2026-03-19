class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        
            n, m = len(grid), len(grid[0])
    
            # prefix sums
            sum_ps = [[0]*m for _ in range(n)]
            x_ps = [[0]*m for _ in range(n)]
            
            for i in range(n):
                for j in range(m):
                    val = 0
                    if grid[i][j] == 'X':
                        val = 1
                    elif grid[i][j] == 'Y':
                        val = -1
                    
                    x_val = 1 if grid[i][j] == 'X' else 0
                    
                    sum_ps[i][j] = val
                    x_ps[i][j] = x_val
                    
                    if i > 0:
                        sum_ps[i][j] += sum_ps[i-1][j]
                        x_ps[i][j] += x_ps[i-1][j]
                    if j > 0:
                        sum_ps[i][j] += sum_ps[i][j-1]
                        x_ps[i][j] += x_ps[i][j-1]
                    if i > 0 and j > 0:
                        sum_ps[i][j] -= sum_ps[i-1][j-1]
                        x_ps[i][j] -= x_ps[i-1][j-1]
            
            ans = 0
            
            for i in range(n):
                for j in range(m):
                    if sum_ps[i][j] == 0 and x_ps[i][j] > 0:
                        ans += 1
            
            return ans
