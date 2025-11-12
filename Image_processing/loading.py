import cv2

image=cv2.imread('Image_processing\python_img.jpg')

if image is not None:
    print("Image loaded successfully.")
else:
    print("Failed to load image.")
    