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

        stack = [(root, root.val)] #root, maxVal
        good = 0 

        while stack:
            node, maxVal = stack.pop()

            if node.val >= maxVal:
                good += 1

            maxValueSoFar = max(maxVal, node.val)
            if node.left:
                stack.append((node.left, maxValueSoFar))
            if node.right:
                stack.append((node.right, maxValueSoFar))
        
        return good