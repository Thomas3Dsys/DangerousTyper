
from timeit import Timer
from tkinter import *
import time
from prompts import prompts
import random

FONT_NAME = "Arial"

start = time.time()
window = Tk()
window.title("Dangerour Story Writer")
window.config(padx=100, pady=50)

prompt = random.choice(prompts)
typing_area= Text(font=(FONT_NAME, 12))
typing_area.insert("1.0", prompt )
typing_area.grid(row=0, column = 0)

start = time.time()
has_been_reset = True

def reset_timer(event):
    global start, has_been_reset
    start = time.time()
    typing_area.configure(bg = "#ffffff")
    has_been_reset = True

def delete_text():
    global has_been_reset
    if has_been_reset :
        if time.time() - start > 5:
            print("Delete")
            typing_area.delete("1.0", END)
            typing_area.configure(bg = "#4a3030")
            has_been_reset = False
            prompt = random.choice(prompts)
            typing_area.insert("1.0", prompt )
        elif time.time() - start < 3:
            #print("regular")
            typing_area.configure(bg = "#ffffff")
        elif time.time() - start > 4.75:
            print("!!")
            typing_area.configure(bg = "#bda8a8")
        elif time.time() - start > 4.25:
            print("!")
            typing_area.configure(bg = "#ccbaba")
        elif time.time() - start > 4:
            print(".")
            typing_area.configure(bg = "#e0d7d7")

    window.after(100, delete_text)


window.bind("<Key>", reset_timer)
window.after(1000, delete_text)
window.mainloop()