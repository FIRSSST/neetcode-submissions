# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same_tree(root_1, root_2):
            if root_1 == None and root_2 != None:
                return False
            if root_1 != None and root_2 == None:
                return False 
            if root_1 == None and root_2 == None:
                return True 
            
            same_val = root_1.val == root_2.val 

            left_same_val = same_tree(root_1.left, root_2.left)
            right_same_val = same_tree(root_1.right, root_2.right)

            return same_val and left_same_val and right_same_val
        
        def sub_tree(root, subRoot):
            
            if root is None:
                return False
            
            sameTree = same_tree(root, subRoot)

            if sameTree:
                return True
            
            left_same_tree = sub_tree(root.left, subRoot)
            right_same_tree = sub_tree(root.right, subRoot)

            return sameTree or left_same_tree or right_same_tree

        return sub_tree(root, subRoot)
