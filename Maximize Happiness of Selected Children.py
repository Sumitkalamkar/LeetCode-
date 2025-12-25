class Solution(object):
    def maximumHappinessSum(self, happiness, k):
         happiness.sort(reverse=True)
         total = 0
    
         for i in range(k):
              total += max(happiness[i] - i, 0)
    
         return total
