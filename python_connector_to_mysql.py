import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.connect_to_db()
        self.initialize_variables()
        self.create_widgets()
        self.create_database_table()
        self.fetch_data()

    def connect_to_db(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="7042573220@abhay",
                database="codewithabhay"
            )
            self.my_cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Connection Error", f"Error: {err}")
            self.conn = None

    def create_database_table(self):
        if self.conn:
            self.my_cursor.execute('''CREATE TABLE IF NOT EXISTS hospital (
                                        Nameoftablets VARCHAR(45),
                                        ref INT PRIMARY KEY,
                                        Dose INT,
                                        NumberofTablets INT,
                                        Lot INT,
                                        Issuedate DATE,
                                        ExpDate DATE,
                                        DailyDose INT,
                                        StorageAdvice VARCHAR(45),
                                        nhsNumber INT,
                                        PatientName VARCHAR(45),
                                        DateOfBirth DATE,
                                        PatientAddress VARCHAR(45)
                                    );''')
            self.conn.commit()

    def initialize_variables(self):
        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()

    def create_widgets(self):
        # Title
        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # Main frame
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        self.create_left_frame(Dataframe)
        self.create_right_frame(Dataframe)
        self.create_button_frame()
        self.create_details_frame()

    def create_left_frame(self, parent):
        DataframeLeft = LabelFrame(parent, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        self.create_patient_info_widgets(DataframeLeft)

    def create_patient_info_widgets(self, parent):
        labels = [
            ("Name Of Tablet", self.Nameoftablets),
            ("Reference No:", self.ref),
            ("Dose:", self.Dose),
            ("No of Tablets:", self.NumberofTablets),
            ("Lot:", self.Lot),
            ("Issue Date:", self.Issuedate),
            ("Exp Date:", self.ExpDate),
            ("Daily Dose:", self.DailyDose),
            ("Side Effect:", self.sideEffect),
            ("Further Information:", self.FurtherInformation),
            ("Blood Pressure:", self.DrivingUsingMachine),
            ("Storage Advice:", self.StorageAdvice),
            ("Medication:", self.HowToUseMedication),
            ("Patient Id:", self.PatientId),
            ("NHS Number:", self.nhsNumber),
            ("Patient Name:", self.PatientName),
            ("Date Of Birth:", self.DateOfBirth),
            ("Patient Address:", self.PatientAddress)
        ]

        for i, (label_text, var) in enumerate(labels):
            lbl = Label(parent, font=("arial", 12, "bold"), text=label_text, padx=2)
            lbl.grid(row=i % 9, column=(i // 9) * 2, sticky=W)
            txt = Entry(parent, font=("arial", 13, "bold"), textvariable=var, width=35)
            txt.grid(row=i % 9, column=(i // 9) * 2 + 1)

        comNameTablet = ttk.Combobox(parent, state="readonly", font=("arial", 12, "bold"), width=33, textvariable=self.Nameoftablets)
        comNameTablet["values"] = ("Nice", "Corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0, column=1)

    def create_right_frame(self, parent):
        DataframeRight = LabelFrame(parent, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Prescription")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        self.txtPrescription = Text(DataframeRight, font=("arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

    def create_button_frame(self):
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        buttons = [
            ("Prescription", self.iPrescription),
            ("Prescription Data", self.iPrescriptionData),
            ("Update", self.update_record),
            ("Delete", self.delete_record),
            ("Clear", self.clear),
            ("Exit", self.iExit)
        ]

        for i, (btn_text, cmd) in enumerate(buttons):
            btn = Button(Buttonframe, text=btn_text, bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6, command=cmd)
            btn.grid(row=0, column=i)

    def create_details_frame(self):
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(Detailsframe, column=("Nameoftablets", "ref", "Dose", "NumberofTablets", "Lot", "Issuedate", "ExpDate", "DailyDose", "StorageAdvice", "nhsNumber", "PatientName", "DateOfBirth", "PatientAddress"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        for col in self.hospital_table["columns"]:
            self.hospital_table.heading(col, text=col.replace("_", " ").title())
            self.hospital_table.column(col, width=100)

        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill=BOTH, expand=1)

        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)

    def fetch_data(self):
        if self.conn:
            try:
                self.my_cursor.execute("SELECT * FROM hospital")
                rows = self.my_cursor.fetchall()
                if rows:
                    self.hospital_table.delete(*self.hospital_table.get_children())
                    for row in rows:
                        self.hospital_table.insert("", END, values=row)
                self.conn.commit()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")

    def iPrescriptionData(self):
        if self.ref.get() == "" or self.NumberofTablets.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            if self.conn:
                self.my_cursor.execute('''INSERT INTO hospital (Nameoftablets, ref, Dose, NumberofTablets, Lot, Issuedate, ExpDate, DailyDose, StorageAdvice, nhsNumber, PatientName, DateOfBirth, PatientAddress) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (
                    self.Nameoftablets.get(),
                    self.ref.get(),
                    self.Dose.get(),
                    self.NumberofTablets.get(),
                    self.Lot.get(),
                    self.Issuedate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.StorageAdvice.get(),
                    self.nhsNumber.get(),
                    self.PatientName.get(),
                    self.DateOfBirth.get(),
                    self.PatientAddress.get(),
                ))
                self.conn.commit()
                self.fetch_data()
                messagebox.showinfo("Success", "Record has been inserted")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    def iPrescription(self):
        self.txtPrescription.delete('1.0', END)
        self.txtPrescription.insert(END, f"Name Of Tablets: \t\t{self.Nameoftablets.get()}\n")
        self.txtPrescription.insert(END, f"Reference No: \t\t{self.ref.get()}\n")
        self.txtPrescription.insert(END, f"Dose: \t\t{self.Dose.get()}\n")
        self.txtPrescription.insert(END, f"No of Tablets: \t\t{self.NumberofTablets.get()}\n")
        self.txtPrescription.insert(END, f"Lot: \t\t{self.Lot.get()}\n")
        self.txtPrescription.insert(END, f"Issue Date: \t\t{self.Issuedate.get()}\n")
        self.txtPrescription.insert(END, f"Exp Date: \t\t{self.ExpDate.get()}\n")
        self.txtPrescription.insert(END, f"Daily Dose: \t\t{self.DailyDose.get()}\n")
        self.txtPrescription.insert(END, f"Storage: \t\t{self.StorageAdvice.get()}\n")
        self.txtPrescription.insert(END, f"NHS Number: \t\t{self.nhsNumber.get()}\n")
        self.txtPrescription.insert(END, f"Patient Name: \t\t{self.PatientName.get()}\n")
        self.txtPrescription.insert(END, f"Date Of Birth: \t\t{self.DateOfBirth.get()}\n")
        self.txtPrescription.insert(END, f"Patient Address: \t\t{self.PatientAddress.get()}\n")

    def get_cursor(self, event):
        cursor_row = self.hospital_table.focus()
        contents = self.hospital_table.item(cursor_row)
        row = contents["values"]

        if row:
            self.Nameoftablets.set(row[0])
            self.ref.set(row[1])
            self.Dose.set(row[2])
            self.NumberofTablets.set(row[3])
            self.Lot.set(row[4])
            self.Issuedate.set(row[5])
            self.ExpDate.set(row[6])
            self.DailyDose.set(row[7])
            self.StorageAdvice.set(row[8])
            self.nhsNumber.set(row[9])
            self.PatientName.set(row[10])
            self.DateOfBirth.set(row[11])
            self.PatientAddress.set(row[12])

    def update_record(self):
        if self.ref.get() == "":
            messagebox.showerror("Error", "Reference No. is required to update a record")
            return

        try:
            if self.conn:
                self.my_cursor.execute('''UPDATE hospital SET 
                                            Nameoftablets=%s, 
                                            Dose=%s, 
                                            NumberofTablets=%s, 
                                            Lot=%s, 
                                            Issuedate=%s, 
                                            ExpDate=%s, 
                                            DailyDose=%s, 
                                            StorageAdvice=%s, 
                                            nhsNumber=%s, 
                                            PatientName=%s, 
                                            DateOfBirth=%s, 
                                            PatientAddress=%s 
                                        WHERE ref=%s''', (
                    self.Nameoftablets.get(),
                    self.Dose.get(),
                    self.NumberofTablets.get(),
                    self.Lot.get(),
                    self.Issuedate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.StorageAdvice.get(),
                    self.nhsNumber.get(),
                    self.PatientName.get(),
                    self.DateOfBirth.get(),
                    self.PatientAddress.get(),
                    self.ref.get()
                ))
                self.conn.commit()
                self.fetch_data()
                messagebox.showinfo("Success", "Record has been updated")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    def delete_record(self):
        if self.ref.get() == "":
            messagebox.showerror("Error", "Reference No. is required to delete a record")
            return

        try:
            if self.conn:
                self.my_cursor.execute('DELETE FROM hospital WHERE ref=%s', (self.ref.get(),))
                self.conn.commit()
                self.fetch_data()
                self.clear()
                messagebox.showinfo("Success", "Record has been deleted")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0", END)

    def iExit(self):
        iExit = messagebox.askyesno("Hospital Management System", "Confirm you want to exit")
        if iExit > 0:
            if self.conn:
                self.conn.close()
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = Hospital(root)
    root.mainloop()