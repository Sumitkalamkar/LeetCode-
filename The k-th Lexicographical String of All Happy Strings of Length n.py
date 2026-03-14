class Solution:
    def getHappyString(self, n: int, k: int) -> str:
            count = 0
            ans = ""

            def backtrack(curr):
                nonlocal count, ans   
                
                if len(curr) == n:
                    count += 1
                    if count == k:
                        ans = curr
                    return
                
                for ch in "abc":
                    if not curr or curr[-1] != ch:
                        backtrack(curr + ch)

            backtrack("")
            return ans
