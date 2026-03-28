class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)

        # Step 1: check diagonal
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""

        # DSU
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # union positions
        for i in range(n):
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    union(i, j)

        # assign characters
        group_char = {}
        current_char = ord('a')

        word = [''] * n

        for i in range(n):
            root = find(i)
            if root not in group_char:
                if current_char > ord('z'):
                    return ""
                group_char[root] = chr(current_char)
                current_char += 1
            word[i] = group_char[root]

        word = ''.join(word)

        #verify LCP
        lcp2 = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    lcp2[i][j] = 1 + lcp2[i + 1][j + 1]
                else:
                    lcp2[i][j] = 0

        # compare
        for i in range(n):
            for j in range(n):
                if lcp[i][j] != lcp2[i][j]:
                    return ""

        return word
