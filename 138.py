"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None

        hash_orig = {}
        
        head2 = Node(head.val)
        hash_orig[head] = head2

        prev = head2
        node = head.next

        forwards = {}

        if head.random != head:
            forwards[head] = head.random
        else:
            head2.random = head2

        while node:
            new = Node(node.val)
            hash_orig[node] = new

            prev.next = new

            random_orig = node.random
            if random_orig in hash_orig:
                new.random = hash_orig[random_orig]
            else:
                forwards[node] = random_orig

            node = node.next
            prev = new

        node = head
        while node:
            if node in forwards:
                if node.random:
                    hash_orig[node].random = hash_orig[node.random]
            node = node.next
        
        return head2