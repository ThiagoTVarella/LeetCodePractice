# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TUDO ERRADO

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        current = root
        predecessor = None
        currNumber = 0
        sumNum = 0

        while current:

            # If not left child, go to the right
            if not current.left:
                currNumber = 10*currNumber + current.val
                if not current.right:
                    sumNum += currNumber
                current = current.right

            # If there's left child, compute predecessor
            else:
                predecessor = current.left
                steps = 1
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                    steps += 1

                # Set predecessor
                if predecessor.right is None:
                    predecessor.right = current
                    currNumber = 10*currNumber + current.val
                    current = current.left

                # Break predecessor
                else:
                    current = current.right
                    predecessor.right = None

                    if predecessor.left is None:
                        sumNum += currNumber

                    # Backtrack
                    while steps > 0:
                        currNumber = currNumber//10
                        steps -= 1

        return sumNum



        # path = root.val 
        # queue = deque([(root,path)])
        # final_sum = 0
        
        # while queue:
        #     aux = queue.popleft()
        #     node,path = aux[0],aux[1]

        #     if node.left is not None:
        #         new_path = 10*path + node.left.val
        #         queue.append((node.left,new_path))

        #     if node.right is not None:
        #         new_path = 10*path + node.right.val
        #         queue.append((node.right,new_path))

        #     if node.left is None and node.right is None:
        #         final_sum += path

        # return final_sum
