"""Comprehensive test suite for Splay Tree implementation."""
import unittest
from splay_tree import SplayTree, Node


class TestSplayTreeBasics(unittest.TestCase):
    """Test basic operations: insert, search, delete."""

    def setUp(self):
        self.tree = SplayTree()

    def test_empty_tree(self):
        """Test properties of empty tree."""
        self.assertTrue(self.tree.is_empty())
        self.assertEqual(self.tree.size, 0)
        self.assertFalse(self.tree.search(5))

    def test_single_insert(self):
        """Test insertion of single element."""
        self.assertTrue(self.tree.insert(10))
        self.assertFalse(self.tree.is_empty())
        self.assertEqual(self.tree.size, 1)
        self.assertTrue(self.tree.search(10))

    def test_duplicate_insert(self):
        """Test that duplicate insertions return False."""
        self.assertTrue(self.tree.insert(10))
        self.assertFalse(self.tree.insert(10))
        self.assertEqual(self.tree.size, 1)

    def test_multiple_inserts(self):
        """Test insertion of multiple elements."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for v in values:
            self.assertTrue(self.tree.insert(v))
        self.assertEqual(self.tree.size, 7)
        for v in values:
            self.assertTrue(self.tree.search(v))

    def test_search_nonexistent(self):
        """Test searching for non-existent elements."""
        self.tree.insert(10)
        self.tree.insert(20)
        self.assertFalse(self.tree.search(15))
        self.assertFalse(self.tree.search(100))

    def test_delete_empty(self):
        """Test deletion from empty tree."""
        self.assertFalse(self.tree.delete(10))

    def test_delete_single(self):
        """Test deletion of single element."""
        self.tree.insert(10)
        self.assertTrue(self.tree.delete(10))
        self.assertTrue(self.tree.is_empty())
        self.assertEqual(self.tree.size, 0)

    def test_delete_nonexistent(self):
        """Test deletion of non-existent element."""
        self.tree.insert(10)
        self.assertFalse(self.tree.delete(20))
        self.assertEqual(self.tree.size, 1)

    def test_delete_with_children(self):
        """Test deletion of nodes with children."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for v in values:
            self.tree.insert(v)
        
        self.assertTrue(self.tree.delete(50))
        self.assertEqual(self.tree.size, 6)
        self.assertFalse(self.tree.search(50))
        
        self.assertTrue(self.tree.delete(30))
        self.assertEqual(self.tree.size, 5)

    def test_in_order_traversal(self):
        """Test in-order traversal returns sorted keys."""
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65]
        for v in values:
            self.tree.insert(v)
        
        result = self.tree.in_order()
        self.assertEqual(result, sorted(values))
        self.assertEqual(len(result), len(values))

    def test_large_insertions(self):
        """Test with large number of insertions."""
        n = 1000
        for i in range(n):
            self.assertTrue(self.tree.insert(i))
        
        self.assertEqual(self.tree.size, n)
        self.assertTrue(self.tree.search(0))
        self.assertTrue(self.tree.search(n // 2))
        self.assertTrue(self.tree.search(n - 1))


if __name__ == '__main__':
    unittest.main()
