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

title_font = pygame.font.SysFont('comicsans', 30)
score_font = pygame.font.SysFont('comicsans', 20)

GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)
OFF_SET = 75

cell_size = 20
num_of_cells = 20
screen = pygame.display.set_mode((2*OFF_SET+num_of_cells * cell_size, 2*OFF_SET+num_of_cells * cell_size))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

game = Game()
SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)

if __name__ == "__main__":
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
        pygame.draw.rect(screen, DARK_GREEN, (OFF_SET-5,OFF_SET-5, cell_size*num_of_cells + 10, cell_size*num_of_cells + 10), 5)
        game.draw()
        title_surface = title_font.render("Snake Game", True, DARK_GREEN)
        score_surface = title_font.render("Score: " + str(game.score), True, DARK_GREEN)
        screen.blit(title_surface, (OFF_SET-5, 20))
        screen.blit(score_surface, (OFF_SET-5, OFF_SET + cell_size * num_of_cells + 10))
        pygame.display.update()

        clock.tick(60)