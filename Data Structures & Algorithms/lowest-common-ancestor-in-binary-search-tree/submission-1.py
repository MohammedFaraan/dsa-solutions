# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        pPath = []
        qPath = []

        def dfs(node, target, path):
            if not node:
                return False

            path.append(node)
            if node.val == target.val:
                return True

            if dfs(node.left, target, path) or dfs(node.right, target, path):
                return True

            path.pop()
            return False

        dfs(root, p, pPath)
        dfs(root, q, qPath)

        res = root

        for i in range(1, min(len(pPath), len(qPath))):
            if pPath[i].val == qPath[i].val:
                res = pPath[i]

        return res
