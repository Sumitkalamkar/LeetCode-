from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        
        
        for i, val in enumerate(nums):
            pos[val].append(i)
        
        ans = float('inf')
        
        
        for indices in pos.values():
            if len(indices) < 3:
                continue
            
            
            for i in range(len(indices) - 2):
                first = indices[i]
                third = indices[i + 2]
                dist = 2 * (third - first)
                ans = min(ans, dist)
        
        return ans if ans != float('inf') else -1
