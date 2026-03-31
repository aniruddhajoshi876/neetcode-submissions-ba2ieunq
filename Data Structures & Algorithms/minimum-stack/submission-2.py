class MinStack:

    def __init__(self):
        self.main = []
        self.extra=[]
        self.min = float('inf')
    def __str__(self):
        print(self.main)
        print(self.extra)
        return 'test...'
    def push(self, val: int) -> None:
        self.main.append(val)
        self.min = min(self.min, val)
        self.extra.append(self.min)

    def top(self) -> int:
        if not self.main: raise('Error')
        return self.main[-1]

    def getMin(self) -> int:
        if not self.main or not self.extra: raise('Error')
        return self.min

    def pop(self) -> None:
        if not self.main or not self.extra: raise('Error')
        self.main.pop()
        self.extra.pop()
        if self.extra:
            self.min = self.extra[-1]
        else:
            self.min=float('inf')