from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #================variables=================

        self.var_dep=StringVar() 
        self.var_course=StringVar() 
        self.var_year=StringVar() 
        self.var_semester=StringVar()         
        self.var_std_id=StringVar()         
        self.var_std_name=StringVar() 
        self.var_div=StringVar()         
        self.var_roll=StringVar() 
        self.var_gender=StringVar()         
        self.var_dob=StringVar() 
        self.var_email=StringVar()         
        self.var_phone=StringVar() 
        self.var_address=StringVar()         
        self.var_teacher=StringVar() 

        
        l4=Label(self.root,text="STUDENT  MANAGEMENT  SYSTEM ",font=("times new roman", 40, "bold"), bg="white", fg="blue").place(x=0, y=0, width=1700, height=50)

        self.fmain=Frame(self.root,bd=2).place(x=0,y=55,width=1600,height=800)
         
        #LEFT FRAME
        lframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        lframe.place(x=10,y=80,width=770,height=800)
        img5 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/img25.jpg")
        img5 = img5.resize((769,160), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        self.l2= Label(lframe, image=self.photoimg5)
        self.l2.place(x=0, y=0, width=769, height=160)
        #current course
        ccframe=LabelFrame(lframe,bd=2,relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        ccframe.place(x=0,y=135,width=769,height=180)

        #department
        dl=Label(ccframe,text="Department",font=("times new roman",13,"bold"))
        dl.grid(row=0,column=0,padx=10,sticky=W)
        dcb=ttk.Combobox(ccframe,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly", width=22)
        dcb["values"]=("Select Department","Computer","Biotech","AI & ML","Mechanical","Electronics","Civil")
        dcb.current(0)
        dcb.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        cl=Label(ccframe, text="Course", font=("times new roman", 13, "bold")) 
        cl.grid(row=0,column=2,padx=10, sticky=W)  
        ccb=ttk.Combobox(ccframe,textvariable=self.var_course, font=("times new roman", 13, "bold"), state="readonly", width=20)
        ccb["values"]=("Select Course", "FE", "SE", "TE", "BE") 
        ccb.current(0) 
        ccb.grid(row=0,column=3, padx=2, pady=10, sticky=W) 

        #year
        yl=Label(ccframe, text="Year", font=("times new roman", 13, "bold")) 
        yl.grid(row=1,column=0, padx=10, sticky=W) 
        ycb=ttk.Combobox(ccframe,textvariable=self.var_year, font=("times new roman", 13, "bold"), state="readonly", width=20) 
        ycb["values"]=("Select Year", "2020-21","2021-22","2022-23", "2023-24") 
        ycb.current(0) 
        ycb.grid(row=1,column=1, padx=2, pady=10, sticky=W) 

        #semester
        sl=Label(ccframe, text="Semester", font=("times new roman", 13, "bold"))
        sl.grid(row=1,column=2, padx=10, sticky=W) 
        scb=ttk.Combobox(ccframe,textvariable=self.var_semester,font=("time new roman",13,"bold"),state="readonly",width=20)
        scb["values"]=("Select Semester", "semester-1", "semester-2") 
        scb.current(0) 
        scb.grid(row=1,column=3, padx=2, pady=10, sticky=W) 

        #CLASS STUDENT INFORMATION
        csframe=LabelFrame(lframe,bd=2,relief=RIDGE,text="Class student information",font=("times new roman",12,"bold"))
        csframe.place(x=0,y=320,width=769,height=400)
        #STUDENT ID
        sidl=Label(csframe, text="StudentID:", font=("times new roman", 13, "bold"))
        sidl.grid(row=0,column=0, padx=10, sticky=W)
        side=Entry(csframe,width=20,textvariable=self.var_std_id,font=("times new roman", 13, "bold"))
        side.grid(row=0,column=1,padx=10,sticky=W)
        #STUDENT NAME
        snl=Label(csframe, text="Student Name:", font=("times new roman", 13, "bold"))
        snl.grid(row=0,column=2,padx=10, pady=5, sticky=W) 
        sne=Entry(csframe,textvariable=self.var_std_name, width=20, font=("times new roman", 13, "bold")) 
        sne.grid(row=0, column=3, padx=10, pady=5, sticky=W) 
        #CLASS DIVISION
        cdl=Label(csframe, text="Class Division:", font=("times new roman", 13, "bold")) 
        cdl.grid(row=1,column=0, padx=10, pady=5, sticky=W) 
        cdcb=ttk.Combobox(csframe,textvariable=self.var_div, font=("times new roman", 13, "bold"), state="readonly", width=18) 
        cdcb["values"]=("A", "B","C","D") 
        cdcb.current(0) 
        cdcb.grid(row=1,column=1, padx=10, pady=5, sticky=W) 
        #ROLL NO.
        rnl=Label (csframe, text="Roll No:", font=("times new roman", 13, "bold"))
        rnl.grid(row=1,column=2, padx=10, pady=5, sticky=W) 
        rne=Entry(csframe,textvariable=self.var_roll, width=20, font=("times new roman", 13, "bold")) 
        rne.grid(row=1,column=3, padx=10, pady=5, sticky=W)
        #GENDER
        gl=Label(csframe, text="Gender:", font=("times new roman", 13, "bold"))
        gl.grid(row=2, column=0, padx=10, pady=5, sticky=W) 
        gcb=ttk.Combobox(csframe,textvariable=self.var_gender, font=("times new roman", 13, "bold"), state="readonly", width=18) 
        gcb["values"]=("Female", "Male","Other") 
        gcb.current(0) 
        gcb.grid(row=2,column=1, padx=10, pady=5, sticky=W) 
        #DOB
        dobl=Label(csframe, text="DOB:", font=("times new roman", 13, "bold")) 
        dobl.grid(row=2,column=2, padx=10, pady=5, sticky=W) 
        dobe=Entry(csframe,textvariable=self.var_dob, width=20, font=("times new roman", 13, "bold")) 
        dobe.grid(row=2,column=3, padx=10, pady=5, sticky=W) 
        #EMAIL
        el=Label(csframe, text="Email:", font=("times new roman", 13, "bold"))
        el.grid(row=3,column=0, padx=10, pady=5, sticky=W) 
        ee=Entry(csframe,textvariable=self.var_email, width=20, font=("times new roman", 13, "bold")) 
        ee.grid(row=3,column=1, padx=10, pady=5, sticky=W) 
        #PHONE NO.
        pl=Label(csframe, text="Phone No:", font=("times new roman", 13, "bold"))
        pl.grid(row=3,column=2, padx=10, pady=5, sticky=W) 
        phone_entry=Entry(csframe,textvariable=self.var_phone, width=20, font=("times new roman", 13, "bold")) 
        phone_entry.grid(row=3,column=3, padx=10, pady=5, sticky=W) 
        #ADDRESS
        al=Label(csframe, text="Address:", font=("times new roman", 13, "bold"))
        al.grid(row=4,column=0, padx=10, pady=5, sticky=W) 
        ae=Entry(csframe,textvariable=self.var_address, width=20, font=("times new roman", 13, "bold")) 
        ae.grid(row=4,column=1, padx=10, pady=5, sticky=W) 
        #TEACHER NAME
        tl=Label(csframe, text="Teacher Name:", font=("times new roman", 13, "bold"))
        tl.grid(row=4,column=2, padx=10, pady=5, sticky=W)
        te=Entry(csframe,textvariable=self.var_teacher,width=20, font=("times new roman", 13, "bold")) 
        te.grid(row=4,column=3, padx=10, pady=5, sticky=W) 
        #RADIO BUTTONS
        self.var_radio1=StringVar()
        rb1=ttk.Radiobutton(csframe,variable=self.var_radio1,text="Take Photo Sample",value="Yes").grid(row=6,column=0) 
    
        rb2=ttk.Radiobutton(csframe,variable=self.var_radio1, text="No Photo Sample",value="No").grid(row=6,column=1) 
        #BUTTONS FRAME
        bframe=Frame(csframe,bd=2,relief=RIDGE)
        bframe.place(x=2,y=200,width=760,height=35)

        sb=Button(bframe,text="Save",command=self.add_data, font=("times new roman", 13, "bold"),width=18,bg="navyblue",fg="white")
        sb.grid(row=0,column=0)

        ub=Button(bframe,text="Update",command=self.update_data, font=("times new roman", 13, "bold"),width=18,bg="navyblue",fg="white")
        ub.grid(row=0,column=1)

        dtb=Button(bframe,text="Delete",command=self.delete_data, font=("times new roman", 13, "bold"),width=18,bg="navyblue",fg="white")
        dtb.grid(row=0,column=2)

        rb=Button(bframe,text="Reset",command=self.reset_data, font=("times new roman", 13, "bold"),width=18,bg="navyblue",fg="white")
        rb.grid(row=0,column=3)

        pbframe=Frame(csframe,bd=2,relief=RIDGE)
        pbframe.place(x=2,y=235,width=760,height=35)

        tpb=Button(pbframe,text="Take Photo Sample",command=self.generate_dataset, font=("times new roman", 13, "bold"),width=38,bg="navyblue",fg="white")
        tpb.grid(row=1,column=0)

        upb=Button(pbframe,text="Update Photo Sample",command=self.update_photo_sample, font=("times new roman", 13, "bold"),width=38,bg="navyblue",fg="white")
        upb.grid(row=1,column=1)

        #RIGHT FRAME
        rframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        rframe.place(x=790,y=80,width=730,height=800)
        img6 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/img26.png")
        img6 = img6.resize((780,160), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        self.l3= Label(rframe, image=self.photoimg6)
        self.l3.place(x=0, y=0, width=780, height=160)
        #==============SEARCH SYSTEM==================
        searchframe=LabelFrame(rframe,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        searchframe.place(x=0,y=135,width=726,height=100)

        searchl=Label(searchframe, text="Search By:", font=("times new roman", 15, "bold"))
        searchl.grid(row=0,column=0, padx=10, pady=5, sticky=W)

        self.var_search_by = StringVar()
        
        self.searchcb = ttk.Combobox(searchframe, font=("times new roman", 12), state="readonly", width=12)
        self.searchcb["values"] = ("Select", "Roll no.", "Phone no.")
        self.searchcb.current(0)
        self.searchcb.grid(row=0, column=1, padx=2, pady=10, sticky=W)


        self.var_search_txt = StringVar()

        self.searche=Entry(searchframe,textvariable=self.var_search_txt,width=15,font=("times new roman", 14, "bold"))
        self.searche.grid(row=0,column=2,padx=10,sticky=W)

        self.searchb = Button(searchframe, text="Search", font=("times new roman", 12, "bold"), width=14, bg="navyblue", fg="white", command=self.search_data)
        self.searchb.grid(row=0, column=3, padx=4)

        self.showallb = Button(searchframe, text="Show All", font=("times new roman", 12, "bold"), width=14, bg="navyblue", fg="white", command=self.show_all_data)
        self.showallb.grid(row=0, column=4, padx=4)

        #=================TABLE FRAME=======================
        tableframe=LabelFrame(rframe,bd=2,relief=RIDGE)
        tableframe.place(x=0,y=237,width=726,height=400)

        scroll_x=ttk.Scrollbar(tableframe, orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar(tableframe, orient=VERTICAL)
        self.student_table=ttk.Treeview(tableframe,column=("dep","course","year","sem","id","name","div","roll","gender","dobs","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview) 
        scroll_y.config(command=self.student_table.yview)
        self.student_table["show"] = "headings"

        self.student_table.heading("dep", text="Department", anchor="center") 
        self.student_table.heading("course", text="Course", anchor="center") 
        self.student_table.heading("year", text="Year", anchor="center") 
        self.student_table.heading("sem", text="Semester", anchor="center") 
        self.student_table.heading("id", text="Student_Id", anchor="center") 
        self.student_table.heading("name", text="Name", anchor="center") 
        self.student_table.heading("div", text="Division", anchor="center") 
        self.student_table.heading("roll", text="RollNo.", anchor="center")
        self.student_table.heading("gender", text="Gender", anchor="center")
        self.student_table.heading("dobs", text="DOB", anchor="center") 
        self.student_table.heading("email", text="Email", anchor="center") 
        self.student_table.heading("phone", text="Phone", anchor="center") 
        self.student_table.heading("address", text="Address", anchor="center") 
        self.student_table.heading("teacher", text="Teacher", anchor="center") 
        self.student_table.heading("photo", text="Photo_Sample_Status", anchor="center") 
        

        self.student_table.column("dep",anchor="center", width=150) 
        self.student_table.column("course",anchor="center", width=150) 
        self.student_table.column("year",anchor="center", width=150) 
        self.student_table.column("sem",anchor="center", width=150) 
        self.student_table.column("id",anchor="center", width=150) 
        self.student_table.column("name",anchor="center", width=150) 
        self.student_table.column("roll",anchor="center", width=150) 
        self.student_table.column("gender",anchor="center", width=150) 
        self.student_table.column("div",anchor="center", width=150) 
        self.student_table.column("dobs",anchor="center", width=150) 
        self.student_table.column("email",anchor="center", width=150) 
        self.student_table.column("phone",anchor="center", width=150) 
        self.student_table.column("address",anchor="center", width=150) 
        self.student_table.column("teacher",anchor="center", width=150) 
        self.student_table.column("photo",anchor="center", width=150) 
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

   # ================== function declarations ==================

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = sqlite3.connect("face_recognizer.db")
                cursor = conn.cursor()

                # Create table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS student (
                        Dep TEXT,
                        Course TEXT,
                        Year TEXT,
                        Semester TEXT,
                        Student_id TEXT PRIMARY KEY,
                        Name TEXT,
                        Division TEXT,
                        Roll TEXT,
                        Gender TEXT,
                        DOB TEXT,
                        Email TEXT,
                        Phone TEXT,
                        Address TEXT,
                        Teacher TEXT,
                        PhotoSample TEXT
                    )
                """)

                # Insert into table
                cursor.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student record has been added!", parent=self.root)

            except Exception as e:
                messagebox.showerror("Error", f"Due To: {str(e)}", parent=self.root)

    # ================== Fetch data ==================

    def fetch_data(self):
        conn = sqlite3.connect("face_recognizer.db")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in data:
                self.student_table.insert("", END, values=row)
            conn.commit()
        conn.close()
    #================search data=====================
    def search_data(self):
        search_by = self.searchcb.get()
        search_value = self.searche.get()

        if search_by == "Select" or search_value == "":
            messagebox.showerror("Error", "Please select a search criteria and enter a value", parent=self.root)
        else:
            try:
                conn = sqlite3.connect("face_recognizer.db")
                my_cursor = conn.cursor()

                if search_by == "Roll no.":
                    query = "SELECT * FROM student WHERE Roll = ?"
                elif search_by == "Phone no.":
                    query = "SELECT * FROM student WHERE Phone = ?"
                else:
                    messagebox.showerror("Error", "Invalid search criteria", parent=self.root)
                    return

                my_cursor.execute(query, (search_value,))
                rows = my_cursor.fetchall()

                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert("", END, values=row)
                else:
                    messagebox.showinfo("No Result", "No record found", parent=self.root)

                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def show_all_data(self):
        self.fetch_data()



    # ================== Get cursor ==================

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        if data:
            self.var_dep.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_semester.set(data[3])
            self.var_std_id.set(data[4])
            self.var_std_name.set(data[5])
            self.var_div.set(data[6])
            self.var_roll.set(data[7])
            self.var_gender.set(data[8])
            self.var_dob.set(data[9])
            self.var_email.set(data[10])
            self.var_phone.set(data[11])
            self.var_address.set(data[12])
            self.var_teacher.set(data[13])
            self.var_radio1.set(data[14])

    # ================== Update ==================

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if update:
                    conn = sqlite3.connect("face_recognizer.db")
                    my_cursor = conn.cursor()
                    my_cursor.execute("""
                        UPDATE student SET 
                            Name=?, Roll=?, Dep=?, Course=?, Year=?, Semester=?, 
                            Division=?, Gender=?, DOB=?, Email=?, Phone=?, 
                            Address=?, Teacher=?, PhotoSample=?
                        WHERE Student_id=?
                    """, (
                        self.var_std_name.get(),
                        self.var_roll.get(),
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_div.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # ================== Delete ==================

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student?", parent=self.root)
                if delete:
                    conn = sqlite3.connect("face_recognizer.db")
                    my_cursor = conn.cursor()
                    my_cursor.execute("DELETE FROM student WHERE Student_id = ?", (self.var_std_id.get(),))
                    conn.commit()
                    conn.close()
                    self.fetch_data()
                    messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # ================== Reset ==================

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #================update photo sample====================

    def update_photo_sample(self):
        if self.var_roll.get() == "":
            messagebox.showerror("Error", "Please enter the Roll Number to update photo!", parent=self.root)
            return

        try:
            conn = sqlite3.connect("face_recognizer.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM student WHERE Roll = ?", (self.var_roll.get(),))
            data = cursor.fetchone()

            if data is None:
                messagebox.showerror("Error", "Student not found!", parent=self.root)
            else:
                self.generate_dataset()  
                messagebox.showinfo("Success", "Photo sample updated!", parent=self.root)
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)


    # ================== Generate Dataset ==================

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = sqlite3.connect("face_recognizer.db")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                myresult = my_cursor.fetchall()
                id = 0
                for _ in myresult:
                    id += 1

                my_cursor.execute("""
                    UPDATE student SET 
                        Name=?, Roll=?, Dep=?, Course=?, Year=?, Semester=?, 
                        Division=?, Gender=?, DOB=?, Email=?, Phone=?, 
                        Address=?, Teacher=?, PhotoSample=?
                    WHERE Student_id=?
                """, (
                    self.var_std_name.get(),
                    self.var_roll.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ========== load predefined data on face frontals from opencv =============
                import os
                if not os.path.exists("data"):
                    os.makedirs("data")
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        return img[y:y + h, x:x + w]

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed!", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    app = Student(root)
    root.mainloop()
