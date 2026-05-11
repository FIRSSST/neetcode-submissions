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
                return 0
            
            left_height = heightOfNode(node.left)
            right_height = heightOfNode(node.right)

            node_height = 1 + max(left_height, right_height)

            nonlocal height
            height[node] = node_height

            return node_height
        
        heightOfNode(root)
      
        stack = [root]
        while stack:
            node = stack.pop()

            left_height = 0
            right_height = 0

            if node.left:
                stack.append(node.left)
                left_height = height[node.left]
            if node.right:
                stack.append(node.right)
                right_height = height[node.right]

            if abs(left_height - right_height) > 1:
                return False

            
        
        return True