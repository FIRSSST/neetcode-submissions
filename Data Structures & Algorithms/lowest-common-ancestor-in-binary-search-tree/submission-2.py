# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
      
        i = 1
        def dfs(root):
            nonlocal i
            print("Call", i, 'root:', root.val)

            if root is None:
                return None
            
            print("We are now at:", root.val, 'L:', root.left and root.left.val or None, 'R:', root.right and root.right.val or None)
            
           
            if root.val > p.val and root.val < q.val:
                print("Returning root:", root.val)
                return root 
            if root.val > p.val and root.val > q.val:
                i += 1
                return dfs(root.left)
            elif root.val < p.val and root.val < q.val:
                i += 1
                return dfs(root.right)
            elif root.val < p.val and root.val > q.val:
                return root
            elif root.val == p.val or root.val == q.val:
                return root
        
        lca = dfs(root)
        return lca

            