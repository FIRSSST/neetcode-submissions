# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        max_depth_so_far = 1 

        deq = deque()
        deq.append((root, max_depth_so_far))

        while deq:
            node, depth = deq.popleft()

            if depth > max_depth_so_far:
                max_depth_so_far = depth
            
            if node.left:
                deq.append((node.left, depth+1))
            if node.right:
                deq.append((node.right, depth+1))
        
        return max_depth_so_far