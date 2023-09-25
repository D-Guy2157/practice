# canvas = widget that is used to draw graphs, plots, images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500)  # for the future lines: X, Y, X, Y, etc...
# canvas.create_line(0, 0, 500, 500, fill="blue", width=5)  # blue line top L bot R
# canvas.create_line(0, 500, 500, 0, fill="red", width=5)  # red line bot L top R
# canvas.create_rectangle(50, 50, 250, 250, fill="purple")  # purple rectangle
points = [250, 0, 500, 500, 0, 500]  # can use lists/tuples to pass in info aswell
# canvas.create_polygon(points, fill="yellow", outline="black", width=5)  # beeg triforce
# canvas.create_arc(0, 0, 500, 500, fill="green", style=PIESLICE, start=90, extent=180)
# instead of start and end, it chooses how much space it takes up^^
# style=PIESLICE is default, start=0,90,180, etc (in degrees) counterclockwise^^
# POKEBALL:
canvas.create_arc(0, 0, 500, 500, fill="red", extent=180, width=10)
canvas.create_arc(0, 0, 500, 500, fill="white", extent=180, start=180, width=10)
canvas.create_oval(190, 190, 310, 310, fill="white", width=10)

canvas.pack()

window.mainloop()
