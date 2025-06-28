import pygame
from pygame import Vector2


class Snake:
    def __init__(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]

    def draw_snake(self):
        for seg in self.body:
            from game_loop import cell_size
            seg_rect = pygame.Rect( seg.x * cell_size, seg.y * cell_size,  cell_size, cell_size)

            from game_loop import screen
            from game_loop import DARK_GREEN
            pygame.draw.rect(screen, DARK_GREEN, seg_rect, 0 , 7)