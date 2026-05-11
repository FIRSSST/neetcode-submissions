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
        
        stack = [(root, root.val)] #node, maxInPath
        good = 0 

        while stack:
            node, maxVal = stack.pop()
            
            if node.val >= maxVal:
                good += 1
            
            maxVal = max(node.val, maxVal)

            if node.left:
                stack.append((node.left, maxVal))
            if node.right:
                stack.append((node.right, maxVal))
        return good
    