class Solution:
    def numSpecial(self, mat):
        m = len(mat)
        n = len(mat[0])

        row_count = [0] * m
        col_count = [0] * n

        # Count 1s in rows and columns
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        special = 0

        # Check special positions
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    special += 1

        return special
