# Splay Tree

A production-grade implementation of a self-balancing binary search tree with adaptive amortized O(log n) operations.

## What is a Splay Tree?

A **Splay Tree** is a self-balancing BST that uses a novel technique called *splaying* to keep frequently accessed elements near the root. When any element is accessed (via search, insert, or delete), it is moved to the root through a sequence of tree rotations:

- **Zig step**: Single rotation when element's parent is the root
- **Zig-zig step**: Two rotations of the same type (LL or RR)
- **Zig-zag step**: Two rotations of different types (LR or RL)

This adaptive strategy means that frequently used data is optimized automatically over time.

## Key Properties

- **Amortized Time Complexity**: O(log n) for search, insert, delete
- **Adaptive**: Frequently accessed nodes stay near the root
- **No Balance Factor**: Unlike AVL trees, no explicit balance maintenance needed
- **Cache-Friendly**: Locality of reference improves cache hit rates
- **Simple Rotations**: Only two operations needed (left/right rotate)

## Features

- Clean, production-ready implementation
- Comprehensive test suite with 40+ test cases
- Support for basic operations: insert, search, delete
- In-order traversal for sorted key extraction
- Size tracking for O(1) cardinality queries

## Installation & Usage

Clone the repository and import the module:

```python
from splay_tree import SplayTree

tree = SplayTree()

# Insert elements
tree.insert(50)
tree.insert(30)
tree.insert(70)

# Search (brings element to root if found)
found = tree.search(30)  # True

# Delete element
tree.delete(30)

# Get all elements in sorted order
keys = tree.in_order()  # [50, 70]
```

## Design & Implementation Notes

### Splaying Algorithm
The core splaying operation recursively restructures the tree by moving the target key to the root. Three cases handle different scenarios:

1. **Zig** (y is root): Single rotation
2. **Zig-Zig** (y-x in same direction): Double rotation same type
3. **Zig-Zag** (y-x in different directions): Double rotation alternating types

After recursive splaying of subtree containing key, additional rotations complete the operation.

### Why This Design?

- **Adaptive Amortized Bound**: No worst-case O(n) lookups if same keys accessed repeatedly
- **Simplicity**: Minimal invariants vs. AVL/RB trees; no balance factor management
- **Competitive**: Empirically faster than AVL/RB for many access patterns
- **Natural LRU Behavior**: Frequently used elements automatically move upward

## Testing

Run the comprehensive test suite:

```bash
python test_splay_tree.py
```

Tests cover:
- Empty tree operations
- Single and multiple insertions
- Duplicate detection
- Searching and non-existent keys
- Deletion with various node configurations
- In-order traversal correctness
- Large-scale insertions (1000+ elements)
- Rotation mechanics (left, right, zig-zag patterns)
- Tree connectivity and size tracking
- Adaptive access patterns

## Performance Characteristics

| Operation | Amortized | Worst-Case |
|-----------|-----------|-----------|
| Search    | O(log n)  | O(log n)  |
| Insert    | O(log n)  | O(log n)  |
| Delete    | O(log n)  | O(log n)  |

Empirical testing shows that with clustered access patterns (same keys accessed frequently), Splay Trees often outperform balanced BSTs due to adaptive repositioning.

## Files

- `splay_tree.py` - Core implementation (SplayTree class and Node)
- `test_splay_tree.py` - Comprehensive unit test suite

## References

- Sleator & Tarjan (1985): Self-Adjusting Binary Search Trees
- Original paper established O(log n) amortized bound

## License

MIT License

## Author

Mohammad Hossinzehi
