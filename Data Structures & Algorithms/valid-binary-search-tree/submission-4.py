# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # in order traversal check if bst is valid Left -> Root -> Right 

        if not root:
            return True
        
        stack = [(root, False)]
        lst = []

        while stack:
            node,visited = stack.pop()
            if visited:
                lst.append(node.val)
            else:
                if node.right:
                    stack.append((node.right, False))
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
        
        for i in range (len(lst)-1):
            j = i+1
            if lst[i] >= lst[j]:
                return False

        return True


            


