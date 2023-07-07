#Please Install the Following Before Running This Script:
''' %pip install numpy '''
''' %pip install pygame '''

#OR

''' pip install numpy '''
''' pip install pygame '''


#This is the Conway's Game of Life code (in Python).
#It generates a cell grid with random cells as alive or dead, and then applies the rules of Conway's Game of Life to determine which cells will live or die.
#The rules are as follows:

#1) Any live cell with fewer than two live neighbours dies, as if caused by under-population.
#2) Any live cell with two or three live neighbours lives on to the next generation.
#3) Any live cell with more than three live neighbours dies, as if by overcrowding.
#4) Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

#This code is used to create a grid of cells that are either alive or dead, and then apply the rules of Conway's Game of Life to determine which cells will live or die.
#This is the Conway's Game of Life code (in Python).


"""
Controls:

Space Bar   Play/Pause the Game
C           Clear the Grid
R           Randomize the Grid
"""

import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conway's Game of Life (Made by Pranav Verma)")

# Set up the grid
cell_size = 10
grid_width, grid_height = width // cell_size, height // cell_size
grid = np.zeros((grid_height, grid_width), dtype=int)

# Set up the colors
bg_color = (255, 255, 255)
cell_color = (0, 0, 0)

# Define the rules of the game
def get_next_generation(grid):
    new_grid = np.zeros_like(grid)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            neighbors = (
                grid[(i-1)%grid.shape[0], (j-1)%grid.shape[1]] +
                grid[(i-1)%grid.shape[0], j] +
                grid[(i-1)%grid.shape[0], (j+1)%grid.shape[1]] +
                grid[i, (j-1)%grid.shape[1]] +
                grid[i, (j+1)%grid.shape[1]] +
                grid[(i+1)%grid.shape[0], (j-1)%grid.shape[1]] +
                grid[(i+1)%grid.shape[0], j] +
                grid[(i+1)%grid.shape[0], (j+1)%grid.shape[1]]
            )
            if grid[i, j] == 1 and neighbors in (2, 3):
                new_grid[i, j] = 1
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1
    return new_grid

# Start the game loop
running = True
paused = False
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_c:
                grid = np.zeros_like(grid)
            elif event.key == pygame.K_r:
                grid = np.random.randint(2, size=grid.shape)

    # Update the grid
    if not paused:
        grid = get_next_generation(grid)

    # Draw the grid
    screen.fill(bg_color)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 1:
                pygame.draw.rect(screen, cell_color, (j*cell_size, i*cell_size, cell_size, cell_size))

    # Update the screen
    pygame.display.update()

    # Wait for the next frame
    clock.tick(10)

# Clean up Pygame
pygame.quit()