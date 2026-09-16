# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None 
            
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop() 
            if visited:
                temp = node.left
                node.left = node.right
                node.right = temp
            else:
                stack.append((node, True)) 
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
        return root
