class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        
        MOD = 10**9 + 7

        # dp[z][o][last]
        dp = [[[0]*2 for _ in range(one+1)] for __ in range(zero+1)]

        # base cases
        for k in range(1, min(limit, zero) + 1):
            dp[k][0][0] = 1   # only zeros

        for k in range(1, min(limit, one) + 1):
            dp[0][k][1] = 1   # only ones

        # fill DP
        for z in range(zero+1):
            for o in range(one+1):

                # end with 0 → previous must be 1 block
                for k in range(1, min(limit, z)+1):
                    dp[z][o][0] += dp[z-k][o][1]
                    dp[z][o][0] %= MOD

                # end with 1 → previous must be 0 block
                for k in range(1, min(limit, o)+1):
                    dp[z][o][1] += dp[z][o-k][0]
                    dp[z][o][1] %= MOD

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD
