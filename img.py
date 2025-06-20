# import cv2

# # Load the image
# image = cv2.imread("W:\dataset\person\img2.JPG")  # Replace with your image file path

# # Convert to 8-bit grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Save the converted image
# cv2.imwrite("W:\dataset\person\output_gray.jpg", gray_image)  # Change path if needed

# print("Image successfully converted to 8-bit grayscale and saved!")

from PIL import Image

# Open the image
img = Image.open("W:\dataset\person\img2.JPG")

# Convert the image to grayscale
img_gray = img.convert("L")

# Save the grayscale image
img_gray.save("W:\dataset\person\output_gray_pillow")