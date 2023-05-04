from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Billing:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Rice Retailing Billing System")
        self.root.config(bg = "#A6C36F")

        #=======Variables==========#
        self.var_search = StringVar()
        self.var_bname = StringVar()
        self.var_contact = StringVar()
        self.var_price = StringVar()
        self.var_kilos = StringVar()
        self.var_stock = StringVar()
        self.var_cname = StringVar()


        #==========Icon==========#
        self.icon_title = PhotoImage(file="img/ricewhite.png")

        #==========Title==========#
        title = Label(self.root, text="No Pay No Grain Billing System",
                  font=("Times New Roman", 35, "bold"), image = self.icon_title,
                  bg="#1E352F", fg="white", anchor="w",
                  padx=20, compound=LEFT)
        title.place(x=0, y=0, relwidth=1, height=70)

    #==========Logout_Button==========#
        logout_btn = Button(self.root, text="Logout"
                        , font=("times new roman", 15, "bold"),
                        bg="#BEEF9E", cursor="hand2")

        logout_btn.place(x=1180, y=10, width=150)

    #==========Clock==========#
        self.clock_lbl = Label(self.root, text="Welcome to the Billing System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
                           font=("Times New Roman", 15)
                           , bg="#828C51", fg="white", anchor="w")
        self.clock_lbl.place(x=0, y=70, relwidth=1, height=30)

    #========Product_Frame==========#
        product_Frame1 = Frame(self.root, bd = 4, relief = RIDGE, bg = "white")
        product_Frame1.place(x = 6, y = 110, width = 410, height = 550)

        product_Title = Label(product_Frame1, text = "All Products", font = ("times new roman", 18, "bold"),
                              bg = "#335145", fg = "white")
        product_Title.pack(side = TOP, fill = X)

        #========Product_search_Frame==========#
        product_Frame2 = Frame(product_Frame1, bd=2, relief=RIDGE, bg="white")
        product_Frame2.place(x=2, y=42, width=398, height=90)

        lbl_Search = Label(product_Frame2, text = "Search brand by name", font = ("times new roman", 13, "bold"),
                           bg = "white", fg = "green")
        lbl_Search.place(x = 2, y = 5)

        lbl_name = Label(product_Frame2, text = "Brand Name", font = ("times new roman", 13, "bold"),
                           bg = "white")
        lbl_name.place(x=5, y=45)
        txt_name = Entry(product_Frame2, textvariable = self.var_search, font=("times new roman", 13, "bold"),
                         bg="lightyellow")
        txt_name.place(x=125, y=47, width = 160, height = 22)

        #==========Button==========#
        btn_Search = Button(product_Frame2, text = "Search", font = ("times new roman", 13), bg="#4caf50",
                            cursor = "hand2", fg = "white")
        btn_Search.place(x = 290, y = 47, height = 22, width = 90)
        btn_Showall = Button(product_Frame2, text="Show All", font=("times new roman", 13), bg="silver",
                            cursor="hand2")
        btn_Showall.place(x=290, y=10, width=90 , height = 25)

        product_Frame3 = Frame(product_Frame1, bd=3, relief=RIDGE)
        product_Frame3.place(x=2, y=138, width=396, height=375)

        vertical_Scroll = Scrollbar(product_Frame3, orient=VERTICAL)
        horizontal_Scroll = Scrollbar(product_Frame3, orient=HORIZONTAL)

        self.product_Table = ttk.Treeview(product_Frame3, columns=("Product_ID", "Name", "Price",
                                                                    "Kilos", "Status"),
                                           yscrollcommand=vertical_Scroll.set, xscrollcommand=horizontal_Scroll.set)
        horizontal_Scroll.pack(side=BOTTOM, fill=X)
        horizontal_Scroll.config(command=self.product_Table.xview)
        vertical_Scroll.pack(side=RIGHT, fill=Y)
        vertical_Scroll.config(command=self.product_Table.yview)

        self.product_Table.heading("Product_ID", text="PRODUCT ID")
        self.product_Table.heading("Name", text="BRAND NAME")
        self.product_Table.heading("Price", text="PRICE")
        self.product_Table.heading("Kilos", text="Kg/s")
        self.product_Table.heading("Status", text="STATUS")
        self.product_Table["show"] = "headings"

        self.product_Table.column("Product_ID", width=90)
        self.product_Table.column("Name", width=120)
        self.product_Table.column("Price", width=90)
        self.product_Table.column("Kilos", width=90)
        self.product_Table.column("Status", width=90)
        self.product_Table.pack(fill=BOTH, expand=1)
        #self.product_Table.bind("<ButtonRelease-1>", self.get_Data)
        lbl_note = Label(product_Frame1, text = "Note: Enter 0 Kilo to remove product from billing", font = ("times new roman", 11),
                         bg = "white", fg = "red")
        lbl_note.pack(side = BOTTOM, fill = X)

    #========Customer_Frame==========#
        customer_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        customer_Frame.place(x=420, y=110, width=550, height=70)

        customer_Title = Label(customer_Frame, text="Customer Details", font=("times new roman", 13),
                              bg="#BEEF9E")
        customer_Title.pack(side=TOP, fill=X)

        lbl_name = Label(customer_Frame, text = "Brand Name", font = ("times new roman", 13, "bold"),
                           bg = "white")
        lbl_name.place(x=5, y=35)
        txt_name = Entry(customer_Frame, textvariable = self.var_cname, font=("times new roman", 13, "bold"),
                         bg="lightyellow")
        txt_name.place(x=105, y=35, width = 170, height = 22)

        lbl_contact = Label(customer_Frame, text="Contact", font=("times new roman", 13, "bold"),
                         bg="white")
        lbl_contact.place(x=290, y=35)
        txt_contact = Entry(customer_Frame, textvariable=self.var_contact, font=("times new roman", 13, "bold"),
                         bg="lightyellow")
        txt_contact.place(x=380, y=35, width=140, height= 22)

        #========cal_cart_Frame==========#
        cal_cart_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        cal_cart_Frame.place(x=420, y=190, width=550, height=360)

        #========calculator_Frame==========#
        cal_Frame = Frame(cal_cart_Frame, bd=2, relief=RIDGE, bg="white")
        cal_Frame.place(x=5, y=10, width=270, height=340)

        #========cart_Frame==========#
        cart_Frame = Frame(cal_cart_Frame, bd=3, relief=RIDGE)
        cart_Frame.place(x=290, y=8, width=248, height=342)
        cart_Title = Label(cart_Frame, text="Cart \t Total Product: [0]", font=("times new roman", 13),
                               bg="#BEEF9E")
        cart_Title.pack(side=TOP, fill=X)

        vertical_Scroll = Scrollbar(cart_Frame, orient=VERTICAL)
        horizontal_Scroll = Scrollbar(cart_Frame, orient=HORIZONTAL)

        self.cart_Table = ttk.Treeview(cart_Frame, columns=("Product_ID", "Name", "Price",
                                                                   "Kilos", "Status"),
                                          yscrollcommand=vertical_Scroll.set, xscrollcommand=horizontal_Scroll.set)
        horizontal_Scroll.pack(side=BOTTOM, fill=X)
        horizontal_Scroll.config(command=self.cart_Table.xview)
        vertical_Scroll.pack(side=RIGHT, fill=Y)
        vertical_Scroll.config(command=self.cart_Table.yview)

        self.cart_Table.heading("Product_ID", text="PRODUCT ID")
        self.cart_Table.heading("Name", text="BRAND NAME")
        self.cart_Table.heading("Price", text="PRICE")
        self.cart_Table.heading("Kilos", text="Kg/s")
        self.cart_Table.heading("Status", text="STATUS")
        self.cart_Table["show"] = "headings"

        self.cart_Table.column("Product_ID", width=100)
        self.cart_Table.column("Name", width=100)
        self.cart_Table.column("Price", width=60)
        self.cart_Table.column("Kilos", width=95)
        self.cart_Table.column("Status", width=90)
        self.cart_Table.pack(fill=BOTH, expand=1)
        # self.cart_Table.bind("<ButtonRelease-1>", self.get_Data)

        #========Add_to_Cart_Widget_Frame==========#
        add_cart_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        add_cart_Frame.place(x=420, y=550, width=550, height=110)

        b_lbl = Label(add_cart_Frame, text = "Brand Name", font = ("times new roman", 13),
                           bg = "white")
        b_lbl.place(x=5, y=5)
        b_txt = Entry(add_cart_Frame, textvariable = self.var_bname, font=("times new roman", 13),
                       bg="lightyellow", state = "readonly")
        b_txt.place(x=5, y=35, width = 190, height = 22)

        price_lbl = Label(add_cart_Frame, text="Price Per Kilo", font=("times new roman", 13),
                      bg="white")
        price_lbl.place(x=230, y=5)
        price_txt = Entry(add_cart_Frame, textvariable=self.var_price, font=("times new roman", 13),
                      bg="lightyellow", state="readonly")
        price_txt.place(x=230, y=35, width=140, height=22)

        kilos_lbl = Label(add_cart_Frame, text="Kilo/s", font=("times new roman", 13),
                          bg="white")
        kilos_lbl.place(x=390, y=5)
        kilos_txt = Entry(add_cart_Frame, textvariable=self.var_kilos, font=("times new roman", 13),
                          bg="lightyellow")
        kilos_txt.place(x=390, y=35, width=140, height=22)

        stock_lbl = Label(add_cart_Frame, text="Stock Kg/s [1000]", font=("times new roman", 13),
                          bg="white")
        stock_lbl.place(x=5, y=70)

        clear_cart_btn = Button(add_cart_Frame, text="Clear", font=("times new roman", 14, "bold"),
                            bg="lightgray", cursor="hand2")

        clear_cart_btn.place(x=180, y=70, width=150, height = 30)
        add_update_cart_btn = Button(add_cart_Frame, text="Add | Update", font=("times new roman", 14, "bold"),
                                bg="#335145", fg = "white",cursor="hand2")
        add_update_cart_btn.place(x=360, y=70, width=150, height=30)


if __name__ == "__main__":
    root = Tk()
    obj = Billing(root)
    root.mainloop()