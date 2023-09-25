from tkinter import *
import random

GAME_WIDTH = 1000
GAME_HEIGHT = 700
SPEED = 70  # game speed, higher is slower, 60 is challenging but a good number
SPACE_SIZE = 50  # size of all game objects
BODY_PARTS = 3  # starting body count
SNAKE_COLOR = "#00FF00"  # GREEN:#00FF00  BLUE:#0000FF
FOOD_COLOR = "#FF0000"  # RED:#FF0000  YELLOW:#FFFF00
BACKGROUND_COLOR = "#000000"  # just keep this black for the love of god
# increase = 0

class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.squares.append(square)

class Food:

    def __init__(self):

        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="food")


def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score
        # global SPEED
        # global increase

        # increase += 1
        # score += increase
        # SPEED -= 1 + increase

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        print("GAME OVER: WIDTH")
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        print("GAME OVER: HEIGHT")
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("GAME OVER: SELF COLLIDE")
            return True

def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('Consolas', 70), text="GAME OVER", fill="red", tags="gameover")


def new_game(event):  # scuffed restart atm

    global canvas
    global snake
    global food
    global direction
    global score

    score = 0
    direction = 'down'

    canvas.delete(ALL)
    canvas.pack()
    window.update()

    snake = Snake()
    food = Food()

    next_turn(snake, food)


window = Tk()
window.title("Snek Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('Consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.bind("<r>", new_game)

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2)) - int((window_width/2))
y = int((screen_height/2)) - int((window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()