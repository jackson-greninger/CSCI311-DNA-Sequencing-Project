import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import ttk, filedialog

# global formatting
BG = '#cef0ce'
FONT_COLOR = '#044004'
FONT_TITLE = ('Arial', 22, 'bold')
FONT_SUB = ('Arial', 12, 'italic')
FONT_LABEL = ('Arial', 12, 'bold')
FONT_BUTTON = ('Arial', 12, 'bold')
FONT_SMALL = ('Arial', 12)

DARK_GREEN  = '#044004'
MID_GREEN   = '#2d7a2d'
WHITE       = '#ffffff'

########### BUTTON FORMAT ###########
def apply_styles():
    """" Register GUI styles for buttons"""
    s = ttk.Style()
    s.theme_use('clam')

    # main action button
    s.configure('main.TButton',
                background= DARK_GREEN,
                foreground = 'white',
                font = FONT_COLOR,
                padding = (20,20),
                relief = 'flat',)
    s.map('main.TButton',
          background= [('active', MID_GREEN), ('disabled', '#aaaaaa')],
          foreground = [('disabled', '#dddddd')])

    # file-picking buttons
    s.configure('file.TButton',
                background=MID_GREEN, foreground=WHITE,
                font=('Arial', 10), padding=(8, 6), relief='flat')
    s.map('file.TButton',
          background=[('active', DARK_GREEN)])

    # drop-down
    s.configure('TDrop',
                padding = (6,6),
                font = FONT_SMALL)
########### ########### ########### ###########

class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('Toplevel Window')

        ttk.Button(self,
                text='Close',
                command=self.destroy).pack(expand=True)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('800x700')
        self.title('Welcome Page')
        self.config(bg='#cef0ce')

        title1 = tk.Label(self, text='Welcome to DNA Sequence Matching',
                          bg='#cef0ce',
                          fg='#044004',
                          font=('Arial', 20, "bold"),
                          justify='center')

        title1.pack(pady=200, padx=50, anchor='center')

        # place a button on the root window
        style = ttk.Style()
        style.configure('start.TButton',
                        background='#044004',
                        foreground='#044004',
                        font=('Arial', 20, "bold"),
                        )

        start_button = ttk.Button(self,
                text='Start',
                style='start.TButton',
                command=self.open_window)

        start_button.grid(row=0, column=0, sticky='nsew')

    def open_window(self):
        window = Window(self)
        window.grab_set()

if __name__ == "__main__":
    app = App()
    app.mainloop()