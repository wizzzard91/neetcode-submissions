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

        result = []
        q = [root]
        while q:
            nextlvl, curlvlresult = [], []
            for node in q:
                curlvlresult.append(node.val)
                if node.left: nextlvl.append(node.left)
                if node.right: nextlvl.append(node.right)
            result.append(curlvlresult)
            q = nextlvl
        return result

        