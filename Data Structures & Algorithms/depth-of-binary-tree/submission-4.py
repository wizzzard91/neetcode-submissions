# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q, maxlvl = [root], 0
        while q:
            nextLvl = []
            maxlvl += 1
            for node in q:
                if node.left: nextLvl.append(node.left)
                if node.right: nextLvl.append(node.right)
            q = nextLvl
        return maxlvl
