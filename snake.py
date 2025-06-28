import pygame
from pygame import Vector2


class Snake:
    def __init__(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1,0)
        self.add_segment = False
        self.eat_sound = pygame.mixer.Sound("sounds/eat.mp3")
        self.hit_wall = pygame.mixer.Sound("sounds/wall.mp3")

    def draw_snake(self):
        for seg in self.body:
            from game_loop import cell_size
            from game_loop import OFF_SET
            seg_rect = pygame.Rect( OFF_SET + seg.x * cell_size, OFF_SET + seg.y * cell_size,  cell_size, cell_size)

            from game_loop import screen
            from game_loop import DARK_GREEN
            pygame.draw.rect(screen, DARK_GREEN, seg_rect, 0 , 7)

    def update_snake(self):
        if self.add_segment:
            self.body.insert(0, self.body[0] + self.direction)
            self.add_segment = False
        else:
            # remove the last seg that is the tail of our snake
            self.body.pop()
            self.body.insert(0, self.body[0] + self.direction)
        return self.body

    def reset(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1,0)