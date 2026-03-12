class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        self.count -= 1
        return True


class Solution:
    def maxStability(self, n, edges, k):
        must_edges = []
        optional_edges = []

        max_val = 0

        for u, v, s, must in edges:
            max_val = max(max_val, s)
            if must:
                must_edges.append((u, v, s))
            else:
                optional_edges.append((u, v, s))

        def can(x):
            dsu = DSU(n)

            # Step 1: mandatory
            for u, v, s in must_edges:
                if s < x:
                    return False
                if not dsu.union(u, v):
                    return False  # cycle

            upgrades = 0

            good = []
            upgrade_needed = []

            for u, v, s in optional_edges:
                if s >= x:
                    good.append((u, v))
                elif 2 * s >= x:
                    upgrade_needed.append((u, v))

            # Step 2: use good edges
            for u, v in good:
                dsu.union(u, v)

            # Step 3: use upgraded edges
            for u, v in upgrade_needed:
                if dsu.union(u, v):
                    upgrades += 1
                    if upgrades > k:
                        return False

            return dsu.count == 1

        lo, hi = 0, max_val * 2
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
