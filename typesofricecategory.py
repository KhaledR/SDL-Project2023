from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class Types:
    def __init__(self, root):
            self.root = root
            self.root.geometry("1100x500+220+130")
            self.root.title("Rice Retailing Billing System")
            self.root.config(bg="white")
            self.root.focus_force()
            self.root.resizable(0, 0)

    #========Title========#
            lbl_title = Label(self.root, text="Manage the Types of Rice", font=("times new roman", 20, "bold"),
                  bg="#828c51", fg="white")
            lbl_title.pack(side = TOP, x=50, y=10, width=1000, height=40)


if __name__ == "__main__":
     root = Tk()
     obj = Types(root)
     root.mainloop()