# Search Algorithms - Maze Pathfinding

## 📋 Overview

Implementation of **Depth-First Search (DFS)** and **A\* Search** algorithms for solving pathfinding problems in a randomly generated 6x6 maze.

## 🎯 Objectives

- Implement DFS algorithm for maze traversal
- Implement A* search algorithm with Manhattan distance heuristic
- Compare algorithm performance (completeness, optimality, time complexity)
- Visualize maze solving process

## 🏗️ Maze Structure

### Grid Layout
- **Size:** 6x6 grid (36 nodes total)
- **Starting Node:** Randomly selected from nodes 0-11 (first two columns)
- **Goal Node:** Randomly selected from nodes 24-35 (last two columns)
- **Barriers:** 4 randomly placed barrier nodes
- **Movements:** Horizontal, vertical, and diagonal (8-directional)

### Node Representation
- `S` - Start node
- `G` - Goal node
- `X` - Barrier (blocked)
- ` ` - Empty (traversable)

## 🔍 Algorithms Implemented

### 1. Depth-First Search (DFS)

**Data Structure:** Stack (LIFO - Last In First Out)

**Algorithm:**
1. Push start node onto stack
2. While stack is not empty:
   - Pop node from stack
   - If node is goal, return path
   - Mark node as visited
   - Push unvisited neighbors onto stack (in increasing order)
3. Return path if found, else no solution

**Characteristics:**
- **Completeness:** ✅ Yes (if solution exists)
- **Optimality:** ❌ No (may not find shortest path)
- **Time Complexity:** O(b^m) where b = branching factor, m = max depth
- **Space Complexity:** O(bm)

### 2. A* Search

**Data Structure:** Priority Queue (based on f(n) = g(n) + h(n))

**Heuristic Function:** Manhattan Distance
```
d(N, G) = |N_x - G_x| + |N_y - G_y|
```

Where:
- `N_x, N_y` = Current node coordinates
- `G_x, G_y` = Goal node coordinates

**Algorithm:**
1. Initialize open set with start node (f = 0 + h(start))
2. While open set is not empty:
   - Select node with lowest f(n) value
   - If node is goal, return path
   - Add node to closed set
   - For each neighbor:
     - Calculate g(n) = cost from start
     - Calculate h(n) = Manhattan distance to goal
     - Calculate f(n) = g(n) + h(n)
     - Add to open set if not visited or better path found
3. Return path if found, else no solution

**Characteristics:**
- **Completeness:** ✅ Yes
- **Optimality:** ✅ Yes (with admissible heuristic)
- **Time Complexity:** O(b^d) where b = branching factor, d = solution depth
- **Space Complexity:** O(b^d)

## 📊 Implementation Details

### Data Structures

#### Stack Class (for DFS)
```python
class Stack:
    - push(item)      # Add to top
    - pop()           # Remove from top
    - is_empty()      # Check if empty
    - peek()          # View top without removing
    - is_available()  # Check if value exists
```

### Key Functions

#### `is_valid_move(x, y)`
- Checks if coordinates are within bounds
- Verifies node is not a barrier
- Ensures node is not the start node

#### `get_neighbors(x, y)`
- Returns all valid neighboring nodes
- Processes neighbors in increasing order
- Supports 8-directional movement (horizontal, vertical, diagonal)

#### `dfs()`
- Implements DFS algorithm
- Tracks visited nodes
- Reconstructs path using `came_from` dictionary
- Returns visited list, path, and time taken

#### `manhattan_distance(node, goal)`
- Calculates Manhattan distance heuristic
- Used in A* search for path cost estimation

#### `a_star_search()`
- Implements A* algorithm
- Uses priority queue for node selection
- Tracks g(n), h(n), and f(n) values
- Returns visited list, path, and time taken


### Program Flow

1. **Maze Generation:**
   - Randomly selects start node (0-11)
   - Randomly selects goal node (24-35)
   - Randomly places 4 barriers
   - Displays initial maze

2. **DFS Execution:**
   - Runs DFS algorithm
   - Displays visited nodes
   - Shows final path
   - Calculates time taken

3. **A* Execution:**
   - Runs A* algorithm
   - Displays visited nodes
   - Shows final path
   - Calculates time taken

4. **Comparison:**
   - Compares visited nodes count
   - Compares path length
   - Compares time complexity

## 📈 Performance Analysis

### Typical Results

| Algorithm | Visited Nodes | Path Length | Time (minutes) |
|-----------|--------------|-------------|----------------|
| DFS       | Variable     | May be long | Higher         |
| A*        | Fewer        | Optimal     | Lower          |

### Key Observations

1. **DFS:**
   - Explores deeply before backtracking
   - May visit many nodes before finding goal
   - Path may not be optimal

2. **A*:**
   - Guided by heuristic, explores fewer nodes
   - Always finds optimal path (with admissible heuristic)
   - More efficient for pathfinding problems

## 🔧 Configuration

### Maze Parameters
```python
rows = 6          # Number of rows
columns = 6        # Number of columns
barrier_count = 4  # Number of barriers
```

### Movement Rules
- **Valid Moves:** Horizontal, vertical, diagonal
- **Invalid Moves:** Through barriers, outside bounds
- **Cost:** All edges have equal cost (1 minute per node)

## 📝 Code Structure

```python
# Maze setup
- Random start/goal selection
- Barrier placement
- Grid initialization

# DFS Implementation
- Stack data structure
- Visited tracking
- Path reconstruction

# A* Implementation
- Priority queue
- Heuristic calculation
- Cost tracking

# Visualization
- Tkinter GUI
- Console output
```

## 🧪 Testing

The program runs three iterations with different random mazes to:
- Verify algorithm correctness
- Compare performance across different scenarios
- Analyze completeness and optimality

### Test Cases
1. **Maze 1:** Random configuration
2. **Maze 2:** Random configuration
3. **Maze 3:** Random configuration

