import tkinter as tk
import random 

#DECLARE SOME CONSTANTS

WIDTH = 400
HEIGHT = WIDTH * 0.75
PLAYER_SIZE = 30
ENEMY_SIZE = 20
MOVE_SPEED = 25

#SCORE COUNTER
score = 0

#BUILD OUR WINDOW
root = tk.Tk()
root.title("Avoid the Blocks!")

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "black")
score_label = tk.Label(root, text = "Score: " + str(score), font = ("Arial", 16))
score_label.pack()
canvas.pack()

#MAKE THE PLAYER
player = canvas.create_rectangle(180, 250, 180 + PLAYER_SIZE, 250 + PLAYER_SIZE, fill = "magenta")

#MAKE A LIST TO HOLD ENEMYS
enemies = []

#MAKE AN ALIVE BOOl
alive = True

#MOVEMENT FUNCTIONS
def move_left(event):
    canvas.move(player, -MOVE_SPEED, 0)
def move_right(event):
    canvas.move(player, MOVE_SPEED, 0)

#BINDING BUTTONS
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

#BAD GUYS
def spawn_enemy():
    x = random.randint(0, WIDTH - ENEMY_SIZE)
    enemy = canvas.create_rectangle(x, 0, x + ENEMY_SIZE, ENEMY_SIZE, fill = "cyan")
    enemies.append(enemy)

#RUN GAME
def run_game():
    global alive
    global score
    global enemies
    
    if not alive:
        del enemies
        canvas.delete("all")
        canvas.create_text(WIDTH//2, HEIGHT//2, text = "GAME OVER", fill = "white", font = ("Arial", 24))

    if random.randint(1, 15) == 1:
        spawn_enemy()

    for enemy in enemies:
        canvas.move(enemy, 0, 10)

        if canvas.bbox(enemy) and canvas.bbox(player):
            ex1, ey1, ex2, ey2 = canvas.bbox(enemy)
            px1, py1, px2, py2 = canvas.bbox(player)

            if px1 < 0 or px2 > WIDTH:
                canvas.coords(player, 180, 250, 180 + PLAYER_SIZE, 250 + PLAYER_SIZE)

            if ex1 < px2 and ex2 > px1 and ey1 < py2 and ey2 > py1:
                alive = False
            if ey1 > HEIGHT:
                score += 1
                enemies.remove(enemy)
                score_label.config(text = "Score: " + str(score))
                

    root.after(50, run_game)

run_game()
root.mainloop()
