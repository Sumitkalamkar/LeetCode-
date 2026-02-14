class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        

        dp = [[0.0] * (r + 1) for r in range(query_row + 1)]
        
        dp[0][0] = poured
        
        for r in range(query_row):
            for c in range(len(dp[r])):
                
  
                overflow = max(0.0, dp[r][c] - 1.0)
                
                if overflow > 0:
                    dp[r+1][c] += overflow / 2
                    dp[r+1][c+1] += overflow / 2
        

        return min(1.0, dp[query_row][query_glass])
