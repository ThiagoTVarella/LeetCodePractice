# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        level = 0
        queue = deque([(root,level)])
        side = []
        levels = set()

        while queue:
            node,level = queue.popleft()
            if node:
                if level not in levels:
                    side.append(node.val)
                    levels.add(level)
                queue.append((node.right,level+1))
                queue.append((node.left,level+1))

        return side