from snake import Snake
from food import Food


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.state = "RUNNING"

    def update(self):
        if self.state == "RUNNING":
            self.snake.update_snake()
            self.check_collision_with_food()
            self.check_collision_with_edges()
    def draw(self):
        self.food.draw()
        self.snake.draw_snake()

    def check_collision_with_food(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.generate_random_position(self.snake.body)
            self.snake.add_segment = True

    def check_collision_with_edges(self):
        from game_loop import num_of_cells
        if self.snake.body[0].x == num_of_cells or self.snake.body[0].x == -1:
            self.game_over()
        if self.snake.body[0].y == num_of_cells or self.snake.body[0].y == -1:
            self.game_over()

    def game_over(self):
        self.snake.reset()
        self.food.position = self.food.generate_random_position(self.snake.body)
        self.state = "STOPPED"