import sys

import pygame

'''
first make a blank canvas
'''
pygame.init()

GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

cell_size = 30
num_of_cells = 25
screen = pygame.display.set_mode((num_of_cells * cell_size, num_of_cells * cell_size))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(GREEN)
    pygame.display.update()
    clock.tick(60)