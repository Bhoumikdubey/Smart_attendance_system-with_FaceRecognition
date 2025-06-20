import cv2
import face_recognition
import numpy as np
import pickle
import pandas as pd
from datetime import datetime
import os
import time
import tkinter as tk
from tkinter import messagebox

# time.sleep(2)

# Load known face encodings
with open("encodings_new.pkl", "rb") as f:
    data = pickle.load(f)

known_face_encodings = data["encodings"]
known_face_names = data["names"]

# Initialize attendance file
attendance_file = "attendance.csv"

# Start webcam
video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_frame = small_frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(
            known_face_encodings, face_encoding
        )
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

            # Mark attendance
            df = (
                pd.read_csv(attendance_file)
                if os.path.exists(attendance_file)
                else pd.DataFrame(columns=["Name", "Time"])
            )
            with open('W:\dataset\latest_attendance.txt', 'w+') as f:
                    f.write(name)
            if name not in df["Name"].values:
                
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # df = df.append({"Name": name, "Time": now}, ignore_index=True)
                df = pd.concat(
                    [df, pd.DataFrame([{"Name": name, "Time": now}])], ignore_index=True
                )
                df.to_csv(attendance_file, index=False)

        # Draw rectangle around face
        top, right, bottom, left = [i * 4 for i in face_location]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(
            frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2
        )

    cv2.imshow("Smart Attendance", frame)
     # Stop after one capture
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()

'''def start_gui():
    root = tk.Tk()
    root.title("Face Recognition Attendance System")
    root.geometry("400x300")

    label = tk.Label(
        root, text="Face Recognition Attendance System", font=("Arial", 14)
    )
    label.pack(pady=20)

    start_button = tk.Button(
        root, text="Start Recognition", command=start_recognition, font=("Arial", 12)
    )
    start_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12))
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "_main_":
    start_gui()'''
