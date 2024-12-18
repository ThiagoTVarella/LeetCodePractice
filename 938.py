# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        '''
        O(n) time complexity, O(log(n)) space complexity
        Example:
        Input: root = [5, 3, 6], low = 4, high = 6
        root.val = 5, within range, return 5+sum of both
        left side is lower, return right, which is 0, so left side is 0
        right side is within range, return 6+sum of both, both of which are empty
        so back to root, return is 5+0+6
        Output: 11 
        '''
        
        # Depth-first search
        def range_sum_dfs(node):

            if not node:
                return 0

            # If node within range, check both branches
            if low <= node.val <= high: return node.val+dfs(node.left)+dfs(node.right)
            # If node lower, check right branch, eliminating unnecessary traversal
            elif node.val < low: return dfs(node.right)
            # If node higher, check left branch, eliminating unnecessary traversal
            else: return dfs(node.left)

        return range_sum_dfs(root)




        # queue = deque()
        # queue.append(root)

        # add = 0

        # while queue:
        #     node = queue.popleft()
           
        #     if low <= node.val <= high:
        #         add += node.val
        #         if node.left: queue.append(node.left)
        #         if node.right: queue.append(node.right)
        #     elif node.val < low and node.right:
        #         queue.append(node.right)
        #     elif node.val > high and node.left:
        #         queue.append(node.left)
            
        # return add
            
