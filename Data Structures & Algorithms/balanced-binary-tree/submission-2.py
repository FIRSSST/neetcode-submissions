# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root == None:
            return True

        height = {}
        def heightOfNode(node):
            if node == None:
                return 0, True
            
            left_height, left_balance = heightOfNode(node.left)
            right_height, right_balance = heightOfNode(node.right)

            node_height = 1 + max(left_height, right_height)
            
            balanced = abs(left_height - right_height) < 2 and left_balance == True and right_balance == True

            nonlocal height
            height[node] = node_height

            return node_height, balanced
        
        height, balanced = heightOfNode(root)
      
        return balanced