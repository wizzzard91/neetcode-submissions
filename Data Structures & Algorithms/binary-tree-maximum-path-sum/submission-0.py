# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    best = float("-inf")
    
    def recursive(self, root: TreeNode | Node) -> int:
        if root is None:
            return 0
        leftV = self.recursive(root.left)
        rightV = self.recursive(root.right)
        self.best = max(self.best, root.val, root.val+leftV, root.val+rightV, root.val+rightV+leftV)
        return max(root.val, root.val+leftV, root.val+rightV)
    
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.recursive(root)
        return self.best
