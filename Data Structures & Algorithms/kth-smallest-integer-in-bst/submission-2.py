# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        lst = []
        def dfs_inorder(node):

            nonlocal lst 
            
            if not node:
                return 
            
            dfs_inorder(node.left)

            lst.append(node)

            dfs_inorder(node.right)


        dfs_inorder(root)

        return lst[k-1].val
                
               

                


        

