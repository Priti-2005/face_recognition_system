from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import sqlite3
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        self.attendance_marked_ids = []

        l5 = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 40, "bold"),
                   bg="white", fg="navyblue")
        l5.place(x=0, y=0, width=1700, height=50)

        # 1ST IMAGE
        img29 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/Img29.jpg")
        img29 = img29.resize((680, 740), Image.LANCZOS)
        self.photoimg29 = ImageTk.PhotoImage(img29)
        self.l4 = Label(self.root, image=self.photoimg29)
        self.l4.place(x=0, y=50, width=680, height=740)

        # 2ND IMAGE
        img13 = Image.open(r"C:/Users/22-4-2/Desktop/Project/PROJECT IMG/Img13.webp")
        img13 = img13.resize((850, 740), Image.LANCZOS)
        self.photoimg13 = ImageTk.PhotoImage(img13)
        self.l5 = Label(self.root, image=self.photoimg13)
        self.l5.place(x=680, y=50, width=850, height=740)

        # Face Recognition Button
        b1_1 = Button(self.l5, text="Face Recognition", command=self.face_recog, cursor="hand2",
                      font=("times new roman", 18, "bold"), bg="green", fg="white")
        b1_1.place(x=295, y=650, width=250, height=40)

    def mark_attendance(self, i, r, n, d):
        if i == "Unknown" or r == "Unknown" or n == "Unknown" or d == "Unknown":
            return

        file_path = "face.csv"
        if not os.path.exists(file_path):
            with open(file_path, "w", newline="\n") as f:
                f.write("ID,Roll,Name,Department,Time,Date,Status\n")

        if i in self.attendance_marked_ids:
            return

        now = datetime.now()
        d1 = now.strftime("%d/%m/%y")
        dtString = now.strftime("%H:%M:%S")

        with open(file_path, "a", newline="\n") as f:
            f.writelines(f"{i},{r},{n},{d},{dtString},{d1},Present\n")

        self.attendance_marked_ids.append(i)

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = sqlite3.connect("face_recognizer.db")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE Student_id=?", (id,))
                n = my_cursor.fetchone()
                n = n[0] if n else "Unknown"

                my_cursor.execute("SELECT Roll FROM student WHERE Student_id=?", (id,))
                r = my_cursor.fetchone()
                r = r[0] if r else "Unknown"

                my_cursor.execute("SELECT Dep FROM student WHERE Student_id=?", (id,))
                d = my_cursor.fetchone()
                d = d[0] if d else "Unknown"

                my_cursor.execute("SELECT Student_id FROM student WHERE Student_id=?", (id,))
                i = my_cursor.fetchone()
                i = i[0] if i else "Unknown"

                if confidence > 60:
                    cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                    cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Roll: {r}", (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Dep: {d}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 0), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty("Welcome To Face Recognition", cv2.WND_PROP_VISIBLE) < 1:
                break

        video_cap.release()
        cv2.destroyAllWindows()


# Run GUI
if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition(root)
    root.mainloop()
