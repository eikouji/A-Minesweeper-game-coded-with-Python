from tkinter import *
from cell import Cell
import settings
import utils


root = Tk()
# override the settings of the window #

root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

# frames #

top_frame = Frame(
    root,
    bg='black', # change later to black #
    width=settings.WIDTH,
    height=utils.height_prct(25)
    )

top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='black', # change later to black #
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)

left_frame.place(x=0, y=utils.height_prct(25))


center_frame = Frame(
    root,
    bg='black', 
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)

center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

# MineSweeper Grid section #

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=y, row=x
        )

Cell.randomize_mines()
for c in Cell.all:
    print(c.is_mine)

# run the window #
root.mainloop()

# a huge thank you to Jim at freeCodeCamp for having a wonderful youtube tutorial to learn from. 
# watch the video at https://youtu.be/OqbGRZx4xUc #