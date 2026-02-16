class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for _ in range(32):          # Because 32-bit integer
            bit = n & 1              # Get last bit
            result = (result << 1) | bit  # Shift result left and add bit
            n = n >> 1               # Shift n right
        
        return result
