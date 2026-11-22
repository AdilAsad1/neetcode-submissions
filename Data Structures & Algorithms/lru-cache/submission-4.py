class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.right = Node(0,0)
        self.left = Node(0,0)
        #left is least recently used, right is most recently used
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        #if key exists update the value, otherwise add the key value in cache, if the cap goes over remove the lru
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
    
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


    def remove(self,node):
        #head -> n1 -> n2 -> node -> tail
        a = node.prev
        b = node.next
        a.next, b.prev = b, a
    
    def insert(self, node):
        #head -> n1 -> n2 -> node -> tail
        #tail.prev.next = node
        #node.prev = tail.prev.next
        #node.next = tail
        #tail.prev = node
        a = self.right.prev
        a.next, node.prev = node, a
        node.next, self.right.prev = self.right, node 
        
