class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) == self.limit:
            return 'error: list already full'
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
            
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit
        
        

    def search(self, target):
        if target not in self.items:
            return -1
        return len(self.items) - self.items.index(target) -1
