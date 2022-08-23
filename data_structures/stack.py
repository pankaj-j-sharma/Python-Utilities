from collections import deque

class Stack:

    def __init__(self) :
        self.buffer=deque()

    def push(self,data):
        self.buffer.append(data)

    def pop(self):
        return self.buffer.pop()

    def peek(self):
        return self.buffer[-1]

    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)


data = Stack()
data.push(12)
data.push(76)
data.push(91)
data.push(30)



