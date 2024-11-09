# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        qu = deque()
        qu.append((root,None,''))
        root.binary = ''
        find = 2

        while find > 0 and qu:
            node,parent,add = qu.popleft()
            if node.left:
                qu.append((node.left,node,'0'))
            if node.right:
                qu.append((node.right,node,'1'))
            node.parent = parent

            if parent:
                node.binary = node.parent.binary + add

            if node == p or node == q:
                find -= 1
        print(find)

        pb,qb = p.binary,q.binary
        n = min(len(pb),len(qb))
        ans_bin = ''
        i = 0
        while i < n and pb[i] == qb[i]:
            ans_bin += pb[i]
            i += 1

        node = root
        for elem in ans_bin:
            if elem == '1':
                node = node.right
            elif elem == '0':
                node = node.left
        
        return node