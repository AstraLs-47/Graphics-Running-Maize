import pygame
import sys
from maze import Maze


# Step 1: Project Setup
pygame.init()

# Step 2: Initial grid setup
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 25
ROWS, COLS = (HEIGHT - 60) // CELL_SIZE, (WIDTH - 60) // CELL_SIZE