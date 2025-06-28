import sys

import pygame
from pygame import Vector2

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
SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:
            snak.update_snake()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snak.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                snak.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                snak.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                snak.direction = Vector2(1,0)

    screen.fill(GREEN)
    food.draw()
    snak.draw_snake()
    pygame.display.update()

    clock.tick(60)