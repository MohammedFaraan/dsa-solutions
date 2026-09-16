# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        vals = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)

        inorder(root)

        for i in range(1, len(vals)):
            if vals[i - 1] >= vals[i]:
                return False

        return True
