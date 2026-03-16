class Solution:
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        res = set()

        for r in range(m):
            for c in range(n):

                # radius = 0 case (single cell)
                res.add(grid[r][c])

                # try bigger rhombus
                k = 1
                while True:
                    if r-k < 0 or r+k >= m or c-k < 0 or c+k >= n:
                        break

                    s = 0

                    # top -> right
                    for i in range(k):
                        s += grid[r-k+i][c+i]

                    # right -> bottom
                    for i in range(k):
                        s += grid[r+i][c+k-i]

                    # bottom -> left
                    for i in range(k):
                        s += grid[r+k-i][c-i]

                    # left -> top
                    for i in range(k):
                        s += grid[r-i][c-k+i]

                    res.add(s)
                    k += 1

        return sorted(res, reverse=True)[:3]
