from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        Label(self.root, text="TRAIN DATA SET", font=("times new roman", 40, "bold"),
              bg="white", fg="navyblue").place(x=0, y=0, width=1700, height=50)

        img27 = Image.open("C:/Users/22-4-2/Desktop/Project/PROJECT IMG/Img27.png").resize((1530, 365), Image.LANCZOS)
        self.photoimg27 = ImageTk.PhotoImage(img27)
        Label(self.root, image=self.photoimg27).place(x=0, y=50, width=1530, height=365)

        Button(self.root, text="TRAIN DATA", cursor="hand2", font=("times new roman", 30, "bold"),
               bg="navyblue", fg="white", command=self.train_classifier).place(x=0, y=380, width=1530, height=60)

        img28 = Image.open("C:/Users/22-4-2/Desktop/Project/PROJECT IMG/Img28.jpg").resize((1530, 365), Image.LANCZOS)
        self.photoimg28 = ImageTk.PhotoImage(img28)
        Label(self.root, image=self.photoimg28).place(x=0, y=440, width=1530, height=365)

    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir) or len(os.listdir(data_dir)) == 0:
            messagebox.showerror("Error", "No images found in 'data' folder for training!")
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            try:
                img = Image.open(image).convert('L')  # Grayscale
                imageNp = np.array(img, 'uint8')
                id = int(os.path.split(image)[1].split('.')[1])
                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1)
            except Exception as e:
                print(f"Skipping file {image} due to error: {e}")

        ids = np.array(ids)

        # Train and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset completed successfully!")


if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()
