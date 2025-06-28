import sys

import pygame
from pygame import Vector2

import snake
from food import Food
from game import Game
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

game = Game()
SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:
            game.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.state == "STOPPED":
                game.state = "RUNNING"
            if event.key == pygame.K_UP and game.snake.direction != Vector2(0,1):
                game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and game.snake.direction != Vector2(0,-1):
                game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and game.snake.direction != Vector2(1,0):
                game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and game.snake.direction != Vector2(-1,0):
                game.snake.direction = Vector2(1, 0)
    game.check_collision_with_food()
    screen.fill(GREEN)
    game.draw()
    pygame.display.update()

    clock.tick(60)