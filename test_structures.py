import unittest
from structures import Product, Stack, Queue, BinaryTree

class TestDataStructures(unittest.TestCase):

    def setUp(self):
        self.p1 = Product(1, "Manzana", 100, 50)
        self.p2 = Product(2, "Pera", 120, 30)
        self.p3 = Product(3, "Uva", 200, 20)

    def test_stack(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(self.p1)
        stack.push(self.p2)
        self.assertEqual(stack.peek(), self.p2)
        self.assertEqual(stack.pop(), self.p2)
        self.assertEqual(stack.pop(), self.p1)
        self.assertTrue(stack.is_empty())

    def test_queue(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        queue.enqueue(self.p1)
        queue.enqueue(self.p2)
        self.assertEqual(queue.peek(), self.p1) # FIFO
        self.assertEqual(queue.dequeue(), self.p1)
        self.assertEqual(queue.dequeue(), self.p2)
        self.assertTrue(queue.is_empty())

    def test_binary_tree(self):
        tree = BinaryTree()
        tree.insert(self.p2) # Root
        tree.insert(self.p1) # Left
        tree.insert(self.p3) # Right
        
        self.assertEqual(tree.search(2), self.p2)
        self.assertEqual(tree.search(1), self.p1)
        self.assertEqual(tree.search(3), self.p3)
        self.assertIsNone(tree.search(99))

    def test_edge_cases(self):
        # Empty Stack
        empty_stack = Stack()
        self.assertIsNone(empty_stack.pop())
        self.assertIsNone(empty_stack.peek())
        
        # Empty Queue
        empty_queue = Queue()
        self.assertIsNone(empty_queue.dequeue())
        self.assertIsNone(empty_queue.peek())
        
        # Empty Tree
        empty_tree = BinaryTree()
        self.assertIsNone(empty_tree.search(1))

if __name__ == '__main__':
    unittest.main()
