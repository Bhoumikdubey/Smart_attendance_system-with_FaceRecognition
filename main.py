import cv2
import face_recognition
import os
import pickle
import numpy as np


path = "W:\dataset\person\known_faces"  # Folder with images
known_face_encodings = []
known_face_names = []
from PIL import Image

for file in os.listdir(path):
# imgg = Image.open("W:\dataset\person\img2.JPG").convert("L")
# imgg.save("W:\dataset\person\output_gray_pillow.jpg")
# imgg.dtype
# img = cv2.imread("W:\dataset\person\img2.JPG")
    img = cv2.imread(f"{path}/{file}")
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# img = face_recognition.load_image_file("W:\dataset\person\output_gray_pillow.jpg")
# imgg = face_recognition.load_image_file(rgb_img)[0]
# image=np.array(img)
# images.append(image)
    try:
        encoding = face_recognition.face_encodings(rgb_img)[0]
    except Exception as e:
        print(e)
    known_face_encodings.append(encoding)
    known_face_names.append(file)

data = {"encodings": known_face_encodings, "names": known_face_names}

with open("encodings_new.pkl", "wb") as f:
    pickle.dump(data, f)

print("Face encoding completed.")