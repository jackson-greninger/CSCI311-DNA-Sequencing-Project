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

########### BUTTON FORMAT ###########
def apply_styles():
    """" Register GUI styles for buttons"""
    s = ttk.Style()
    s.theme_use('clam')

    # main action button
    s.configure('main.TButton',
                background= DARK_GREEN,
                foreground = 'white',
                padding = (20,20),
                relief = 'flat',)
    s.map('main.TButton',
          background = [('active', MID_GREEN), ('disabled', '#aaaaaa')],
          foreground = [('disabled', '#dddddd')])

    # file-picking buttons
    s.configure('file.TButton',
                background = MID_GREEN, foreground= 'white',
                font = ('Arial', 10),
                padding = (8, 6),
                relief='flat')
    s.map('file.TButton',
          background = [('active', DARK_GREEN)])

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
            filetypes = [('Text files', '*.txt'), ('All files', '*.*')])

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
                   command = lambda: self.controller.show('FileSelection')).pack(pady= 30, ipadx = 30)

        # Footer with credits
        tk.Label(self,
                 text = 'CSCI 311 - William Chastain, Jackson Greninger, Laura Ozoria, Cynthia Pintado',
                 bg = BG,
                 fg = DARK_GREEN,
                 font = FONT_SMALL).pack(side = 'bottom', pady = 12)
########### ########### ########### ###########

########### FILE SELECTION ###########
class FileSelectionPage(tk.Frame):
    """
    Query and DNA Sequence Files selection page.
    Continue button pops up when all the right files have been selected.
    """

    # Algorithm Options
    ALGORITHMS = ['Longest Common Substring', 'Longest-Common Subsequence', 'Needleman-Wunsch']

    def __init__(self, parent, controller):
        super().__init__(parent, bg = BG)
        self.controller = controller

        # store live input values
        self.query_var = tk.StringVar()
        self.seq_var = tk.StringVar()
        self.algorithm_var = tk.StringVar()

        self._build()

        # continue button appears after all files input
        for var in (self.query_var, self.seq_var, self.algorithm_var):
            var.trace_add('write', self._check_ready)

    def _build(self):
        tk.Frame(self,
                 bg = DARK_GREEN,
                 height=6).pack(fill='x')

        # header banner
        header = tk.Frame(self,
                          bg = DARK_GREEN)
        header.pack(fill='x')
        tk.Label(header,
                 text = 'Select Your Files',
                 bg = DARK_GREEN,
                 fg = 'white',
                 font = ('Arial', 16, 'bold'),
                 pady = 14).pack()

        # white card
        card = tk.Frame(self,
                        bg = 'white',
                        bd = 0,
                        highlightbackground = '#c8e6c8',
                        highlightthickness = 1)

        card.pack(padx = 60,
                  pady = 30,
                  fill = 'both',
                  expand=True)

        # content div
        inner = tk.Frame(card, bg = 'white')
        inner.pack(padx = 30,
                   pady = 24,
                   fill = 'both',
                   expand = True)

        inner.columnconfigure(0, weight = 1)

        # file selection title rows
        file_row(inner, 'Query File ', row = 0, var = self.query_var)
        file_row(inner, 'DNA Sequences File ', row = 2, var = self.seq_var)

        # algorithm dropdown menu
        tk.Label(inner, text = 'Algorithm',
                 bg = 'white',
                 fg = DARK_GREEN,
                 font = FONT_LABEL).grid(
                        row = 4,
                        column = 0,
                        sticky = 'w',
                        pady = (14, 2))

        self.drop = ttk.Combobox(inner,
                                 textvariable = self.algorithm_var,
                                 values = self.ALGORITHMS,
                                 state = 'readonly',
                                 font = FONT_SMALL)
        self.drop.set('select an algorithm')
        self.drop.grid(row = 5,
                       column = 0,
                       columnspan = 2,
                       sticky = 'ew',
                       ipady = 4)


        # creates continue button without visibility
        self.continue_button = ttk.Button(inner,
                               text='Continue',
                               style='main.TButton',
                               command=self._go_next)
        # Add or not back button to welcome page????

    def _check_ready(self, *args):
        """
        Called when StringVars are changed.
        Shows the continue button when all the file fields have been selected.
        """
        q = self.query_var.get().strip()
        s = self.seq_var.get().strip()
        a = self.algorithm_var.get()

        if q and s and a in self.ALGORITHMS:
            self.continue_button.grid(row = 6,
                                      column = 0,
                                      columnspan = 2,
                                      pady = (24, 4),
                                      sticky = 'e')
        else:
            self.continue_button.grid_remove()

    def _go_next(self):
        # set files so app can run algorithms
        self.controller.run_algorithm(
            self.query_var.get(),
            self.seq_var.get(),
            self.algorithm_var.get()
        )
        self.controller._pages['Visualization'].load()
        self.controller.show('Visualization')
