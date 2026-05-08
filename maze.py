import pygame

class Maze:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.offset = 20
        
       
        # Initial grid wall state
        # 1 = Wall exists, 0 = Wall removed
        
        self.northWall = [[1 for _ in range(cols)] for _ in range(rows)]
        self.eastWall = [[1 for _ in range(cols)] for _ in range(rows)]
        
        
        # Additional data structures for maze generation and solving
        
        self.visited = [[False for _ in range(cols)] for _ in range(rows)]
        self.solver_visited = [[False for _ in range(cols)] for _ in range(rows)]
        self.dead_ends = [[False for _ in range(cols)] for _ in range(rows)]

    def reset_visited(self):
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]

    def is_valid(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols

    def draw(self, screen):
        # Draw the grid boundaries (West and South)
        pygame.draw.line(screen, (255, 255, 255), (self.offset, self.offset), 
                         (self.offset, self.offset + self.rows * self.cell_size), 2)
        pygame.draw.line(screen, (255, 255, 255), (self.offset, self.offset + self.rows * self.cell_size), 
                         (self.offset + self.cols * self.cell_size, self.offset + self.rows * self.cell_size), 2)

        for r in range(self.rows):
            for c in range(self.cols):
                x = self.offset + c * self.cell_size
                y = self.offset + r * self.cell_size
                
                # Draw North Wall
                if self.northWall[r][c] == 1:
                    pygame.draw.line(screen, (255, 255, 255), (x, y), (x + self.cell_size, y), 2)
                
                # Draw East Wall
                if self.eastWall[r][c] == 1:
                    pygame.draw.line(screen, (255, 255, 255), (x + self.cell_size, y), (x + self.cell_size, y + self.cell_size), 2)

    def draw_cell(self, screen, r, c, color):
        x = self.offset + c * self.cell_size + 2
        y = self.offset + r * self.cell_size + 2
        size = self.cell_size - 4
        pygame.draw.rect(screen, color, (x, y, size, size))