## 🧑‍🏫 Face Recognition Attendance System

A Python-based project that automates attendance using face recognition, built with OpenCV, Tkinter, and machine learning.

## 📌 Project Overview

This project captures real-time images using a webcam, detects faces, and marks attendance automatically by recognizing the student’s face. The system stores records in a database and allows the admin to manage student details through a GUI dashboard.

## 🚀 Features

✔️ Login & Signup System

✔️ Add Student Details (GUI)

✔️ Capture Face Samples

✔️ Train Face Recognition Model

✔️ Real-Time Attendance with Camera

✔️ Attendance Report in CSV Format

✔️ Search & Manage Student Records

✔️ SQLite / MySQL Support

✔️ Attractive Tkinter GUI

## 🏗️ Tech Stack

Python

Tkinter – GUI

OpenCV – Face Detection & Recognition

NumPy

PIL / Pillow – Image handling

SQLite / MySQL – Database

CSV – Attendance reports

## 📸 How It Works

Admin adds a student with name, roll number, division, etc.

System captures 50–100 face images of the student.

Model trains on these images.

During attendance:

Camera opens

Face is detected

Model matches face with database

Attendance is marked automatically with Name + Time + Date

## 📁 Project Folder Structure
Face-Recognition-Attendance-System/
│── attendance/           → Attendance CSV files  
│── data/                 → Captured face samples  
│── trainer/              → Trained model file  
│── database/             → SQLite/MySQL database  
│── main.py               → Main GUI file  
│── train.py              → Model training script  
│── detector.py           → Face detection logic  
│── readme.md             → Project readme  

## 🛠️ Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/Face-Recognition-Attendance-System.git

2️⃣ Install Dependencies
pip install opencv-python
pip install numpy
pip install pillow
pip install mysql-connector-python   # If using MySQL

## ▶️ How to Run
python main.py

## 📊 Attendance Output Example

CSV includes:

Student ID

Name

Date

Time

Status (Present)

## ⭐ Future Enhancements

Add email alerts

Add admin panel analytics

Add mobile app integration

Cloud database support

## 🤝 Contributing

Pull requests are welcome!

## 📝 License

This project is open-source and free to use.
