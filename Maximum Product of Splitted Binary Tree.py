class Solution(object):
    def maxProduct(self, root):
        MOD = 10**9 + 7
        
        # Step 1: Find total sum of the tree
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)
        
        total = totalSum(root)
        self.max_product = 0
        
        # Step 2: DFS to compute subtree sums and products
        def dfs(node):
            if not node:
                return 0
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            
            subtree_sum = node.val + left_sum + right_sum
            
            # Try cutting above this subtree
            product = subtree_sum * (total - subtree_sum)
            self.max_product = max(self.max_product, product)
            
            return subtree_sum
        
        dfs(root)
        return self.max_product % MOD
