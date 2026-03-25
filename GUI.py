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

########### FILE-PICK HELPER ###########
def file_row(parent, label_text, row, var):
    """
    Builds file picking row format.
    Parameters:
        parent - main frame of widget
        label_text - button's text
        row - start grid number
        var - stores file path
    """

    # button text format
    tk.Label(parent,
             text=label_text,
             bg = BG,
             fg = DARK_GREEN,
             font = FONT_LABEL).grid(
                    row = row,
                    column = 0,
                    sticky = 'w',
                    pady = (10, 2))

    # entry button format
    entry = tk.Entry(parent,
                     textvariable = var,
                     width = 46,
                     font = FONT_SMALL,
                     bg = 'white',
                     relief = 'solid',
                     bd = 1,
                     fg = '#333333')

    # button grid lining
    entry.grid(row = row + 1,
               column = 0,
               sticky = 'ew',
               ipady = 5,
               pady = (0, 4))

    def browse():
        """ Opens user's OS' file picker"""
        path = filedialog.askopenfilename(
            filetypes = ['*.txt',
                         ('All files', '*.*')])

        if path:
            var.set(path) # file-path

        ttk.Button(parent,
                   text = 'browse',
                   style = 'file.TButton',
                   command = browse).grid(
            row = row + 1,
            column = 1,
            padx = (8, 0),
            pady = (0, 4)
        )
########### ########### ########### ###########

########### WELCOME PAGE ###########
class WelcomePage(tk.Frame):
    """
    Welcome Page, potentially we could add info about the project here(?
    Start Button connects to Sequence file selection page.
    """

    def __init__(self, parent, controller):

        super().__init__(parent, bg = BG)
        self.controller = controller
        self._build()

        def _build(self):
            tk.Frame(self, bg = DARK_GREEN, height = 6).pack(fill = 'x')
            centre = tk.Frame(self,
                              bg = BG)
            centre.place(relx = 0.5,
                         rely = 0.42,
                         anchor = 'center')

            # welcome Page title
            tk.Label(centre,
                        text="DNA Sequence Matching",
                        bg=BG,
                        fg=DARK_GREEN,
                        font=FONT_TITLE).pack(pady=(8, 4))
            # Start Button
            ttk.Button(centre,
                       text = 'Start',
                       command = lambda: self.controller.show('ADD FILE PAGE NAME')).pack(pady= 30)

            # Footer with credits
            tk.Label(self,
                     text = 'CSCI 311 - William Chastain, Jackson Greninger, Laura Ozoria, Cynthia Pintado',
                     bg = BG,
                     fg = DARK_GREEN,
                     font = FONT_SMALL).pack(side = 'bottom', pady = 12)
########### ########### ########### ###########

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