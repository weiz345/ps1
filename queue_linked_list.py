class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, val):
        # TODO: Implement
        pass

    def dequeue(self):
        # TODO: Implement
        pass

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.val

    def is_empty(self):
        # TODO: Implement
        pass

    def get_size(self):
        return self.size
    
    