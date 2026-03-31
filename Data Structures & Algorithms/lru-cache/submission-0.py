class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
    def show_cache(self):
        curr = self.head.next
        result = []
        while curr != self.tail:
            result.append((curr.key, curr.val))   # or (curr.key, curr.value)
            curr = curr.next
        print("Cache (LRU → MRU):", result)

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        last = self.tail.prev
        last.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = last
    def get(self, key):
        if key not in self.map: return -1

        node = self.map[key]
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key, value):

        #already exists

        if key in self.map:
            
            node = self.map[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            return
        #doesnt exist
        node = Node(key,value)
        self.insert(node)
        self.map[key] = node

        #check capacity
        if len(self.map) > self.capacity:
            least = self.head.next
            self.remove(least)
            del self.map[least.key]