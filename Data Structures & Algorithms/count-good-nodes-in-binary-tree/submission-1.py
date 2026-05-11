# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 

        def dfs(node, maxSoFar):
            if not node:
                return 0
            
            res = 0 
            if node.val >= maxSoFar:
                res += 1
            if node.left:
                res += dfs(node.left, max(node.left.val, maxSoFar))
            
            if node.right:
                res += dfs(node.right, max(node.right.val, maxSoFar))

            return res

        return dfs(root, root.val)
