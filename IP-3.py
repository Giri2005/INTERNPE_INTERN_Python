import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title('Snake Game')
        self.master.resizable(False, False)

        self.canvas = tk.Canvas(master, width=600, height=400, bg='black')
        self.canvas.pack()

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.snake_direction = 'Right'
        self.food_position = self.set_new_food_position()
        self.score = 0

        self.score_label = tk.Label(self.master, text=f'Score: {self.score}', font=('Arial', 16))
        self.score_label.pack()

        self.master.bind('<Left>', self.turn_left)
        self.master.bind('<Right>', self.turn_right)
        self.master.bind('<Up>', self.turn_up)
        self.master.bind('<Down>', self.turn_down)

        self.run_game()

    def set_new_food_position(self):
        while True:
            x = random.randint(0, 59) * 10
            y = random.randint(0, 39) * 10
            food_position = (x, y)
            if food_position not in self.snake:
                return food_position

    def turn_left(self, event):
        if self.snake_direction != 'Right':
            self.snake_direction = 'Left'

    def turn_right(self, event):
        if self.snake_direction != 'Left':
            self.snake_direction = 'Right'

    def turn_up(self, event):
        if self.snake_direction != 'Down':
            self.snake_direction = 'Up'

    def turn_down(self, event):
        if self.snake_direction != 'Up':
            self.snake_direction = 'Down'

    def run_game(self):
        if self.check_collisions():
            self.end_game()
            return

        self.move_snake()
        self.check_food_collision()

        self.canvas.delete(tk.ALL)
        self.draw_snake()
        self.draw_food()

        self.master.after(100, self.run_game)

    def check_collisions(self):
        head_x, head_y = self.snake[0]
        if head_x < 0 or head_x >= 600 or head_y < 0 or head_y >= 400:
            return True
        if (head_x, head_y) in self.snake[1:]:
            return True
        return False

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.snake_direction == 'Left':
            new_head = (head_x - 10, head_y)
        elif self.snake_direction == 'Right':
            new_head = (head_x + 10, head_y)
        elif self.snake_direction == 'Up':
            new_head = (head_x, head_y - 10)
        elif self.snake_direction == 'Down':
            new_head = (head_x, head_y + 10)
        self.snake = [new_head] + self.snake[:-1]

    def check_food_collision(self):
        if self.snake[0] == self.food_position:
            self.snake.append(self.snake[-1])
            self.food_position = self.set_new_food_position()
            self.score += 10
            self.score_label.config(text=f'Score: {self.score}')

    def draw_snake(self):
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill='green')

    def draw_food(self):
        self.canvas.create_rectangle(self.food_position[0], self.food_position[1], self.food_position[0] + 10, self.food_position[1] + 10, fill='red')

    def end_game(self):
        self.canvas.create_text(300, 200, text='Game Over', fill='red', font=('Arial', 24))

if __name__ == '__main__':
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
