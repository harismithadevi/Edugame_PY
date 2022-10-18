import turtle as t
import tkinter as tk


def press():
    for color in ["red", "yellow", "green"]:
        turt.color(color)
        turt.right(120)

root = tk.Tk()
canvas = tk.Canvas(root)
canvas.config(width=600, height=200)
canvas.pack(side=tk.LEFT)
screen = t.TurtleScreen(canvas)
screen.bgcolor("cyan")
button = tk.Button(root, text="Press me", command=press)
button.pack()
turt = t.RawTurtle(screen, shape="turtle")
root.mainloop()
