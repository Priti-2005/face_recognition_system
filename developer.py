from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        l6 = Label(self.root, text="DEVELOPER", font=("times new roman", 40, "bold"),bg="white", fg="navyblue")
        l6.place(x=0, y=0, width=1700, height=45)

        #IMAGE
        img15 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/img15.jpg")
        img15 = img15.resize((1550, 790), Image.LANCZOS)
        self.photoimg15 = ImageTk.PhotoImage(img15)
        self.l5 = Label(self.root, image=self.photoimg15)
        self.l5.place(x=0, y=45, width=1550, height=790)
        
        #frame

        self.fleft = Frame(self.l5, bd=2)
        self.fleft.place(x=5, y=45, width=500, height=600)

        self.fcenter = Frame(self.l5, bd=2)
        self.fcenter.place(x=515, y=45, width=500, height=600)

        self.fright=Frame(self.l5,bd=2)
        self.fright.place(x=1025,y=45,width=500,height=600)

        #developers info
        #DEVELOPER 1
        di11 = Label(self.fleft, text="Developer 1: Priti", font=("times new roman", 20, "bold"))
        di11.place(x=0, y=5)

        di12 = Label(self.fleft, text="Pursuing BTech at ACE", font=("times new roman", 18))
        di12.place(x=0, y=40)

        di13 = Label(self.fleft, text="Python Programmer", font=("times new roman", 18))
        di13.place(x=0, y=70)

        di14 = Label(self.fleft, text="Familiar with Tkinter for GUI Development", font=("times new roman", 18))
        di14.place(x=0, y=100)

        di15 = Label(self.fleft, text="Developed Face Recognition Attendance System", font=("times new roman", 18))
        di15.place(x=0, y=130)

        #DEVELOPER 2
        di21 = Label(self.fcenter, text="Developer 2: Anu Saini", font=("times new roman", 20, "bold"))
        di21.place(x=0, y=5)

        di22 = Label(self.fcenter, text="Pursuing BTech at ACE", font=("times new roman", 18))
        di22.place(x=0, y=40)

        di23 = Label(self.fcenter, text="Python & Java Programmer", font=("times new roman", 18))
        di23.place(x=0, y=70)

        di24 = Label(self.fcenter, text="Familiar with Tkinter for GUI Development", font=("times new roman", 18))
        di24.place(x=0, y=100)

        di25 = Label(self.fcenter, text="Developed Face Recognition Attendance System", font=("times new roman", 18))
        di25.place(x=0, y=130)

        #DEVELOPER 3
        di31 = Label(self.fright, text="Developer 3: Vanshika", font=("times new roman", 20, "bold"))
        di31.place(x=0, y=5)

        di32 = Label(self.fright, text="Pursuing BTech at ACE", font=("times new roman", 18))
        di32.place(x=0, y=40)

        di33 = Label(self.fright, text="Python Programmer", font=("times new roman", 18))
        di33.place(x=0, y=70)

        di34 = Label(self.fright, text="Familiar with Data Analysis techniques and tools", font=("times new roman", 18))
        di34.place(x=0, y=100)

        di35 = Label(self.fright, text="Developed Face Recognition Attendance System", font=("times new roman", 18))
        di35.place(x=0, y=130)


        img16 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/img16.webp")
        img16 = img16.resize((500,400), Image.LANCZOS)
        self.photoimg16 = ImageTk.PhotoImage(img16)
        self.l6 = Label(self.fleft, image=self.photoimg16)
        self.l6.place(x=0, y=250, width=500, height=400)

        img18 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/img18.webp")
        img18 = img18.resize((500,400), Image.LANCZOS)
        self.photoimg18 = ImageTk.PhotoImage(img18)
        self.l8 = Label(self.fcenter, image=self.photoimg18)
        self.l8.place(x=0, y=250, width=500, height=400)

        img19 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/img19.jfif")
        img19 = img19.resize((500,400), Image.LANCZOS)
        self.photoimg19 = ImageTk.PhotoImage(img19)
        self.l9 = Label(self.fright, image=self.photoimg19)
        self.l9.place(x=0, y=250, width=500, height=400)


if __name__ == "__main__":
    root = Tk()
    app = Developer(root)
    root.mainloop()


  
