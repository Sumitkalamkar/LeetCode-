class Solution(object):
    def maxTwoEvents(self, events):
      # Sort events by start time
        events.sort(key=lambda x: x[0])
        
        heap = []  # min-heap: (endTime, value)
        best_so_far = 0
        ans = 0
        
        for start, end, value in events:
            # Remove events that ended before current start
            while heap and heap[0][0] < start:
                _, val = heapq.heappop(heap)
                best_so_far = max(best_so_far, val)
            
            # Try taking current event + best previous non-overlapping event
            ans = max(ans, best_so_far + value)
            
            # Push current event into heap
            heapq.heappush(heap, (end, value))
        
        return ans
