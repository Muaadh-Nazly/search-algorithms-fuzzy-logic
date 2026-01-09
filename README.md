# Artificial Intelligence - Search Algorithms & Fuzzy Logic

## 📋 Project Overview

This repository contains implementations of core Artificial Intelligence algorithms and techniques, demonstrating problem-solving methods, search algorithms, and fuzzy logic applications.


## 📁 Repository Structure

```
Search Algorithms & Fuzzy Logic/
├── README.md                          # This file
├── Search Algorithms/   # Search algorithm implementations
│   ├── search-algorithms.py                 # DFS and A* implementations
│   └── README.md                      # Search algorithms documentation
├── Fuzzy Logic/         # Fuzzy logic implementation
│   ├── fuzzy-logic.ipynb              # Jupyter notebook
└   └── README.md                     # Fuzzy logic documentation
```

## 🎯 Implemented Solutions

### Search Algorithms
Implementation of **Depth-First Search (DFS)** and **A\* Search** algorithms for solving maze pathfinding problems.

**Key Features:**
- Random maze generation (6x6 grid)
- DFS implementation with stack data structure
- A* search with Manhattan distance heuristic
- Path visualization and performance analysis
- Comparison of completeness, optimality, and time complexity


### Fuzzy Logic
Implementation of fuzzy logic system for error likelihood prediction and mitigation strategies.

**Key Features:**
- Fuzzy inference system using scikit-fuzzy
- Membership functions for input variables
- Rule-based decision making
- Error likelihood and mitigation strategies

## 🛠️ Technology Stack

### Search Algorithms
- **Language:** Python 3
- **Libraries:**
  - `tkinter` - GUI visualization
  - `random` - Maze generation
- **Algorithms:** DFS, A* (with Manhattan distance heuristic)

### Fuzzy Logic
- **Language:** Python 3
- **Libraries:**
  - `numpy` - Numerical computations
  - `scikit-fuzzy` - Fuzzy logic implementation
- **Framework:** Fuzzy Control System



### Prerequisites
- Python 3.7 or higher
- Required Python packages (see individual question READMEs)


## 🔍 Key Algorithms

### Depth-First Search (DFS)
- **Data Structure:** Stack (LIFO)
- **Completeness:** Yes (if solution exists)
- **Optimality:** No (may not find shortest path)
- **Time Complexity:** O(b^m) where b is branching factor, m is max depth

### A* Search
- **Data Structure:** Priority Queue
- **Heuristic:** Manhattan Distance
- **Completeness:** Yes
- **Optimality:** Yes (with admissible heuristic)
- **Time Complexity:** O(b^d) where b is branching factor, d is solution depth

### Fuzzy Logic System
- **Input Variables:** Data redundancy, degradation level, error history
- **Output Variables:** Error likelihood, error mitigation
- **Inference:** Rule-based fuzzy inference
- **Defuzzification:** Center of gravity method

## 📈 Performance Analysis

### Search Algorithm Comparison
- **DFS:** Explores deeply, may explore many nodes
- **A*:** More efficient with heuristic guidance
- **Analysis:** Included in Question 3 implementation
