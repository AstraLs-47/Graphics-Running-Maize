import pygame
import sys
from maze import Maze
from generator import MazeGenerator
from solver import MazeSolver

# Step 1: Project Setup
pygame.init()

# Step 2: Initial grid setup
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 25
ROWS, COLS = (HEIGHT - 60) // CELL_SIZE, (WIDTH - 60) // CELL_SIZE

# Step 3: Visualization setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator and Solver")
clock = pygame.time.Clock()

def main():
    # Step 2 & 3: Initialization
    maze = Maze(ROWS, COLS, CELL_SIZE)
    generator = MazeGenerator(maze)
    
    state = "GENERATING" # States: GENERATING, SOLVING, FINISHED
    solver = None
    
    # Step 6: Start and End Points
    start_point = (0, 0)
    end_point = (ROWS - 1, COLS - 1)

    running = True
    while running:
        screen.fill((30, 30, 30))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Step 5: Animate Maze Generation
        if state == "GENERATING":
            if not generator.step():
                # Step 10: Bonus (Cycles) - Make it visible
                pygame.display.set_caption("Maze Complete - Adding Cycles...")
                pygame.time.wait(500) # Brief pause to see the perfect maze
                # Step 10: Bonus (Cycles)
                generator.add_cycles(chance=0.05)
                pygame.display.set_caption("Cycles Added - Solving...")
                pygame.time.wait(500)
                
                state = "SOLVING"
                solver = MazeSolver(maze, start_point, end_point)
            
            # Highlight current generation cell
            maze.draw_cell(screen, generator.current_cell[0], generator.current_cell[1], (0, 255, 0))

        # Step 8: Animate Maze Solver
        elif state == "SOLVING":
            if not solver.step():
                state = "FINISHED"
            solver.draw_path(screen)

        elif state == "FINISHED":
            solver.draw_path(screen)

        # Step 2: Draw the grid
        maze.draw(screen)
        
        # Draw Start/End (Step 6)
        maze.draw_cell(screen, start_point[0], start_point[1], (0, 200, 0)) # Green start
        maze.draw_cell(screen, end_point[0], end_point[1], (200, 0, 200)) # Purple end

        pygame.display.flip()
        clock.tick(60) # Fast animation

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()