from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from student import Student
import os
from time import strftime
from datetime import datetime
from train import Train
from face_rec import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        #image1
        img1 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/img1.jpg")
        img1 = img1.resize((550, 150), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        self.l1= Label(self.root, image=self.photoimg1).place(x=0, y=0, width=550, height=150)
        #image 2
        img2= Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/img2.jpg")
        img2 = img2.resize((550, 150), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        self.l2= Label(self.root, image=self.photoimg2).place(x=550, y=0, width=550, height=150)
        #image3
        img3 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/img3.jpg")
        img3 = img3.resize((560, 150), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        self.l2= Label(self.root, image=self.photoimg3).place(x=1100, y=0, width=560, height=150)
        #bg image
        img4 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/IMG4.jpg")
        img4 = img4.resize((1700, 800), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        self.l = Label(self.root, image=self.photoimg4).place(x=0, y=150, width=1700, height=800)

        self.l4=Label(self.root,text="FACE  RECOGNITION  ATTENDANCE  SYSTEM ",font=("times new roman", 40, "bold"), bg="white", fg="navyblue")
        self.l4.place(x=0, y=150, width=1700, height=50)

        #===========time=================
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(self.l4,font=('times new roman',13,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        #student button
        img5 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/img5.webp")
        img5 = img5.resize((240,220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.photoimg5,command=self.student_details,cursor="hand2").place(x=200,y=250,width=240,height=220)
        b1_1=Button(self.root,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman", 20, "bold"), bg="skyblue", fg="navyblue").place(x=200,y=450,width=240,height=40)
        #face detector button
        img6 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/img6.jfif")
        img6 = img6.resize((240,220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b2=Button(self.root,image=self.photoimg6,cursor="hand2",command=self.face_data).place(x=520,y=250,width=240,height=220)
        b2_2=Button(self.root,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman", 20, "bold"), bg="skyblue", fg="navyblue").place(x=520,y=450,width=240,height=40)
        #attendance button
        img7 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/img7.png")
        img7 = img7.resize((240,220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b3=Button(self.root,image=self.photoimg7,cursor="hand2",command=self.attendance_data).place(x=840,y=250,width=240,height=220)
        b3_3=Button(self.root,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman", 20, "bold"), bg="skyblue", fg="navyblue").place(x=840,y=450,width=240,height=40)
        #help desk button
        img8 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/img8.jpg")
        img8 = img8.resize((240,220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b4=Button(self.root,image=self.photoimg8,cursor="hand2",command=self.help_data).place(x=1160,y=250,width=240,height=220)
        b4_4=Button(self.root,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman", 20, "bold"), bg="skyblue", fg="navyblue").place(x=1160,y=450,width=240,height=40)
        #train data button
        img9 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/img9.jpg")
        img9 = img9.resize((240,220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b5=Button(self.root,image=self.photoimg9,cursor="hand2",command=self.train_data).place(x=200,y=530,width=240,height=220)
        b5_5=Button(self.root,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman", 20, "bold"), bg="skyblue", fg="navyblue").place(x=200,y=730,width=240,height=40)
        #photos button
        img10 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/img10.jpg")
        img10 = img10.resize((240,220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b6=Button(self.root,image=self.photoimg10,cursor="hand2",command=self.open_img).place(x=520,y=530,width=240,height=220)
        b6_6=Button(self.root,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman", 20, "bold"), bg="skyblue", fg="navyblue").place(x=520,y=730,width=240,height=40)
        #developers button
        img11 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/img11.jpg")
        img11 = img11.resize((240,220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b7=Button(self.root,image=self.photoimg11,cursor="hand2",command=self.developer_data).place(x=840,y=530,width=240,height=220)
        b7_7=Button(self.root,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman", 20, "bold"), bg="skyblue", fg="navyblue").place(x=840,y=730,width=240,height=40)
        #exit button
        img12 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/img12.jpg")
        img12 = img12.resize((240,220), Image.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)
        b7=Button(self.root,image=self.photoimg12,cursor="hand2",command=self.i_Exit).place(x=1160,y=530,width=240,height=220)
        b7_7=Button(self.root,text="Exit",cursor="hand2",command=self.i_Exit,font=("times new roman", 20, "bold"), bg="skyblue", fg="navyblue").place(x=1160,y=730,width=240,height=40)


    def open_img(self):
        os.startfile("data")

    def i_Exit(self):
        self.i_Exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.i_Exit>0:
            self.root.destroy()
        else:
            return
    #==================================function buttons========================================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)


    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)




if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition_System(root)
    root.mainloop()

        




