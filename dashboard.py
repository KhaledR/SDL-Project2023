from tkinter import *
from PIL import Image, ImageTk
from employee import Employee

class BillSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Rice Retailing Billing System")
        self.root.config(bg = "#A6C36F")

        #==========Icon==========#
        self.icon_title = PhotoImage(file = "img/ricewhite.png")

        #==========Title==========#
        title = Label(self.root, text = "No Pay No Grain Billing System",
                      image = self.icon_title, font = ("Times New Roman", 35, "bold")
                      , bg = "#1E352F", fg = "white", anchor = "w",
                      padx = 20, compound = LEFT)
        title.place(x = 0, y = 0, relwidth = 1, height = 70)

        #==========Logout Button==========#
        logout_btn = Button(self.root, text = "Logout"
                            , font = ("times new roman", 15, "bold"),
                            bg = "#BEEF9E", cursor = "hand2")

        logout_btn.place(x = 1180, y = 10,  width = 150)

        #==========Clock==========#
        self.clock_lbl  =  Label(self.root, text = "Welcome to the Billing System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
                       font = ("Times New Roman", 15)
                      , bg = "#828C51", fg = "white", anchor = "w")
        self.clock_lbl.place(x=0, y=70, relwidth=1, height=30)

        #==========Left Menu==========#
        self.menulogo = Image.open("img/menu_icon.png")
        self.menulogo = self.menulogo.resize((200,200),Image.LANCZOS)
        self.menulogo = ImageTk.PhotoImage(self.menulogo)

        left_menu = Frame(self.root, bd = 2, relief = RIDGE,
                          bg = "white")
        left_menu.place(x = 2, y = 102, width= 200, height = 565)

        menuLogo_lbl = Label(left_menu, image = self.menulogo)
        menuLogo_lbl.pack(side = TOP, fill = X)

        # self.icon_side = PhotoImage(file = "img/34-right-side.png")

        menu_lbl = Label(left_menu, text = "Menu", font = ("times new roman", 20),
                         bg = "#BEEF9E")
        menu_lbl.pack(side = TOP, fill = X)

        #==========Left Menu Buttons==========#

        employee_btn = Button(left_menu, text="Employee", 
                              padx = 5, anchor = "w", font=("times new roman", 20, "bold"), bg = "white", bd = 3,
                              cursor = "hand2", command = self.employee)
        employee_btn.pack(side=TOP, fill=X)
        supplier_btn = Button(left_menu, text="Supplier",
                              padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3,
                              cursor="hand2")
        supplier_btn.pack(side=TOP, fill=X)
        types_btn = Button(left_menu, text="Types of Rice",
                              padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3,
                              cursor="hand2")
        types_btn.pack(side=TOP, fill=X)
        product_btn = Button(left_menu, text="Product",
                              padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3,
                              cursor="hand2")
        product_btn.pack(side=TOP, fill=X)
        sales_btn = Button(left_menu, text="Sales",
                              padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3,
                              cursor="hand2")
        sales_btn.pack(side=TOP, fill=X)
        exit_btn = Button(left_menu, text="Exit",
                              padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3,
                              cursor="hand2")
        exit_btn.pack(side=TOP, fill=X)

        #==========Content==========#
        self.employee_lbl = Label(self.root, text="Total Employee\n[ 0 ]",
                            font=("Times New Roman", 20)
                            , bg="#335145", fg="white", bd = 5, relief = RIDGE)
        self.employee_lbl.place(x = 300, y = 120, height = 150, width = 300)

        self.supplier_lbl = Label(self.root, text="Total Supplier\n[ 0 ]",
                                  font=("Times New Roman", 20)
                                  , bg="#335145", fg="white", bd = 5, relief = RIDGE)
        self.supplier_lbl.place(x=650, y=120, height=150, width = 300)

        self.category_lbl = Label(self.root, text="Total Category\n[ 0 ]",
                                  font=("Times New Roman", 20)
                                  , bg="#335145", fg="white", bd = 5, relief = RIDGE)
        self.category_lbl.place(x=1000, y=120, height=150, width = 300)

        self.product_lbl = Label(self.root, text="Total Product\n[ 0 ]",
                                  font=("Times New Roman", 20)
                                  , bg="#335145", fg="white", bd = 5, relief = RIDGE)
        self.product_lbl.place(x=300, y=300, height=150, width = 300)

        self.sales_lbl = Label(self.root, text="Total Sales\n[ 0 ]",
                                  font=("Times New Roman", 20)
                                  , bg="#335145", fg="white", bd = 5, relief = RIDGE)
        self.sales_lbl.place(x=650, y=300, height=150, width=300)

        #==========Footer==========#
        footer_lbl = Label(self.root, text= "RRBS - Rice Retailing Billing System by Group 9 (No Pay, No Grain)",
                               font=("Times New Roman", 13)
                               , bg="#828C51", fg="white")
        footer_lbl.pack(side = BOTTOM, fill = X)

        #==========Employee_new_Window==========#

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Employee(self.new_win)




if __name__ == "__main__":
    root = Tk()
    obj = BillSystem(root)
    root.mainloop()