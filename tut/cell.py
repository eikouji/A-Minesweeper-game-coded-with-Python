from tkinter import Button
class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None # at first #

    def create_btn_object(self, location):
        btn = Button(
            location,
            text='Text'
        )
        # helps ability to customize button obj #
        self.cell_btn_object = btn

# create button instance that will belong to each button object #
