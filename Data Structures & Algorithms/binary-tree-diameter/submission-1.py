# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
      
        height = {}
        def height_f(node):
            if not node:
                return 0

            left_height = height_f(node.left)
            right_height = height_f(node.right)

            nonlocal height
            height[node.left] = left_height
            height[node.right] = right_height

            height[node] = max(left_height, right_height) + 1

            return height[node]

        height_f(root)
        stack = [root]
        max_diameter = 0
        while stack:
            node = stack.pop()

            if node in height:
                max_diameter = max(max_diameter, height.get(node.left, 0) + height.get(node.right, 0))

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return max_diameter

