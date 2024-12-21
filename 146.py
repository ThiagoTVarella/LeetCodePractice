
class Node():
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None 
        self.right = None

class LRUCache:
    def __init__(self,cap):
        self.cap = cap
        self.leftmost = Node(0,0)
        self.rightmost = Node(0,0)
        self.leftmost.right = self.rightmost
        self.rightmost.left = self.leftmost
        self.n = 0
        self.node_dict = {}

    def remove(self,node):
        node.left.right = node.right
        node.right.left = node.left

    def append(self,node):
        node.left = self.rightmost.left
        node.right = self.rightmost
        self.rightmost.left.right = node 
        self.rightmost.left = node

    def get(self, key):
        # check if in dictionary. if it is, remove node from list, append to end, and return value
        if key in self.node_dict:
            self.remove(self.node_dict[key])
            self.append(self.node_dict[key])
            return self.node_dict[key].value
        else:
            return -1
    
    def put(self, key, value):
        # Check if in dictionary. if is, remove node from list, append to end, change value of node
        if key in self.node_dict:
            self.remove(self.node_dict[key])
            self.append(self.node_dict[key])
            self.node_dict[key].value = value
        else:
            new_node = Node(key,value)
            self.node_dict[key] = new_node
            self.append(self.node_dict[key])
            self.n += 1
            if self.n > self.cap:
                old_node = self.leftmost.right
                del self.node_dict[old_node.key]
                self.remove(old_node)
                self.n -= 1

                # self.leftmost.right = old_node.right
                # old_node.right.left = self.leftmost
        # If not, create node, and append to the right

        # check cap






















# # Define node
# class Node():
#     def __init__(self, key: int, value: int):
#         self.key = key
#         self.value = value
#         self.left = None
#         self.right = None

# class LRUCache:

# # Define remove function
#     def remove(self,node) -> None:
#         node.left.right = node.right
#         node.right.left = node.left

# # Define insert function
#     def insert(self,node) -> None:
#         node.left = self.RM.left
#         node.right = self.RM
#         self.RM.left.right = node
#         self.RM.left = node

#     def __init__(self, capacity: int):
#         # Define self.capacity, hash, leftmost and rightmost nodes
#         self.capacity = capacity
#         self.hashmap = {}
#         self.LM = Node(0,0)
#         self.RM = Node(0,0)

#         # Link the extreme nodes
#         self.LM.right = self.RM
#         self.RM.left = self.LM

#     def get(self, key: int) -> int:
#         # Check if in hash     
#         if key in self.hashmap:

#             # Define new node
#             new_node = Node(key,self.hashmap[key].value)

#             # Remove old node
#             self.remove(self.hashmap[key])
#             del self.hashmap[key]

#             # Place new node at top
#             self.insert(new_node)
#             self.hashmap[key] = new_node

#             # return value
#             return self.hashmap[key].value

#         # If not, return -1
#         else:
#             return -1   

#     def put(self, key: int, value: int) -> None:
#         # Define new node
#         new_node = Node(key,value)

#         # Check if in hash
#         if key in self.hashmap:

#             # Remove old node
#             self.remove(self.hashmap[key])
#             del self.hashmap[key]

#             # Insert new node
#             self.insert(new_node)
#             self.hashmap[key] = new_node
        
#         # If not in hash
#         else:
#             # Insert new node
#             self.insert(new_node)
#             self.hashmap[key] = new_node

#             # Check if exceeds capacity
#             if len(self.hashmap) > self.capacity:

#                 # Remove node at bottom
#                 del self.hashmap[self.LM.right.key]
#                 self.remove(self.LM.right)


        

# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.list = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.list:
            self.list.move_to_end(key)
            return self.list[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.list:
            self.list[key] = value
            self.list.move_to_end(key)
        else:
            self.list[key] = value
            if len(self.list) > self.cap:
                self.list.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# class Node:
#     def __init__(self, key: int, value: int):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None 

# class LRUCache:
#     def __init__(self, capacity: int):  
#         self.hash = {}
#         self.cap = capacity
#         self.left = Node(0,0)
#         self.right = Node(0,0)
#         self.right.prev = self.left
#         self.left.next = self.right

#     def insert(self, node):
#         node.prev = self.right.prev 
#         node.next = self.right
#         self.right.prev.next = node 
#         self.right.prev = node
#         self.hash[node.key] = node

#     def remove(self, node):
#         node.prev.next = node.next 
#         node.next.prev = node.prev
#         del self.hash[node.key] 

#     def get(self, key: int) -> int:
#         # Retrieve value from hash 
#         if key in self.hash:
#             curr_node = self.hash[key]
#             value = curr_node.value
#             new_node = Node(key,value)
#             # Remove node from current position
#             self.remove(curr_node)
#             # Append node to the rightmost element
#             self.insert(new_node)
#             # Return value if appropriate, otherwise -1
#             return value
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:
#         # Create new node
#         new_node = Node(key,value)
#         # Check if key exists and update value 
#         if key in self.hash:
#             curr_node = self.hash[key]
#             self.remove(curr_node)
#             self.insert(new_node)
#         else:
#             self.insert(new_node)
#             # If exceeded capacity, remove leftmost node
#             if len(self.hash) > self.cap:
#                 self.remove(self.left.next)