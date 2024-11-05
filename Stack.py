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
        self.counter -= 1
        return element

    def size(self) -> int:
        return self.counter + 1


"""
is_empty — проверка стека на пустоту. Метод возвращает True или False;
push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
size — возвращает количество элементов в стеке.
"""
