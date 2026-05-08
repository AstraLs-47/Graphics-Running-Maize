class WallFollowerSolver:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end
        self.curr = start
        self.dir = 1  # Start facing East (0:N, 1:E, 2:S, 3:W)
        self.path = [start]
        self.finished = False
        self.steps = 0
        # Limit steps to detect infinite loops
        self.max_steps = maze.rows * maze.cols * 8

    def can_move(self, r, c, direction):
        if direction == 0:  # North
            return r > 0 and self.maze.northWall[r][c] == 0
        if direction == 1:  # East
            return c < self.maze.cols - 1 and self.maze.eastWall[r][c] == 0
        if direction == 2:  # South
            return r < self.maze.rows - 1 and self.maze.northWall[r+1][c] == 0
        if direction == 3:  # West
            return c > 0 and self.maze.eastWall[r][c-1] == 0
        return False

    def step(self):
        if self.finished or self.steps > self.max_steps:
            return False
            
        r, c = self.curr
        if (r, c) == self.end:
            self.finished = True
            return False

        # Priority: Turn Right (d+1), Go Straight (d), Turn Left (d-1), Back (d+2)
        for turn in [1, 0, -1, 2]:
            nd = (self.dir + turn) % 4
            if self.can_move(r, c, nd):
                self.dir = nd
                dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)][nd]
                self.curr = (r + dr, c + dc)
                self.path.append(self.curr)
                self.steps += 1
                return True
        return False

    def draw_path(self, screen):
        for i, (r, c) in enumerate(self.path):
            # Draw path in yellow. Latest position is brighter.
            color = (255, 255, 0) if i == len(self.path) - 1 else (200, 200, 0)
            self.maze.draw_cell(screen, r, c, color)