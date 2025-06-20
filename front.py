import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import webbrowser

def run_face_recognition():
    '''file_path = filedialog.askopenfilename(title="Select Image for Face Recognition")
    if not file_path:
        return'''
    
    try:
        # Run your face recognition script (Replace 'face_recognition.py' with your actual script name)
        result = subprocess.run(["python", "second.py",''' file_path'''], check=True,capture_output=True,shell=True,text=True)
        messagebox.showinfo("Success", "Face recognition completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def open_html_report():
    html_file = "output.html"  # Ensure this matches the output of your face recognition script
    with open('W:\dataset\latest_attendance.txt','r') as f:
        name = f.read().strip()
    # name = 'bhoumik.jpg'
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Face Recognition Results</title>
    <link rel="stylesheet" href="styles.css">
</head>
<script>
    document.readyState
</script>
<body>
    <h1>Face Recognition Results</h1>
    <p>Processed Image:</p>
    <img src="W:\dataset\person\known_faces\{name}" alt="Processed Face Recognition Result">
    <p>Detected Faces and Details:</p>
    <div id="results">
        <p>No results yet. Run the face recognition script to update this file.</p>
    </div>
</body>
</html>'''
    
    with open('W:\dataset\html_report.html','w+') as f:
        f.write(html)
    
    webbrowser.open('W:\dataset\html_report.html')

# Create main GUI window
root = tk.Tk()
root.title("Face Recognition Interface")
root.geometry("400x300")

# Buttons
select_btn = tk.Button(root, text="Start Today's Attendance", command=run_face_recognition)
select_btn.pack(pady=20)

view_btn = tk.Button(root, text="View Attendance Report", command=open_html_report)
view_btn.pack(pady=20)

exit_btn = tk.Button(root, text="Exit", command=root.quit)
exit_btn.pack(pady=20)

# Run the Tkinter loop
root.mainloop()