Smart Attendance System Using Facial Recognition

A Python-based smart attendance tracker that leverages facial recognition technology to mark and manage attendance efficiently. This hybrid application combines a desktop interface built with Tkinter and web elements styled with HTML/CSS for a sleek user experience. Attendance records are stored and managed using CSV files, making it lightweight and highly portable.
🔍 Features
- 🎯 Facial Recognition using OpenCV and face encodings
- 📝 CSV-based Storage for attendance logs (no need for complex databases)
- 🧠 Smart Matching Algorithm to detect and mark student presence
- 🖥️ Tkinter GUI for easy navigation and admin controls
- 🌐 Responsive Web View with HTML and CSS to display attendance reports
- 📂 Attendance history export and real-time recognition logs
  
🧰 Tech Stack
- Python (Core logic & facial recognition)
- OpenCV & face_recognition (Image processing)
- Tkinter (Desktop UI)
- HTML/CSS (Web interface)
- CSV (Data storage)

📸 How It Works
- Capture and register student faces through the GUI.
- Live camera feed scans and matches student faces.
- If a match is found, it automatically logs the student as present.
- Attendance records are saved in a date-wise CSV file.
- Admin can view and export the data via desktop or browser.
 
🚀 Getting Started
- Clone the repository.
- Install dependencies with pip install -r requirements.txt.
- Run main.py to launch the application.
- Start marking attendance with a webcam!
  
📌 Future Enhancements
- Database integration (e.g., SQLite or Firebase)
- Email notifications for absentees
- Role-based login (Admin, Faculty)
- Graphical analytics dashboards
