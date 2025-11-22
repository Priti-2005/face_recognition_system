from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import cv2
import webbrowser  # Import added

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        l6 = Label(self.root, text="HELP DESK", font=("times new roman", 40, "bold"), bg="white", fg="navyblue")
        l6.place(x=0, y=0, width=1700, height=45)

        # IMAGE
        img17 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/IMG17.jpg")
        img17 = img17.resize((1550, 790), Image.LANCZOS)
        self.photoimg17 = ImageTk.PhotoImage(img17)
        self.l7 = Label(self.root, image=self.photoimg17)
        self.l7.place(x=0, y=45, width=1550, height=790)

        # Clickable Email Label
        di2 = Label(self.l7, text="Email: programmerpython42@gmail.com", font=("times new roman", 20, "bold"),
                    fg="navyblue", bg="white", cursor="hand2")
        di2.place(x=520, y=210)
        di2.bind("<Button-1>", self.send_email)  # Event binding

    def send_email(self, event=None):
        # Mailto link with pre-filled subject and body
        email = "programmerpython42@gmail.com"
        subject = "Help Needed"
        body = "Dear Team,\n\nI need assistance with the Face Recognition System.\nPlease get back to me.\n\nThank you."
        webbrowser.open(f"mailto:{email}?subject={subject}&body={body}")



if __name__ == "__main__":
    root = Tk()
    app = Help(root)
    root.mainloop()
