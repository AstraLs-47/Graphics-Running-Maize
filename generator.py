import random

class MazeGenerator:
    def __init__(self, maze):
        self.maze = maze
        self.stack = []
        self.current_cell = (0, 0)
        self.maze.visited[0][0] = True
        self.stack.append(self.current_cell)

    def step(self):
        if not self.stack:
            return False

        r, c = self.current_cell
        neighbors = []

        # Check neighbors (Up, Right, Down, Left)
        for dr, dc, direction in [(-1, 0, 'N'), (0, 1, 'E'), (1, 0, 'S'), (0, -1, 'W')]:
            nr, nc = r + dr, c + dc
            if self.maze.is_valid(nr, nc) and not self.maze.visited[nr][nc]:
                neighbors.append((nr, nc, direction))

        if neighbors:
            nr, nc, direction = random.choice(neighbors)
            
            # Remove wall (Step 4 Logic)
            if direction == 'N':
                self.maze.northWall[r][c] = 0
            elif direction == 'E':
                self.maze.eastWall[r][c] = 0
            elif direction == 'S':
                self.maze.northWall[nr][nc] = 0
            elif direction == 'W':
                self.maze.eastWall[r][c-1] = 0

            self.maze.visited[nr][nc] = True
            self.stack.append((nr, nc))
            self.current_cell = (nr, nc)
        else:
            self.current_cell = self.stack.pop()
        
        return True

    def add_cycles(self, chance=0.05):
        # Step 10: Bonus (Cycles)
        for r in range(1, self.maze.rows - 1):
            for c in range(1, self.maze.cols - 1):
                if random.random() < chance:
                    if random.choice([True, False]):
                        self.maze.northWall[r][c] = 0
                    else:
                        self.maze.eastWall[r][c] = 0