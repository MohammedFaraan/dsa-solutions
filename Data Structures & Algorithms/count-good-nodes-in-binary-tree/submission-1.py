# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res=0

        def dfs(node, maxV):
            if not node:
                return

            if node.val >= maxV:
                self.res+=1
                maxV=node.val
            
            if node.left:
                dfs(node.left, maxV)
            
            if node.right:
                dfs(node.right, maxV)
        
        if root:
            self.res += 1
            dfs(root.left, root.val)
            dfs(root.right, root.val)
        
        return self.res
