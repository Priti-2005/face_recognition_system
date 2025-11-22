from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #===============variable============

        self.var_atten_id=StringVar() 
        self.var_atten_roll=StringVar()  
        self.var_atten_name=StringVar()  
        self.var_atten_dep=StringVar()  
        self.var_atten_time=StringVar() 
        self.var_atten_date=StringVar() 
        self.var_atten_attendance=StringVar() 

        #image1
        img2= Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/img25.jpg")
        img2 = img2.resize((765,130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        self.l2= Label(self.root, image=self.photoimg2).place(x=0, y=0, width=765, height=130)
        #image2
        img3 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/Img14.jpg")
        img3 = img3.resize((765,130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        self.l2= Label(self.root, image=self.photoimg3).place(x=765, y=0, width=765, height=130)
        
        self.l4=Label(self.root,text="ATTENDANCE  MANAGEMENT  SYSTEM ",font=("times new roman", 40, "bold"), bg="white", fg="navyblue").place(x=0, y=130, width=1700, height=50)

        self.fmain=Frame(self.root,bd=2).place(x=20,y=310,width=1480,height=600)

        #left frame
        lframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        lframe.place(x=15,y=190,width=740,height=595)
        
        img5 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/img26.png")
        img5 = img5.resize((740,130), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        self.l2= Label(lframe, image=self.photoimg5)
        self.l2.place(x=0, y=0, width=740, height=130)

        inside_frame=Frame(lframe,bd=2,relief=RIDGE)
        inside_frame.place(x=0,y=135,width=735,height=400)

        #labels and entry
        
        #attendance id
        aidl=Label(inside_frame, text="AttendanceID:", font=("times new roman", 13, "bold"))
        aidl.grid(row=0,column=0, padx=10, sticky=W)
        aide=Entry(inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman", 13, "bold"))
        aide.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        #rollno.
        rl=Label(inside_frame, text="RollNo.:",font=("times new roman", 13, "bold")) 
        rl.grid(row=0,column=2, padx=4, pady=8) 
        are=Entry(inside_frame,width=20,textvariable=self.var_atten_roll, font=("times new roman", 13, "bold")) 
        are.grid(row=0,column=3, pady=8) 
        #name 
        nl=Label(inside_frame, text="Name:",font=("times new roman", 13, "bold")) 
        nl.grid(row=1,column=0) 
        ane=Entry(inside_frame,width=20,textvariable=self.var_atten_name, font=("times new roman", 13, "bold")) 
        ane.grid(row=1,column=1,pady=8) 
        #Department 
        dl=Label(inside_frame, text="Department:",font=("times new roman", 13, "bold"))
        dl.grid(row=1,column=2)  
        ade=Entry(inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman", 13, "bold")) 
        ade.grid(row=1,column=3,pady=8)
        #time
        tl=Label(inside_frame, text="Time:",font=("times new roman", 13, "bold")) 
        tl.grid(row=2,column=0)
        ate=Entry(inside_frame,width=20,textvariable=self.var_atten_time, font=("times new roman", 13, "bold"))  
        ate.grid(row=2,column=1, pady=8)  
        #Date 
        dl=Label(inside_frame, text="Date:",font=("times new roman", 13, "bold")) 
        dl.grid(row=2,column=2)  
        ad=Entry(inside_frame, width=20,textvariable=self.var_atten_date, font=("times new roman", 13, "bold")) 
        ad.grid(row=2,column=3, pady=8)  
        #attendance 
        al=Label(inside_frame, text="Attendance Status:",font=("times new roman", 13, "bold")) 
        al.grid(row=3,column=0) 
        self.atten_status=ttk.Combobox(inside_frame, width=18,textvariable=self.var_atten_attendance, font=("times new roman", 13, "bold"), state="readonly") 
        self.atten_status ["values"]=("Status", "Present", "Absent") 
        self.atten_status.grid(row=3,column=1,pady=8) 
        self.atten_status.current(0)

        #buttons frame 
        btn_frame=Frame(inside_frame, bd=2, relief=RIDGE, bg="white") 
        btn_frame.place(x=0,y=300,width=735,height=35)
        
        import_btn=Button(btn_frame, text="Import csv",command=self.importCsv,width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white") 
        import_btn.grid(row=0,column=0) 

        export_btn=Button(btn_frame, text="Export csv",command=self.exportCsv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white") 
        export_btn.grid(row=0,column=1)
        
        update_btn=Button(btn_frame, text="Update", width=17,command=self.update_data, font=("times new roman", 13, "bold"), bg="blue", fg="white") 
        update_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame, text="Reset",command=self.reset_data, width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white") 
        reset_btn.grid(row=0,column=3) 
                                
        
        #right frame
        rframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        rframe.place(x=770,y=190,width=745,height=595)

        table_frame=Frame(rframe, bd=2, relief=RIDGE, bg="white") 
        table_frame.place(x=5,y=5,width=730,height=445)

        #Scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendaceReportTable=ttk.Treeview(table_frame,column=("id", "roll", "name", "department", "time", "date", "attendance"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X) 
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)

        self.AttendaceReportTable.heading("id", text="Attendance ID") 
        self.AttendaceReportTable.heading("roll", text="Roll") 
        self.AttendaceReportTable.heading("name", text="Name") 
        self.AttendaceReportTable.heading("department", text="Department") 
        self. AttendaceReportTable.heading("time", text="Time") 
        self.AttendaceReportTable.heading("date", text="Date") 
        self.AttendaceReportTable.heading("attendance", text="Attendance")

        self.AttendaceReportTable["show"]="headings"
        
        self.AttendaceReportTable.column("id", width=100) 
        self.AttendaceReportTable.column("roll", width=100) 
        self.AttendaceReportTable.column("name", width=100) 
        self.AttendaceReportTable.column("department", width=100) 
        self.AttendaceReportTable.column("time", width=100) 
        self.AttendaceReportTable.column("date", width=100) 
        self.AttendaceReportTable.column("attendance", width=100) 
        
        self.AttendaceReportTable.pack(fill=BOTH, expand=1)

        self.AttendaceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #==================import csv=================================
        
    def importCsv(self):  
        global mydata 
        mydata = []
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")],
            parent=self.root
        )
        if fln != "":
            try:
                with open(fln, newline="") as myfile:
                    csvread = csv.reader(myfile, delimiter=",")
                    for i in csvread:
                        mydata.append(i)
                    self.fetchData(mydata)
            except Exception as e:
                messagebox.showerror("Error", f"Error reading file:\n{str(e)}", parent=self.root)
        else:
            messagebox.showinfo("Cancelled", "No file selected.", parent=self.root)

    def fetchData(self, rows):
        global mydata
        mydata = rows
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
        for row in rows:
            self.AttendaceReportTable.insert("", END, values=row)

        self.AttendaceReportTable.column("id", anchor="center")
        self.AttendaceReportTable.column("roll", anchor="center")
        self.AttendaceReportTable.column("name", anchor="center")
        self.AttendaceReportTable.column("department", anchor="center")
        self.AttendaceReportTable.column("time", anchor="center")
        self.AttendaceReportTable.column("date", anchor="center")
        self.AttendaceReportTable.column("attendance", anchor="center")

    #======================export csv===============================

    def exportCsv(self): 
        try: 
            if len(mydata) < 1:  
                messagebox.showerror("No Data", "No data found to export", parent=self.root) 
                return False 
            print("Data to be exported:", mydata)  
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",defaultextension=".csv",filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")],parent=self.root)
            if fln:
                with open(fln, mode="w", newline="") as myfile:
                    exp_write = csv.writer(myfile, delimiter=",")
                    exp_write.writerow(["ID", "Roll", "Name", "Department", "Time", "Date", "Attendance"]) 
                    for i in mydata:
                        exp_write.writerow(i)
                messagebox.showinfo("Data Export", f"Your data was exported to {os.path.basename(fln)} successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
           
    def get_cursor(self,event=""): 
        cursor_row=self.AttendaceReportTable.focus() 
        content=self.AttendaceReportTable.item(cursor_row) 
        rows=content['values']
        if rows and len(rows) >= 7: 
            self.var_atten_id.set(rows[0]) 
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2]) 
            self.var_atten_dep.set(rows[3]) 
            self.var_atten_time.set(rows[4]) 
            self.var_atten_date.set(rows[5])  
            self.var_atten_attendance.set(rows[6])
        else:
            self.reset_data()


    def update_data(self):
        try:
            selected = self.AttendaceReportTable.focus()
            if not selected:
                messagebox.showerror("No Selection", "Please select a row to update.", parent=self.root)
                return
            
            values = (
                self.var_atten_id.get(),
                self.var_atten_roll.get(),
                self.var_atten_name.get(),
                self.var_atten_dep.get(),
                self.var_atten_time.get(),
                self.var_atten_date.get(),
                self.var_atten_attendance.get()
            )

            self.AttendaceReportTable.item(selected, values=values)

            index = self.AttendaceReportTable.index(selected)
            mydata[index] = values

            messagebox.showinfo("Success", "Record updated successfully.", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"Error updating data:\n{str(e)}", parent=self.root)


    def reset_data(self):
        self.var_atten_id.set("") 
        self.var_atten_roll.set("")
        self.var_atten_name.set("") 
        self.var_atten_dep.set("") 
        self.var_atten_time.set("") 
        self.var_atten_date.set("")  
        self.var_atten_attendance.set("")
        
        


if __name__ == "__main__":
    root = Tk()
    app = Attendance(root)
    root.mainloop()

