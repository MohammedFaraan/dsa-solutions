# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.length = 0

        def dfs(node):
            if not node:
                return

            val = dfs(node.left)
            if val is not None:
                return val

            res.append(node.val)
            self.length += 1
            if self.length == k:
                return res[-1]

            val = dfs(node.right)
            if val is not None:
                return val

        return dfs(root)
