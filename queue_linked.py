class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class Queue:
    '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.rear = None
        self.front = None
        self.count = 0


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        return self.count == 0


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        return self.count == self.capacity


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue
                   If Queue is full when enqueue is attempted, raises IndexError'''
        if self.is_full():
            raise IndexError

        if self.front == None:
            self.front = Node(item)
            self.rear = self.front
            self.count += 1

        else:
            node = Node(item)
            self.rear.next = node
            self.rear = node
            self.count += 1


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
                 If Queue is empty when dequeue is attempted, raises IndexError'''

        if self.is_empty():
            raise IndexError
        else:
            node = self.front
            self.front = node.next
            self.count -= 1

        return node.item


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.count
