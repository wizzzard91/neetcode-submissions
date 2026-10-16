# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEqual(self, q, p):
        if q and p:
            if q.val != p.val: return False
            if not self.isEqual(q.left, p.left): return False
            if not self.isEqual(q.right, p.right): return False
            return True
        elif not q and not p:
            return True
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False

        q = [root]
        while q:

            tmp = []
            for node in q:
                hasSubtree = self.isEqual(node, subRoot)
                if hasSubtree:
                    return True
                
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            
            q = tmp

        return False
