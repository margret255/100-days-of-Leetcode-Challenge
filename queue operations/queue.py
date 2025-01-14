class Queue:
    def __init__(self, capacity=100):
        self.queue = []
        self.capacity = capacity

    def enqueue(self, item):
        if len(self.queue) >= self.capacity:
            raise OverflowError("Queue is full!")
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue!")
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue!")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity