class Solution(object):
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])
        
        # dp[j] = longest valid subsequence ending at column j
        dp = [1] * m
        
        for j in range(m):
            for i in range(j):
                # check if column i can come before column j
                valid = True
                for r in range(n):
                    if strs[r][i] > strs[r][j]:
                        valid = False
                        break
                
                if valid:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        # maximum columns we can keep
        max_keep = max(dp)
        
        # minimum deletions
        return m - max_keep
        
