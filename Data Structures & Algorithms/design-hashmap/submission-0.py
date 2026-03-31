class MyHashMap:

    def __init__(self):
        self.data = []

    def put(self, key: int, value: int) -> None:
        for i in self.data:
            if i[0] == key:
                i[1] = value
                return
        self.data.append([key, value])

    def get(self, key: int) -> int:
        for i in self.data:
            if i[0] == key:
                return i[1]
        return -1
        
    
    def remove(self, key: int) -> None:
            for i in self.data:
                 if i[0] == key:
                      self.data.remove(i)