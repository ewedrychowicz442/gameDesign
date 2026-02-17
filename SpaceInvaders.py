import tkinter as tk

#PARAMETERS
WIDTH = 600
HEIGHT = 450

def make_enemy_sprite():
    pattern = [
        "00100000100",
        "00010001000",
        "00111111100",
        "01101110110",
        "11111111111",
        "10111111101",
        "10100000101",
        "00011011000"
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)
    for y in range(h):
        for x in range(w):
            if pattern [y] [x] == "1":
                img.put("white", (x, y))
    return img

def make_player_sprite():
    h = 16
    w = 24

    img = tk.PhotoImage(width = w, height  = h)
    
    for y in range(h):
        for x in range(w):
            if 6 <= x <= 17 and y >= 6:
                img.put("blue", (x, y))
    return img

root = tk.Tk()
root.title("SPACE INVADERZ")

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "black")
canvas.pack()

player_img = make_player_sprite()
enemy_img = make_enemy_sprite()

#Create the Player
player = canvas.create_image(WIDTH//2, HEIGHT-40, image = player_img, anchor = "center")

#Enemy Formation - enemies do NOT move independently, but rather as a group
ROWS = 4
COLS = 8
CELL = 32

enemies = [] # a list to store our enemies

def create_enemy_formation():
    enemies.clear()
    start_x = 100
    start_y = 60

    for r in range(ROWS):
        for c in range(COLS):
            x = start_x + c * CELL
            y = start_y + r * CELL

            e = canvas.create_image(x, y, image = enemy_img, anchor = "nw")

            enemies.append(e)

#Player Controls
def move_left(event):
    canvas.move(player, -15, 0)
def move_right(event):
    canvas.move(player, 15, 0)

#Binding
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

#Laser Beams
lasers = []

def make_laser_sprite():
    img = tk.PhotoImage(width = 4, height = 10)

    for y in range(10):
        for x in range(4):
            img.put("yellow", (x, y))
    return img
laser_img = make_laser_sprite()

def shoot(event):
    if len(lasers) > 0:
        return
    #Bounding Boxes
    px1, py1, px2, py2 = canvas.bbox(player)
    l = canvas.create_image((px1 + px2)//2, py1, imgage = laser_img, anchor = "s")

    lasers.append(l)
root.bind("<space>", shoot)