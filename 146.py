class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None 

class LRUCache:
    def __init__(self, capacity: int):  
        self.hash = {}
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.right.prev = self.left
        self.left.next = self.right

    def insert(self, node):
        node.prev = self.right.prev 
        node.next = self.right
        self.right.prev.next = node 
        self.right.prev = node
        self.hash[node.key] = node

    def remove(self, node):
        node.prev.next = node.next 
        node.next.prev = node.prev
        del self.hash[node.key] 

    def get(self, key: int) -> int:
        # Retrieve value from hash 
        if key in self.hash:
            curr_node = self.hash[key]
            value = curr_node.value
            new_node = Node(key,value)
            # Remove node from current position
            self.remove(curr_node)
            # Append node to the rightmost element
            self.insert(new_node)
            # Return value if appropriate, otherwise -1
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Create new node
        new_node = Node(key,value)
        # Check if key exists and update value 
        if key in self.hash:
            curr_node = self.hash[key]
            self.remove(curr_node)
            self.insert(new_node)
        else:
            self.insert(new_node)
            # If exceeded capacity, remove leftmost node
            if len(self.hash) > self.cap:
                self.remove(self.left.next)