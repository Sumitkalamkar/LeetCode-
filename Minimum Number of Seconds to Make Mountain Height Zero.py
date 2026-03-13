import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes):
        
        def can_finish(T):
            total = 0
            
            for t in workerTimes:
                # solve x(x+1)/2 * t <= T
                val = (2 * T) // t
                
                # quadratic solution
                x = int((math.sqrt(1 + 4 * val) - 1) // 2)
                total += x
                
                if total >= mountainHeight:
                    return True
            
            return False
        
        low, high = 0, 10**18
        
        while low < high:
            mid = (low + high) // 2
            
            if can_finish(mid):
                high = mid
            else:
                low = mid + 1
        
        return low
