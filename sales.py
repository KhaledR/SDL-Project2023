from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class Sales:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Rice Retailing Billing System")
        self.root.config(bg = "white")
        self.root.focus_force()
        self.root.resizable(0,0)

        #========Variables========#
        self.var_invoice = StringVar()


        #========Title========#
        lbl_title = Label(self.root, text="View Customer Bills", font=("times new roman", 27, "bold"),
                    bg="#828c51", fg="white", bd = 3, relief = RIDGE)
        lbl_title.pack(side = TOP, fill = X)

        lbl_invoice = Label(self.root, text = "Invoice No.", font=("times new roman", 13),
                    bg="white")
        lbl_invoice.place(x = 50, y = 100)

        txt_invoice = Entry(self.root, textvariable= self.var_invoice, font=("times new roman", 13),
                        bg="white")
        txt_invoice.place(x=160, y=100, width = 170, height = 27)

        #========Buttons========#
        btn_search = Button(self.root, text = "Search", bg="#4caf50", font=("Times New Roman", 13),
                            cursor="hand2", fg="white")
        btn_search.place(x = 360, y = 100, width = 120, height = 27)
        btn_clear = Button(self.root, text="Clear", bg="#808080", font=("Times New Roman", 13),
                            cursor="hand2", fg="white")
        btn_clear.place(x=490, y=100, width=120, height=27)

        #========Bill_List_Frame========#
        sales_Frame = Frame(self.root, bd = 3, relief = RIDGE)
        sales_Frame.place(x = 50, y = 140, width = 200, height = 330)

        scrolly = Scrollbar(sales_Frame, orient = VERTICAL)
        self.sales_List = Listbox(sales_Frame, font = ("times new roman", 14), bg = "white")
        scrolly.config(command = self.sales_List.yview)
        scrolly.pack(side = RIGHT, fill = Y)
        self.sales_List.pack(fill = BOTH, expand = 1)

        #========Bill_Area========#
        bill_Frame = Frame(self.root, bd = 3, relief = RIDGE)
        bill_Frame.place(x = 280, y = 140, width = 410, height = 330)

if __name__ == "__main__":
    root = Tk()
    obj = Sales(root)
    root.mainloop()