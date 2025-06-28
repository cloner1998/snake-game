from snake import Snake
from food import Food


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)

    def update(self):
        self.snake.update_snake()

    def draw(self):
        self.food.draw()
        self.snake.draw_snake()

    def check_collision_with_food(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.generate_random_position(self.snake.body)
