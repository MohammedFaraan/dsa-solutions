# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            queue =  deque([(p, q)])

            while queue:
                node1, node2 = queue.popleft()

                if node1.val != node2.val:
                    return False
                
                if (node1.left and not node2.left) or (not node1.left and node2.left):
                    return False

                if node1.left and node2.left:
                    queue.append((node1.left, node2.left))
                
                if (node1.right and not node2.right) or (not node1.right and node2.right):
                    return False
                
                if node1.right and node2.right:
                    queue.append((node1.right, node2.right))
            
            return True
            
        return bfs(p, q)
