/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    maxDepth(root) {

        function dfs(node) {
            if (node === null) {
                return 0
            }

            
            const leftHeight = dfs(node.left)
            const rightHeight = dfs(node.right)

            return 1 + Math.max(leftHeight, rightHeight)
        }

        return dfs(root)

    }
}
