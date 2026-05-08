class MazeSolver:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end
        self.stack = [start]
        self.maze.solver_visited[start[0]][start[1]] = True
        self.current_path = [start]
        self.finished = False

    def step(self):
        if not self.stack or self.finished:
            return False

        r, c = self.stack[-1]
        if (r, c) == self.end:
            self.finished = True
            return False

        neighbors = []
        # Directions: Up, Right, Down, Left
        # We can move if no wall exists in that direction
        
        # North
        if r > 0 and self.maze.northWall[r][c] == 0 and not self.maze.solver_visited[r-1][c]:
            neighbors.append((r-1, c))
        # East
        if c < self.maze.cols - 1 and self.maze.eastWall[r][c] == 0 and not self.maze.solver_visited[r][c+1]:
            neighbors.append((r, c+1))
        # South
        if r < self.maze.rows - 1 and self.maze.northWall[r+1][c] == 0 and not self.maze.solver_visited[r+1][c]:
            neighbors.append((r+1, c))
        # West
        if c > 0 and self.maze.eastWall[r][c-1] == 0 and not self.maze.solver_visited[r][c-1]:
            neighbors.append((r, c-1))

        if neighbors:
            nr, nc = neighbors[0] # Typical DFS solver
            self.maze.solver_visited[nr][nc] = True
            self.stack.append((nr, nc))
        else:
            # Backtracking: Mark as dead end (Blue)
            dead_r, dead_c = self.stack.pop()
            self.maze.dead_ends[dead_r][dead_c] = True
        
        return True

    def draw_path(self, screen, show_dead_ends=True):
        # Red cells -> current path (Step 8)
        for r, c in self.stack:
            self.maze.draw_cell(screen, r, c, (255, 0, 0))
        
        if show_dead_ends:
            # Blue cells -> dead ends (Step 8)
            for r in range(self.maze.rows):
                for c in range(self.maze.cols):
                    if self.maze.dead_ends[r][c]:
                        self.maze.draw_cell(screen, r, c, (0, 0, 255))