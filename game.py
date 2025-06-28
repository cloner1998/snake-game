from food import Food
from snake import Snake


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()

    def update(self):
        self.snake.update_snake()

    def draw(self):
        self.food.draw()
        self.snake.draw_snake()