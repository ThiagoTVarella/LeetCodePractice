# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        

        # root is median, which is len(n)//2
        beg = 0     # 0
        top = len(nums)-1 # 2
        median_index = (len(nums)-1)//2 # 1

        # create the root
        root = TreeNode(val = nums[median_index])

        # queue 
        queue = deque([(median_index,beg,top,root)])
        # divide in 2 sublists, and take new medians
        while queue:
            (median_index,beg,top,node) = queue.popleft()
            median_left = (beg+median_index-1)//2 # 0
            median_right = (median_index+1+top)//2 # 1


            if beg < median_index and beg <= median_left <= median_index:
                new_node = TreeNode(val = nums[median_left])
                node.left = new_node
                new_tuple = (median_left,beg,median_index-1,new_node)
                queue.append(new_tuple)

            if median_index < top and median_index <= median_right <= top:
                new_node = TreeNode(val = nums[median_right])
                node.right = new_node
                new_tuple = (median_right,median_index+1,top,new_node)
                queue.append(new_tuple)
            
        return root
