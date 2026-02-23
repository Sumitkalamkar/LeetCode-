class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        needed = 1 << k
        seen = set()
        
        num = 0
        mask = needed - 1
        
        for i in range(len(s)):
            num = ((num << 1) & mask) | int(s[i])
            
            if i >= k - 1:
                seen.add(num)
                if len(seen) == needed:
                    return True
        
        return False
