# Id and Name

- **Name**: Lensa Beshada
- **Id**: UGR/9635/16

## Loom Video Link



# Maze Generator and Solver

A Python program that generates and solves mazes using Pygame for visualization.

## Features

- **Maze Generation**: Uses stack-based Depth-First Search (DFS) algorithm to create perfect mazes
- **Maze Solving**: Implements backtracking algorithm to find the path from start to end
- **Animations**: Visualizes both generation and solving processes
- **Data Structures**: Uses 2D arrays for wall representation (north_wall and east_wall)
- **Bonus Cycles**: Randomly removes extra walls to create loops, demonstrating limitations of wall-following algorithms

## Maze Generation Logic

The maze is generated using a recursive backtracking (stack-based DFS) algorithm:

1. Start from a random cell
2. Mark the cell as visited
3. While there are unvisited cells:
   - Get unvisited neighbors of current cell
   - If neighbors exist:
     - Choose one randomly
     - Remove the wall between current and chosen cell
     - Mark chosen cell as visited
     - Push chosen cell to stack
   - If no neighbors:
     - Pop current cell from stack (backtrack)

This creates a "perfect" maze with no loops and exactly one path between any two cells.

After generation, the bonus feature randomly removes additional walls (1 in 20 chance) to introduce cycles. This makes the maze imperfect and shows why simple wall-following algorithms (like the right-hand rule) can fail - they may get stuck in loops.

## Maze Solving Logic

The solver uses a backtracking algorithm with a stack:

1. Start from start cell
2. Mark as visited
3. While stack not empty:
   - If current is end, solution found
   - Find valid moves (unvisited neighbors with no wall)
   - If moves exist:
     - Choose first move (depth-first exploration)
     - Push to stack, mark visited
   - If no moves:
     - Mark current as dead end
     - Pop from stack (backtrack)

## Data Structures

- `north_wall[R][C]`: 1 if wall exists above cell (i,j), 0 if removed
- `east_wall[R][C]`: 1 if wall exists to the right of cell (i,j), 0 if removed
- `visited[R][C]`: Tracks visited cells during generation
- `solver_visited[R][C]`: Tracks visited cells during solving

## Stack Usage

Both generation and solving rely heavily on stacks:
- **Generation**: Stack keeps track of the current path being carved
- **Solving**: Stack maintains the current exploration path

## Visualization

- **Generation**: Yellow cell shows current position, gray cells are visited
- **Solving**: Red cells show the current path, blue cells show dead ends
- **Start/End**: Green for start, red for end

## Requirements

- Python 3.x
- Pygame

## Running the Program

```bash
# Regular Version (Step 1-9)
python main.py

# Bonus Challenge (Step 10)
# Demonstrates the failure of the 'shoulder-to-the-wall' rule in mazes with cycles.
python demonstrate_bonus.py
```

In the challenge mode, you will see a yellow trail representing the wall-follower algorithm. In mazes with cycles, this algorithm often gets trapped in infinite loops, while the backtracking algorithm (shown in blue) continues to explore and find the true path.
```

The program will:
1. Generate the maze with animation
2. Set start and end points
3. Solve the maze with animation
4. Display the final result



