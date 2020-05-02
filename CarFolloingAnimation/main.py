from WindowManager import Window
import tkinter as tk


def main():
    root = tk.Tk()
    root.resizable(False, False)
    root.configure(bg='#334353')
    root.iconbitmap('car.ico')

    Window(root)

    tk.mainloop()
    root.mainloop()


main()
