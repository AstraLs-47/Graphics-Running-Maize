import pygame
import sys
from maze import Maze
from generator import MazeGenerator
from solver import MazeSolver

pygame.init()
WIDTH, HEIGHT = 800, 650
CELL_SIZE = 25
ROWS, COLS = (HEIGHT - 120) // CELL_SIZE, (WIDTH - 60) // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CHALLENGE: Wall Follower vs Cycles")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 18)

def main():
    maze = Maze(ROWS, COLS, CELL_SIZE)
    generator = MazeGenerator(maze)
    state = "GENERATING"
    solver = None
    start, end = (0, 0), (ROWS - 1, COLS - 1)

    while True:
        screen.fill((30, 30, 30))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()

        if state == "GENERATING":
            if not generator.step():
                generator.add_cycles(chance=0.05)
                solver = MazeSolver(maze, start, end)
                state = "SOLVING"
            maze.draw_cell(screen, generator.current_cell[0], generator.current_cell[1], (0, 255, 0))

        elif state in ["SOLVING", "FINISHED"]:
            if state == "SOLVING":
                if not solver.step():
                    state = "FINISHED"
            
            # Draw the final path in Yellow (Step 10 logic)
            for r, c in solver.stack:
                maze.draw_cell(screen, r, c, (255, 255, 0))
            
            # Draw the deadlocks/backtracked areas in Blue
            for r in range(maze.rows):
                for c in range(maze.cols):
                    if maze.dead_ends[r][c]:
                        maze.draw_cell(screen, r, c, (0, 0, 255))
            
            if state == "FINISHED":
                msg = "Goal Reached! Cycles handled correctly."
                color = (0, 255, 0)
            else:
                msg = "Backtracking Solver: Navigating 1-in-20 Cycles..."
                color = (255, 255, 255)
            screen.blit(font.render(msg, True, color), (20, HEIGHT - 40))

        maze.draw(screen)
        maze.draw_cell(screen, start[0], start[1], (0, 200, 0))
        maze.draw_cell(screen, end[0], end[1], (200, 0, 200))
        
        instr = "Yellow: Path | Blue: Dead-ends/Deadlocks (Rule Breaking Mitigation)"
        screen.blit(font.render(instr, True, (200, 200, 200)), (20, HEIGHT - 70))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()