from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
from main import Face_Recognition_System

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1700x900")
        self.root.title("Login System")

        self.username = StringVar()
        self.password = StringVar()

        # ===== Set Background Image First =====
        img4 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/IMG4.jpg")
        img4 = img4.resize((1700, 900), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=0, width=1700, height=900)

        # ===== Heading on top =====
        title = Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM",
                      font=("times new roman", 40, "bold"), bg="white", fg="navyblue")
        title.place(x=0, y=0, width=1700, height=70)

        # ===== Frame on top of background =====
        self.frame = Frame(self.root, bg='DodgerBlue2', bd=5)
        self.frame.place(x=380, y=200, width=850, height=450)

        Label(self.frame, text='Admin Login', font=('times new roman', 22, 'bold'),bg='DodgerBlue2').place(x=350, y=20)

        Label(self.frame, text="Username", font=('times new roman', 20, 'bold'), bg='DodgerBlue2').place(x=160, y=100)
        Label(self.frame, text="Password", font=('times new roman', 20, 'bold'), bg='DodgerBlue2').place(x=160, y=160)
        
        self.e1 = Entry(self.frame, textvariable=self.username, bd=5, font=('times new roman', 20),width=30, bg="DarkSlateGray1", fg='black')
        self.e1.place(x=290, y=100)
        self.e2 = Entry(self.frame, textvariable=self.password, bd=5, font=('times new roman', 20),width=30, bg="DarkSlateGray1", fg='black', show='*')
        self.e2.place(x=290, y=160)

        Button(self.frame, text="Login", font=('times new roman', 16, 'bold'), padx=10, pady=5, bd=3,bg="navyblue", fg='white', width=18, command=self.login).place(x=25, y=300)
        Button(self.frame, text="Sign Up", font=('times new roman', 16, 'bold'), padx=10, pady=5, bd=3,bg="navyblue", fg='white', width=18, command=self.signup).place(x=310, y=300)
        Button(self.frame, text="Reset", font=('times new roman', 16, 'bold'), padx=10, pady=5, bd=3,bg="navyblue", fg='white', width=17, command=self.clears).place(x=590, y=300)

    def signup(self):
        conn = sqlite3.connect("project3.db")
        cursor = conn.cursor()
        usernames = self.username.get().strip()
        passwords = self.password.get().strip()

        if not usernames:
            messagebox.showinfo("Signup", "Please enter username")
            return
        if not passwords:
            messagebox.showinfo("Signup", "Please enter password")
            return

        cursor.execute("CREATE TABLE IF NOT EXISTS login(username CHAR(20) NOT NULL, password CHAR(20) NOT NULL)")
        cursor.execute("INSERT INTO login(username, password) VALUES (?, ?)", (usernames, passwords))
        conn.commit()
        conn.close()

        messagebox.showinfo("Signup Success", "You are now registered")

    def login(self):
        usernames = self.username.get().strip()
        passwords = self.password.get().strip()
        conn = sqlite3.connect("project3.db")
        cursor = conn.cursor()
        if not usernames:
            messagebox.showinfo("Login", "Please enter username")
            return
        if not passwords:
            messagebox.showinfo("Login", "Please enter password")
            return

        cursor.execute("SELECT * FROM login WHERE username = ? AND password = ?", (usernames, passwords))
        if cursor.fetchone() is None:
            messagebox.showinfo("Login", "Incorrect username or password")
        else:
            messagebox.showinfo("Login", "Welcome Admin!")
            self.root.destroy()
            import main
            new_root=Tk()
            obj = main.Face_Recognition_System(new_root)
            new_root.mainloop
        conn.close()

    def clears(self):
        self.username.set("")
        self.password.set("")

if __name__ == "__main__":
    root = Tk()
    app = Login(root)
    root.mainloop()
