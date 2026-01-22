class Solution:
    def minBitwiseArray(self, nums):
        ans = []

        for p in nums:
            if p == 2:
                ans.append(-1)
                continue

            best = None

            # Try removing each set bit
            for bit in range(31):
                if (p >> bit) & 1:
                    x = p ^ (1 << bit)
                    if x >= 0 and (x | (x + 1)) == p:
                        if best is None or x < best:
                            best = x

            ans.append(best if best is not None else -1)

        return ans
