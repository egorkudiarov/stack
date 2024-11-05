class Stack:
    def __init__(self):
        self.counter = -1
        self.stack = {}
    
    def is_empty(self) -> bool:
        return self.counter == -1

    def push(self, element):
        self.counter += 1
        self.stack.setdefault(self.counter, element)

    def pop(self):
        element = self.stack.pop(self.counter)
        self.counter -= 1
        return element

    def peek(self):
        element = self.stack.get(self.counter)
        return element

    def size(self) -> int:
        return self.counter + 1