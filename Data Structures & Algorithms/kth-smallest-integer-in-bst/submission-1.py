# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        prev = None
        count = 0
        kthNode = None
        def dfs_inorder(node):
            nonlocal kthNode, count, prev
            if not node:
                return None
            
            dfs_inorder(node.left)

            count += 1
            prev = node
         
            if count == k:
                kthNode = node 

            dfs_inorder(node.right)


        dfs_inorder(root)
        return kthNode.val
        

