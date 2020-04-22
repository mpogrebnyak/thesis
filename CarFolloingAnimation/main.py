from WindowManager import Window
import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.resizable(False, False)

    root.configure(bg='#334353')
    #root.geometry("1920x1080")

    app = Window(root)

    tk.mainloop()

    root.mainloop()


main()
