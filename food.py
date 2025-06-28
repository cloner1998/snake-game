import pygame
from pygame import Vector2


class Food():
    def __init__(self):
        self.position = Vector2(5, 6)

    def draw(self):
        from game_loop import cell_size
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size )
        from game_loop import screen
        from game_loop import DARK_GREEN
        pygame.draw.rect(screen, DARK_GREEN, food_rect)