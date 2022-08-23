from collections import deque

class Queue:
    def __init__(self):
        self.buffer=deque()

    def enqueue(self,data):
        self.buffer.appendleft(data)

    def dequeue(self):
        self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)


data = Queue()
data.enqueue(12)
data.enqueue(76)
data.enqueue(91)
data.enqueue(30)
data.dequeue()