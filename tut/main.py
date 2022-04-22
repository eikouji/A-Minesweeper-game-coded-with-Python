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

# cell code #
c1 = Cell()
c1.create_btn_object(center_frame)
c1.cell_btn_object.place(
    x=0, y=0
)

# place example, not gonna work with many buttons #
c2 = Cell()
c2.create_btn_object(center-frame)
c2.cell_btn_object.place(
    x=40, y=0
)



# run the window #
root.mainloop()