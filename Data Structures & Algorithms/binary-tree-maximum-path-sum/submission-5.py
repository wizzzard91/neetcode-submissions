# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    best = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def recursive(node):
            if not node:
                return 0
        
            leftValue = recursive(node.left)
            rightValue = recursive(node.right)

            self.best = max(self.best, node.val, node.val + leftValue, node.val + rightValue, node.val + leftValue + rightValue)
            return max(node.val, node.val + leftValue, node.val + rightValue)

        recursive(root)
        return self.best
        