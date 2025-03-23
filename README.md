# Algorithm Repository

## Overview
This repository contains implementations of various algorithms, starting with pathfinding algorithms like **A* (A-Star)** and **IDA* (Iterative Deepening A-Star)**. Each algorithm is organized into its own directory containing the necessary components to execute the simulation.

## Directory Structure
```
/algorithms-repo
│── A*
│   ├── agent.py          # Implementation of the A* agent
│   ├── environment.py    # Defines the grid-based environment
│   ├── main.py           # Runs the A* simulation using Pygame
│
│── IDA*
│   ├── agent.py          # Implementation of the IDA* agent
│   ├── environment.py    # Defines the grid-based environment
│   ├── main.py           # Runs the IDA* simulation using Pygame
│
│── README.md             # Documentation
```

## Implemented Algorithms
- **A* (A-Star) Algorithm**: A heuristic-based search algorithm that finds the shortest path using a cost function combining the path cost and an estimated heuristic.
- **IDA* (Iterative Deepening A-Star) Algorithm**: A memory-efficient variation of A* that performs iterative deepening with a cost threshold to find the optimal path.

## How to Run
1. Clone this repository:
   ```sh
   git clone https://github.com/Rakib013/CSE-366.git
   cd CSE-366 
   ```
2. Install dependencies:
   ```sh
   pip install pygame
   ```
3. Run the simulations:
   - To run A*:
     ```sh
     cd A*
     python main.py
     ```
   - To run IDA*:
     ```sh
     cd ../IDA*
     python main.py
     ```

