"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from collections import standardDict

class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # Handle edge cases
        if not head:
            return head 
        
        # Create a list of cloned to reference to check if node has been
        #  cloned and access the cloned node
        cloned = {}
        new_head = Node(head.val)
        cloned[head] = new_head

        # Iterate through the list.
        while head:

            # every node not on cloned, create new node with null pointers. 
            #  if pointer has been cloned, assign them.
            if head.next and head.next in cloned: cloned[head].next = cloned[head.next]
            elif head.next: cloned[head].next = cloned[head.next] = Node(head.next.val)

            if head.random and head.random in cloned: cloned[head].random = cloned[head.random]
            elif head.random: cloned[head].random = cloned[head.random] = Node(head.random.val)

            head = head.next

        return new_head
#       ___
#\/    /   \
# 1 -> 2 -> 3 -> 
#  \_______/

# head = 3
# cloned: 1,2
# new_1.val,.next,.random
# new_2.val,.next,.random
# new_3.val,.random





        # if not head:
        #     return None

        # hash_orig = {}
        
        # head2 = Node(head.val)
        # hash_orig[head] = head2

        # prev = head2
        # node = head.next

        # forwards = {}

        # if head.random != head:
        #     forwards[head] = head.random
        # else:
        #     head2.random = head2

        # while node:
        #     new = Node(node.val)
        #     hash_orig[node] = new

        #     prev.next = new

        #     random_orig = node.random
        #     if random_orig in hash_orig:
        #         new.random = hash_orig[random_orig]
        #     else:
        #         forwards[node] = random_orig

        #     node = node.next
        #     prev = new

        # node = head
        # while node:
        #     if node in forwards:
        #         if node.random:
        #             hash_orig[node].random = hash_orig[node.random]
        #     node = node.next
        
        # return head2