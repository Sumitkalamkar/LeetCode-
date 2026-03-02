class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
         
            n = len(grid)

            # count trailing zeros
            zeros = []
            for row in grid:
                count = 0
                for x in reversed(row):
                    if x == 0:
                        count += 1
                    else:
                        break
                zeros.append(count)

            swaps = 0

            for i in range(n):
                needed = n - i - 1
                j = i

                # find suitable row
                while j < n and zeros[j] < needed:
                    j += 1

                if j == n:
                    return -1

                # bring row upward
                while j > i:
                    zeros[j], zeros[j-1] = zeros[j-1], zeros[j]
                    swaps += 1
                    j -= 1

            return swaps
