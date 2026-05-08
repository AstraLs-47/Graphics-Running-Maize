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