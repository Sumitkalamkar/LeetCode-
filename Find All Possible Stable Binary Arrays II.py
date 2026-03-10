class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][0] = stable arrays with i zeros, j ones, ending in 0
        # dp[i][j][1] = stable arrays with i zeros, j ones, ending in 1
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # Base cases: single runs of 0s or 1s (up to limit length)
        for i in range(1, min(limit, zero) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(limit, one) + 1):
            dp[0][j][1] = 1
        
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # Append 0: sum all valid arrays with i-1 zeros, j ones
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
                # Subtract: arrays that would create limit+1 consecutive zeros
                # Those are arrays with i-1-limit zeros, j ones, ending in 1
                if i - limit - 1 >= 0:
                    dp[i][j][0] = (dp[i][j][0] - dp[i-1-limit][j][1]) % MOD
                
                # Append 1: sum all valid arrays with i zeros, j-1 ones
                dp[i][j][1] = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD
                # Subtract: arrays that would create limit+1 consecutive ones
                # Those are arrays with i zeros, j-1-limit ones, ending in 0
                if j - limit - 1 >= 0:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j-1-limit][0]) % MOD
        
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD
