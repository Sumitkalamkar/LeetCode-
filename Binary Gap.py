class Solution:
   def binaryGap(self,n: int) -> int:
        binary = bin(n)[2:]   # Convert to binary and remove '0b'
        last_index = -1
        max_gap = 0
        
        for i in range(len(binary)):
            if binary[i] == '1':
                if last_index != -1:
                    max_gap = max(max_gap, i - last_index)
                last_index = i
        
        return max_gap
