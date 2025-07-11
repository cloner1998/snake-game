import pygame
from pygame import Vector2


class Food:
    def __init__(self, snake_body):
        self.position = self.generate_random_position(snake_body)

    def draw(self):
        from game_loop import cell_size
        from game_loop import OFF_SET
        food_rect = pygame.Rect(OFF_SET + self.position.x * cell_size, OFF_SET + self.position.y * cell_size, cell_size, cell_size )

        from game_loop import screen
        from game_loop import DARK_GREEN

        # pygame.draw.rect(screen, DARK_GREEN, food_rect)
        food_surface = pygame.image.load("images/food.png")
        screen.blit( food_surface, food_rect)

    def generate_random_cell(self):
        from random import randint
        from game_loop import num_of_cells
        x = randint(0, num_of_cells - 1)
        y = randint(0, num_of_cells - 1)
        return Vector2(x, y)

    def generate_random_position(self, snake_body):

        position = self.generate_random_cell()
        while position in snake_body:
            position = self.generate_random_cell()
        return position