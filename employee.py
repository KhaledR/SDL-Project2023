from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Rice Retailing Billing System")
        self.root.config(bg = "white")
        self.root.focus_force()
        self.root.resizable(0,0)

        #==========Variables==========#
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_usertype = StringVar()
        self.var_salary = StringVar()





        #==========Search_Frame==========#
        search_Frame = LabelFrame(self.root, text = "Search Employee", bg = "white",
                                  font=("Times New Roman", 12, "bold")
                                 , bd=2, relief=RIDGE)
        search_Frame.place(x = 250, y = 20, width = 600, height = 70)

        #==========Options==========#
        combo_Search = ttk.Combobox(search_Frame, textvariable = self.var_searchby, values = ("Select", "Email", "Name", "Contact"),
                                    state = "readonly", justify = CENTER,
                                    font=("Times New Roman", 13))
        combo_Search.place(x = 10, y = 10, width = 180)
        combo_Search.current(0)

        txt_Search = Entry(search_Frame, textvariable = self.var_searchtxt, font = ("Times New Roman", 13), bg = "lightyellow")
        txt_Search.place(x = 200, y = 10)

        btn_Search = Button(search_Frame, text = "Search", font=("Times New Roman", 13), bg="#4caf50",
                            cursor = "hand2", fg = "white")
        btn_Search.place(x=410, y=9, width = 150, height = 30)


        #==========Title==========#
        title = Label(self.root, text = "Employee Details", font = ("times new roman", 13),
                      bg = "#828c51", fg = "white")
        title.place(x = 50, y = 100, width = 1000)

        #==========Content==========#

        #==========Row1==========#
        lbl_emp_id = Label(self.root, text = "Employee ID", font = ("times new roman", 13),
                      bg = "white")
        lbl_emp_id.place(x = 50, y = 150)
        lbl_gender = Label(self.root, text="Gender", font=("times new roman", 13),
                           bg="white")
        lbl_gender.place(x=350, y=150)
        lbl_contact = Label(self.root, text = "Contact", font = ("times new roman", 13),
                      bg = "white")
        lbl_contact.place(x = 700, y = 150)

        txt_emp_id = Entry(self.root, textvariable = self.var_emp_id , font=("times new roman", 13),
                           bg="white")
        txt_emp_id.place(x=150, y=150, width=180)
        combo_Gender = ttk.Combobox(self.root, textvariable=self.var_gender,
                                    values=("Select", "Male", "Female", "Other"),
                                    state="readonly", justify=CENTER,
                                    font=("Times New Roman", 13))
        combo_Gender.place(x=500, y=150, width=180)
        combo_Gender.current(0)
        txt_contact = Entry(self.root, textvariable = self.var_contact, font=("times new roman", 13),
                            bg="white")
        txt_contact.place(x=850, y=150, width=180)


        #==========Row2==========#
        lbl_name = Label(self.root, text="Name", font=("times new roman", 13),
                         bg="white")
        lbl_name.place(x=50, y=190)
        lbl_dob = Label(self.root, text="Date of Birth", font=("times new roman", 13),
                        bg="white")
        lbl_dob.place(x=350, y=190)
        lbl_doj = Label(self.root, text="Date of Joining", font=("times new roman", 13),
                        bg="white")
        lbl_doj.place(x=700, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("times new roman", 13),
                         bg="white")
        txt_name.place(x=150, y=190, width=180)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("times new roman", 13),
                        bg="white")
        txt_dob.place(x=500, y=190, width=180)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("times new roman", 13),
                        bg="white")
        txt_doj.place(x=850, y=190, width=180)

        #==========Row3==========#
        lbl_email = Label(self.root, text="Email", font=("times new roman", 13),
                          bg="white")
        lbl_email.place(x=50, y=230)
        lbl_pass = Label(self.root, text="Password", font=("times new roman", 13),
                         bg="white")
        lbl_pass.place(x=350, y=230)
        lbl_usertype = Label(self.root, text="User Type", font=("times new roman", 13),
                             bg="white")
        lbl_usertype.place(x=700, y=230)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("times new roman", 13),
                         bg="white")
        txt_email.place(x=150, y=230, width=180)
        txt_pass = Entry(self.root, show="*",textvariable=self.var_pass, font=("times new roman", 13),
                        bg="white")
        txt_pass.place(x=500, y=230, width=180)
        combo_usertype = ttk.Combobox(self.root, textvariable=self.var_usertype,
                                    values=("Select", "Admin", "Employee"),
                                    state="readonly", justify=CENTER,
                                    font=("Times New Roman", 13))
        combo_usertype.place(x=850, y=230, width=180)
        combo_usertype.current(0)

        #==========Row4==========#
        lbl_address = Label(self.root, text="Address", font=("times new roman", 13),
                          bg="white")
        lbl_address.place(x=50, y=270)
        lbl_salary = Label(self.root, text="Salary", font=("times new roman", 13),
                         bg="white")
        lbl_salary.place(x=500, y=270)

        txt_address = Entry(self.root, font=("times new roman", 13),
                          bg="white")
        txt_address.place(x=150, y=270, width=300, height=60)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("times new roman", 13),
                         bg="white")
        txt_salary.place(x=580, y=270, width=180)

        #==========Buttons==========#
        btn_Save = Button(self.root, text="Save", font=("Times New Roman", 13), bg="#0D98BA",
                            cursor="hand2", fg="white")
        btn_Save.place(x=500, y=305, width=110, height=28)
        btn_Update = Button(self.root, text="Update", font=("Times New Roman", 13), bg="#335145",
                            cursor="hand2", fg="white")
        btn_Update.place(x=620, y=305, width=110, height=28)
        btn_Delete = Button(self.root, text="Delete", font=("Times New Roman", 13), bg="#ff0000",
                            cursor="hand2", fg="white")
        btn_Delete.place(x=740, y=305, width=110, height=28)
        btn_Clear = Button(self.root, text="Clear", font=("Times New Roman", 13), bg="#808080",
                            cursor="hand2", fg="white")
        btn_Clear.place(x=860, y=305, width=110, height=28)

        #=========Employee_Details==========#
        emp_frame = Frame(self.root, bd = 3, relief = RIDGE)
        emp_frame.place(x = 0, y = 350, relwidth = 1, height = 150)

        vertical_Scroll = Scrollbar(emp_frame, orient = VERTICAL)
        horizontal_Scroll = Scrollbar(emp_frame, orient = HORIZONTAL)

        self.employee_Table = ttk.Treeview(emp_frame, columns = ("Emp_ID", "Name", "Email",
                                                                 "Gender", "Contact", "DoB", "DoJ", "Pass",
                                                                 "UserType", "Address", "Salary"),
                                           yscrollcommand = vertical_Scroll.set, xscrollcommand = horizontal_Scroll.set)
        horizontal_Scroll.pack(side = BOTTOM, fill = X)
        horizontal_Scroll.config(command = self.employee_Table.xview)
        vertical_Scroll.pack(side = RIGHT, fill = Y)
        vertical_Scroll.config(command = self.employee_Table.yview)


        self.employee_Table.heading("Emp_ID", text = "EMPLOYEE ID")
        self.employee_Table.heading("Name", text="NAME")
        self.employee_Table.heading("Email", text="EMAIL")
        self.employee_Table.heading("Gender", text="GENDER")
        self.employee_Table.heading("Contact", text="CONTACT NUMBER")
        self.employee_Table.heading("DoB", text="DATE OF BIRTH")
        self.employee_Table.heading("DoJ", text="DATE OF JOINING")
        self.employee_Table.heading("Pass", text="PASS")
        self.employee_Table.heading("UserType", text="USER TYPE")
        self.employee_Table.heading("Address", text="ADDRESS")
        self.employee_Table.heading("Salary", text="SALARY")
        self.employee_Table["show"] = "headings"

        self.employee_Table.column("Emp_ID", width = 90)
        self.employee_Table.column("Name", width = 100)
        self.employee_Table.column("Email", width = 100)
        self.employee_Table.column("Gender", width = 100)
        self.employee_Table.column("Contact", width = 130)
        self.employee_Table.column("DoB", width = 100)
        self.employee_Table.column("DoJ", width = 105)
        self.employee_Table.column("Pass", width = 90)
        self.employee_Table.column("UserType", width = 100)
        self.employee_Table.column("Address", width = 100)
        self.employee_Table.column("Salary", width = 100)

        self.employee_Table.pack(fill = BOTH, expand = 1)




if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()