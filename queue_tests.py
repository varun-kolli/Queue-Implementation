import unittest

from queue_array import Queue
from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_empty(self):
        q = Queue(5)
        q.enqueue(1)
        q.dequeue()
        self.assertTrue(q.is_empty())


    def test_full(self):
        q = Queue(1)
        q.enqueue(1)
        self.assertTrue(q.is_full())


    def test_enq_error(self):
        q = Queue(1)
        q.enqueue(1)
        with self.assertRaises(IndexError):
            q.enqueue(6)

    def test_enq_none_cond(self):
        q = Queue(1)
        q.enqueue(1)
        self.assertEqual(q.front, q.rear)

    def test_enq(self):
        q = Queue(3)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)

    def test_dq_error(self):
        q = Queue(1)
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_dq(self):
        q = Queue(3)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.dequeue()
        self.assertEqual(q.dequeue(), 2)


    def test_dq_ret(self):
        q = Queue(3)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        #self.assertEqual(q.dequeue(), 3)


    def test_size(self):
        q = Queue(3)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.size(), 3)


if __name__ == '__main__': 
    unittest.main()