########### ########### ########### ###########

########### VISUALISATION PAGE TBD ###########
class VisualizationPage(tk.Frame):
    """Displays hte results of running the algorithm"""

    def __init__(self, parent, controller):
        super().__init__(parent, bg = BG)
        self.controller = controller
        # self._build()

    def load(self):
        for widget in self.winfo_children():
            widget.destroy()

        if self.controller.results is None:
            tk.Label(self, text='Algorithm not yet implemented',
                     bg = BG,
                     fg = DARK_GREEN,
                     font = FONT_LABEL).pack(pady=20)
            return

        best_name, best_length, best_seq = self.controller.results
        algorithm = self.controller.current_algorithm

        # algorithm name
        tk.Label(self,
                 text = algorithm,
                 bg = BG,
                 fg = DARK_GREEN,
                 font = FONT_TITLE).pack(pady=(30, 20))

        # last 3 - centered, justified center
        tk.Label(self, text=f'Best Match: {best_name}',
                 bg=BG,
                 fg=DARK_GREEN,
                 font=('Arial', 14, 'bold'),
                 justify='center').pack(pady=5)

        tk.Label(self,
                 text=f'Sequence Length: {best_length}',
                 bg=BG,
                 fg=DARK_GREEN,
                 font=('Arial', 12, 'bold'),
                 justify='center').pack(pady=5)

        tk.Label(self,
                 text=f'Sequence:\n{best_seq}',
                 bg=BG,
                 fg=DARK_GREEN,
                 font=('Arial', 13),
                 justify='center',
                 wraplength=600).pack(pady=5)

    def _build(self):
        tk.Frame(self, bg = DARK_GREEN, height = 6).pack(fill = 'x')

        header = tk.Frame(self, bg = DARK_GREEN)
        header.pack(fill = 'x')
        tk.Label(header,
                 text = 'Results & Visualization',
                 bg = DARK_GREEN,
                 fg = 'white',
                 font = ('Arial', 16, 'bold'),
                 pady = 14).pack()

########### CONTROLLER ###########
class App(tk.Tk):
    """
    Runs GUI and controllers.
    """
    def __init__(self):
        super().__init__()
        self.title('DNA Sequence Matching')
        self.geometry('800x600')
        self.resizable(False, False)
        self.config(bg = BG)

        apply_styles()

        # page frame
        container = tk.Frame(self, bg = BG)
        container.pack(fill = 'both', expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # pages set-up
        self._pages = {}
        for PageClass in (WelcomePage, FileSelectionPage, VisualizationPage):
            name = PageClass.__name__.replace('Page', '')
            page = PageClass(container, self)
            self._pages[name] = page

            page.grid(row = 0, column = 0, sticky = 'nsew')

        self.show('Welcome')

    def run_algorithm(self, query_file, sequences_file, algorithm):
        """"
        Runs the algorithm selected in the GUI.
        """
        self.current_algorithm = algorithm
        if algorithm == 'Longest-Common Subsequence':
            import LCS
            self.results = LCS.run(query_file, sequences_file)
        else:
            self.results = None

    def show(self, name):
        self._pages[name].tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()