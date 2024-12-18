# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(root):

            if not root:
                return (0,0)

            path_left,max_diameter_left = dfs(root.left)
            path_right,max_diameter_right = dfs(root.right)

            max_diameter = max([max_diameter_left,max_diameter_right,path_left+path_right])

            return max(path_left,path_right)+1,max_diameter

        path,diameter = dfs(root)
        return diameter







        # diameter = 0

        # def dfs(node):

        #     nonlocal diameter

        #     if not node:
        #         return -1

        #     height_left = dfs(node.left)
        #     height_right = dfs(node.right)

        #     diameter = max(diameter)

        #     return 







        # maximum = 0

        # def dfs(node)-> int:

        #     nonlocal maximum

        #     if not node:
        #         return -1

        #     d_left = dfs(node.left)
        #     d_right = dfs(node.right)

        #     maximum = max(maximum,d_left+d_right+2)

        #     return max(d_left,d_right)+1

        # dfs(root)
            
        # return maximum