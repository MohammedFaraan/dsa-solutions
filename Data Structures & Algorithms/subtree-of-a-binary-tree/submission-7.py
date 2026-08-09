# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return

            if node.val == subRoot.val:
                print(node.val)
                if self.isSame(node, subRoot):
                    print("found")
                    return True

            return dfs(node.left) or dfs(node.right)

        if dfs(root):
            return True
        
        return False
    
    def isSame(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q or (p.val != q.val):
            return False
                
        return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)

        

