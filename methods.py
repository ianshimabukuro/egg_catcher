from random import randrange
from tkinter import Canvas, Tk, messagebox, font

def create_eggs():
    x = randrange(10,740)
    y = 40
    new_egg = c.create_oval(x,y,x+egg_width,y+egg_height, fill=  next(color_cycle),width = 0)
    eggs.append(new_egg)
    root.after(egg_interval,create_eggs)

def move_eggs():
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2) = c.coords(egg)
        c.move(egg,0,10)
        if egg_y2 > canvas_height:
            egg_dropped(egg)
    root.after(egg_speed,move_eggs)

def egg_dropped(egg):
    eggs.remove(egg)
    c.delete(egg)
    lose_a_life()
    if lives_remaining == 0:
        messagebox.showinfo("Game Over",score)
        root.destroy()

def lose_a_life():
    global lives_remaining
    lives_remaining -=1
    c.itemconfigure(lives_text,text = 'Lives: ' + str(lives_remaining))

def check_catch():
    (catcher_x,catcher_y,catcher_x2,catcher_y2) = c.coords(catcher)
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2) = c.coords(egg)
        if catcher_x >egg_x and egg_x2 <catcher_x2 and catcher_y2 - egg_y2 <40:
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)
    root.after(100,check_catch)

def increase_score(points):
    global score, egg_speed, egg_interval
    score += points
    egg_speed = int(egg_speed*difficulty_factor)
    egg_interval = int(egg_interval*difficulty_factor)
    c.itemconfigure(score_text,text = 'Score' + str(score))

def move_left(event):
    (x1,y1,x2,y2) = c.coords(catcher)
    if x1 > 0:
        c.move(catcher,-20,0)

def move_right(event):
    (x1,y1,x2,y2) = c.coords(catcher)
    if x2 > 0:
        c.move(catcher,20,0)






