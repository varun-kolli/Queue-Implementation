
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''
    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.front = None
        self.rear = None
        self.capacity = capacity
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
        else:
            if not self.rear: #basically, if there's nothing there, the front and back are the same thing
                self.front = Node(item)
                self.rear = self.front
            else:
                self.rear.next = Node(item)
                self.rear = Node(item)
            self.count += 1

    def dequeue(self):
            '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
               If Queue is empty when dequeue is attempted, raises IndexError'''
            if self.is_empty():
                raise IndexError
            else:
                self.count -= 1
                if not self.front:
                    return None
                else:
                    ret = self.front.item
                    self.front = self.front.next
                    return ret




    def size(self):
            '''Returns the number of elements currently in the Queue, not the capacity'''
            return self.count

q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
#q = [1, 2, 3]


