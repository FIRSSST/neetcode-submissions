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
        lstOfVals = []
        while stack:
            node,visited = stack.pop()

            if not node:
                continue

            if not visited:
                if node.right:
                    stack.append((node.right, False))
                   
                
                stack.append((node, True))

                if node.left:
                    stack.append((node.left, False))

         
                    
            else:
               lstOfVals.append(node.val)


        for i in range (0, len(lstOfVals) - 1):
            j = i + 1
            if lstOfVals[i] >= lstOfVals[j]:
                return False

        return True


            


