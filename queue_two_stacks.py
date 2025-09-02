class Queue:
    def __init__(self):
        self.stack1 = []  # used for enqueue
        self.stack2 = []  # used for dequeue
        self.size_ = 0

    def enqueue(self, val):
        # Always push to stack1
        self.stack1.append(val)
        self.size_ += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        # If stack2 is empty, move everything from stack1
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        self.size_ -= 1
        return self.stack2.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def is_empty(self):
        return self.size_ == 0

    def get_size(self):
        return self.size_
