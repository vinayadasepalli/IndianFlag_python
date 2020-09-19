import math
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=500, height=400)  # window size
labelname = Label(tk, text="JAI HIND")
labelname.config(font=("Courier", 21))

email = Label(tk, text="vinay.dasepalli@gmail.com")
email.config(font=("Arial", 21))

labelname.pack()
canvas.pack()
email.pack()

canvas.create_rectangle(100, 100, 400, 200, fill='#FF9933')  # Color = Deep Saffron
canvas.create_rectangle(100, 150, 400, 200, fill='#FFFFFF')  # Color = white
canvas.create_rectangle(100, 250, 400, 200, fill='#138808')  # Color = India Green

cx, cy, r, hour = 250, 175, 25, 1


def create_circle(x, y, r, canvas):  # create circle
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1)


create_circle(cx, cy, r, canvas)

for x in range(0, 24):
    lineAngle = math.pi/2 - 2*math.pi*hour/24
    hourX = cx + r * math.cos(lineAngle)
    hourY = cy - r * math.sin(lineAngle)
    canvas.create_line(cx, cy, hourX, hourY, fill="black", width=0.5)
    hour = hour+1

tk.mainloop()
