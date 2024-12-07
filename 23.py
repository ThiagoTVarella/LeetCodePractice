# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        O(N log(k)) for N the size of the longest list and k lists
        Example:
        [[1,5,7],[1,4,5],[2,9]]
        [[1,4,5,5,7],[1,4,5],[2,9]]
        [[1,2,4,5,5,7,9],[1,4,5],[2,9]]
        Return [1,2,4,5,5,7,9]
        '''

        k = len(lists)

        # Handling edge case
        if k == 0:
            return None

        # Divide and conquer
        step = 1
        while step < k:
            for i in range(0,k,2*step):
                if i+step < k:
                    lists[i] = self.merge2Lists(lists[i],lists[i+step])
            step *= 2
        
        return lists[0]

    def merge2Lists(self,l1,l2):
        '''
        O(N) for N the size of the longest list
        '''

        final = ListNode()
        curr = final

        # Two pointers merge
        while l1 and l2:

            if l1.val <= l2.val: 
                curr.next = l1
                l1 = l1.next
            else: 
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next

        # Handle rest of the list
        if l1 is None:
            curr.next = l2
        else:
            curr.next = l1

        return final.next
        













        # if not lists:
        #     return None

        # output = []
        # while True:

        #     min_val = float('inf')
        #     min_val_ind = -1

        #     for i,node in enumerate(lists):
        #         if node and node.val < min_val:
        #             min_val = node.val
        #             min_val_ind = i
            
        #     if min_val_ind != -1:
        #         output.append(lists[min_val_ind].val)
        #         lists[min_val_ind] = lists[min_val_ind].next
        #     else:
        #         break

        # if output:
        #     final_node = ListNode(val = output[-1])
        # else:
        #     final_node = None

        # aux_node = final_node
        # for i in range(len(output)-2,-1,-1):
        #     new_node = ListNode(val = output[i], next = aux_node)
        #     aux_node = new_node

        # return aux_node









        # k = len(lists)

        # lists_l = []

        # for i in range(len(lists)):
        #     if lists[i]:
        #         lista = lists[i]
        #         lists_aux = [lista.val]
        #         while lista.next:
        #             lists_aux.append(lista.next.val)
        #             lista = lista.next
        #         lists_l.append(lists_aux)

        # totlen = sum([len(li) for li in lists_l])
        # pts = [0 for li in lists_l]

        # output = []
        # root = None

        # while totlen > 0:
        #     find_min = float('inf')
        #     min_ind = 0
        #     for i in range(len(pts)):
        #         if pts[i] < len(lists_l[i]) and lists_l[i][pts[i]] < find_min:
        #             min_ind = i
        #             find_min = lists_l[i][pts[i]]
        #     if not output:
        #         prev = ListNode(find_min)
        #         root = prev
        #     else:
        #         next = ListNode(find_min)
        #         prev.next = next
        #         prev = next
        #     output.append(find_min)
        #     pts[min_ind] += 1
        #     totlen -= 1        
 
        # return root