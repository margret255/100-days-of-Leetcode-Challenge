class Stack:
    def __init__(self, capacity=100):
        self.stack = []
        self.capacity = capacity

    def push(self, item):
        if len(self.stack) >= self.capacity:
            raise OverflowError("Stack is full!")
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack!")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack!")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity