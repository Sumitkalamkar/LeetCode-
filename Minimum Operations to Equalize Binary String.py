class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        a = s.count('0')
        
        if a == 0:
            return 0
        
        # Try minimal m upwards
        for m in range(1, n + 5):  # upper bound large enough
            total_flips = m * k
            if total_flips < a:
                continue
            if (total_flips - a) % 2 != 0:
                continue
            d = (total_flips - a) // 2
            max_d = a * ((m - 1) // 2) + (n - a) * (m // 2)
            if d <= max_d:
                return m
        return -1
