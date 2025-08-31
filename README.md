📌 Smart Attendance Management System using Face Recognition

📖 Overview

The Smart Attendance Management System is a Django-based web application that leverages Face Recognition technology to automate student attendance marking. It eliminates manual errors, ensures accuracy, and provides real-time attendance reports for both students and teachers.


---

✨ Features

🔑 Student Login → Secure access for students to mark attendance.

👨‍🏫 Teacher Login → Dedicated dashboard for teachers to manage and monitor attendance.

🎥 Face Recognition Integration → Attendance is marked automatically when a student is recognized by the system.

💾 Database Storage → Attendance data securely stored in MySQL/SQLite.

📊 Reports & Dashboard → Teachers can generate attendance reports and verify records.

🎨 Responsive UI → Built using HTML, CSS, JavaScript, Bootstrap for smooth interaction.



---

🛠️ Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS, JavaScript, Bootstrap

Face Recognition: OpenCV, dlib

Database: MySQL / SQLite

Tools: Git, XAMPP / MySQL Workbench
Project Structure

Smart-Attendance-System/
│── manage.py
│── requirements.txt
│── db.sqlite3
│── attendance/        # Main Django app
│── templates/         # HTML templates
│── static/            # CSS, JS, Images
│── media/             # Student images dataset
│── README.md


---

⚙️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/Tharun9113/Face_recognition_attendance_management_system

2️⃣ Create Virtual Environment

python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run Database Migrations

python manage.py makemigrations
python manage.py migrate

5️⃣ Start the Server

python manage.py runserver

Now visit 👉 http://127.0.0.1:8000/


---

📊 Future Enhancements

🔐 Integration with Multi-Factor Authentication (MFA).

📱 Mobile App for students to view attendance in real-time.

☁️ Cloud Deployment (Heroku/AWS) for scalability.

📈 Advanced analytics for attendance insights.



---

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.


---

📜 License

This project is licensed under the MIT License – feel free to use and modify it.


---


