# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(root1, root2):
            if root1 == None and root2 != None:
                return False 
            if root2 == None and root1 != None:
                return False 
            if root1 == None and root2 == None:
                return True
            
            
            same_val = root1.val == root2.val

            left_same_val = dfs(root1.left, root2.left)
            right_same_val = dfs(root1.right, root2.right)

            return left_same_val and right_same_val and same_val
            
        return dfs(p, q)