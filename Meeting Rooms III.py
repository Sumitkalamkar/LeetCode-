class Solution(object):
    def mostBooked(self, n, meetings):
            # Sort meetings by start time
            meetings.sort()
            
            # Min-heap of free rooms
            free_rooms = list(range(n))
            heapq.heapify(free_rooms)
            
            # Min-heap of busy rooms: (end_time, room)
            busy_rooms = []
            
            # Count meetings per room
            count = [0] * n
            
            for start, end in meetings:
                duration = end - start
                
                # Free rooms that have finished before current meeting starts
                while busy_rooms and busy_rooms[0][0] <= start:
                    finish_time, room = heapq.heappop(busy_rooms)
                    heapq.heappush(free_rooms, room)
                
                if free_rooms:
                    # Assign meeting to free room
                    room = heapq.heappop(free_rooms)
                    heapq.heappush(busy_rooms, (end, room))
                else:
                    # Delay meeting
                    finish_time, room = heapq.heappop(busy_rooms)
                    new_end = finish_time + duration
                    heapq.heappush(busy_rooms, (new_end, room))
                
                count[room] += 1
            
            # Return room with max meetings (tie → smallest index)
            return count.index(max(count))
