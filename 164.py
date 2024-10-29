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

        self.leftmost = Node(0,0)
        self.rightmost = Node(0,0)
        self.leftmost.next = self.rightmost
        self.rightmost.prev = self.leftmost

    def remove(self, node):
        del self.hash[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        self.hash[node.key] = node
        node.prev = self.rightmost.prev
        node.next = self.rightmost
        self.rightmost.prev.next = node
        self.rightmost.prev = node

    def get(self, key: int) -> int:
        if key in self.hash:
            new_node = self.hash[key]
            self.remove(self.hash[key])
            self.insert(new_node)
            return self.hash[key].value
        else:
            return -1        

    def put(self, key: int, value: int) -> None:
        new_node = Node(key,value)
        if key in self.hash:
            self.remove(self.hash[key])
            self.insert(new_node)
        else:
            if len(self.hash) >= self.cap:
                self.remove(self.leftmost.next)
            self.insert(new_node)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)