import sys

import pygame

import snake
from food import Food
from snake import Snake

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

food = Food()
snak = Snake()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    snak.update_snake()

    screen.fill(GREEN)
    food.draw()
    snak.draw_snake()
    pygame.display.update()

    clock.tick(60)