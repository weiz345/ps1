class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.front = None   # first node
        self.rear = None    # last node
        self.size = 0       # number of items

    def enqueue(self, val):
        new_node = ListNode(val)
        if self.is_empty():
            # both front and rear point to new node
            self.front = self.rear = new_node
        else:
            # attach new node at rear and update rear
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self.front.val
        self.front = self.front.next
        # if queue becomes empty, rear must also be None
        if self.front is None:
            self.rear = None
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.val

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size
