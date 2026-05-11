# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        deq = deque()

        deq.append(root)

        res = []
        while deq:
            size = len(deq)
            arr = []

            for i in range (0, size):
                node = deq.popleft()
                arr.append(node.val)

                if node.left:
                    deq.append(node.left)

                if node.right:
                    deq.append(node.right)
            
            res.append(arr)
        return res