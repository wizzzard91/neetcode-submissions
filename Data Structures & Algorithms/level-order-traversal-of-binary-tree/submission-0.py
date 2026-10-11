# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        currentLevelNodes = [root]
        result = []

        while currentLevelNodes:
            nextLevelNodes, currentLevelValues = [], []
            for node in currentLevelNodes:
                if node.left: nextLevelNodes.append(node.left)
                if node.right: nextLevelNodes.append(node.right)
                currentLevelValues.append(node.val)
            currentLevelNodes = nextLevelNodes
            result.append(currentLevelValues)
            
        return result
        