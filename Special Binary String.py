class Solution:
    def makeLargestSpecial(self, s: str) -> str:
            
        if len(s) <= 2:
            return s
        
        count = 0
        start = 0
        parts = []
        
        for i, ch in enumerate(s):
            if ch == '1':
                count += 1
            else:
                count -= 1
            
            # Found a balanced special substring
            if count == 0:
                # Recursively process inside
                inner =self.makeLargestSpecial(s[start+1:i])
                parts.append('1' + inner + '0')
                start = i + 1
        
        # Sort in descending order
        parts.sort(reverse=True)
        
        return ''.join(parts)
