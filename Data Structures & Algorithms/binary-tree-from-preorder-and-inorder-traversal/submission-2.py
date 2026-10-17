# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIndex = {val: i for i, val in enumerate(inorder)}
        return self.build(preorder, inorderIndex, 0, 0, len(inorder) - 1)

    def build(self, preorder, inorderIndex, preStart, inStart, inEnd):
        if inStart > inEnd:
            return None

        rootVal = preorder[preStart]
        root = TreeNode(rootVal)
        mid = inorderIndex[rootVal]
        leftSize = mid - inStart

        root.left = self.build(preorder, inorderIndex, preStart + 1, inStart, mid - 1)
        root.right = self.build(preorder, inorderIndex, preStart + 1 + leftSize, mid + 1, inEnd)
        return root