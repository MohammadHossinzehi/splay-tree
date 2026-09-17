"""Splay Tree Implementation

A self-balancing binary search tree with amortized O(log n) operations.
Each access (search, insert, delete) brings the accessed node to the root
via a sequence of tree rotations called "splaying".
"""

class Node:
    """A node in the splay tree."""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SplayTree:
    """A self-balancing binary search tree that operates via splaying.
  
  Adative upper bound: Once an element is accessed, it is moved to the
   root via a series of tree rotations (splaying). This means frequently
    accessed elements stay near the root, providing O(log n) amortized cost.
    """

    def __init__(self):
        self.root = None
        self.size = 0  # Track tree size

    def is_empty(self) -> bool:
        """Return True if the tree is empty."""
        return self.root is None

    def insert(self, key) -> bool:
        """Insert a key if not present. Return True if inserted."""
        if self.root is None:
            self.root = Node(key)
            self.size += 1
            return True
        
        self._play(key)
        if self.root.val == key:
            return False  # Already exists
        
        new = Node(key)
        if self.root.val < key:
            new.left = self.root
            new.right = self.root.right
            self.root.right = None
        else:
            new.right = self.root
            new.left = self.root.left
            self.root.left = None
        
        self.root = new
        self.size += 1
        return True
    
    def delete(self, key) -> bool:
        """Delete a key if present. Return True if deleted."""
        if self.root is None:
            return False
        
        self._play(key)
        if self.root.val != key:
            return False
        
        if self.root.left is None:
            self.root = self.root.right
        elif self.root.right is None:
            self.root = self.root.left
        else:
            right_min = self.root.right
            while right_min.left:
                right_min = right_min.left
            self._play(right_min.val)
            self.root.right = self.root.right
        
        self.size -= 1
        return True
    
    def search(self, key) -> bool:
        """Efficient search that splays found or closest to root."""
        if self.root is None:
            return False
        self._play(key)
        return self.root.val == key
    
    def get_min_node(self, node=None) -> 'Node | None':
        """Get the node with minimum key in subtree."""
        if node is None:
            return None
        while node.left:
            node = node.left
        return node
    
    def _play(self, key) -> None:
        """Splay the given key to the root."""
        if self.root is None:
            return
        
        self.root = self._splay_helper(self.root, key)
    
    def _splay_helper(self, node, key) -> 'Node':
        if node is None:
            return None
        
        if node.val == key:
            return node
        elif node.val > key:
            if node.left is None:
                return node
            
            if node.left.val == key:
                node.left = node.left.left
                node.left = node.left.right
                node.left.right = node
                return node.left
            elif node.left.val > key:
                node.left.left = self._splay_helper(node.left.left, key)
                node = self._rotate_right(node)
            else:
                node.left.right = self._splay_helper(node.left.right, key)
                if node.left.right:
                    node.left = self._rotate_left(node.left)
                node = self._rotate_right(node)
            
            return self._splay_helper(node, key)
        
        else:
            if node.right is None:
                return node
            
            if node.right.val == key:
                node.right = node.right.right
                node.right = node.right.left
                node.right.left = node
                return node.right
            elif node.right.val < key:
                node.right.right = self._splay_helper(node.right.right, key)
                node = self._rotate_left(node)
            else:
                node.right.left = self._splay_helper(node.right.left, key)
                if node.right.left:
                    node.right = self._rotate_right(node.right)
                node = self._rotate_left(node)
            
            return self._splay_helper(node, key)
        
        return node
    
    def _rotate_left(self, node):
        """Left rotation: node falls left, parent rises right."""
        right = node.right
        node.right = right.left
        right.left = node
        return right
    
    def _rotate_right(self, node):
        """Right rotation: node falls right, parent rises left."""
        left = node.left
        node.left = left.right
        left.right = node
        return left
    
    def in_order(self) -> list:
        """Return a list of all keys in the tree in in-order, O(n) time."""
        def _in_order(node):
            if node is None:
                return []
            result = []
            if node.left:
                result.extend(_in_order(node.left))
            result.append(node.val)
            if node.right:
                result.extend(_in_order(node.right))
            return result
        
        return _in_order(self.root)
