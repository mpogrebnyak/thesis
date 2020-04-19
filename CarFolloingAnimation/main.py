from WindowManager import Window
import tkinter as tk

def main():
    root = tk.Tk()
    root.geometry("1920x1080")
    app = Window(root)

    tk.mainloop()

    root.mainloop()


main()
