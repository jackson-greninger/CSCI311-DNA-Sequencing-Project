import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import ttk

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