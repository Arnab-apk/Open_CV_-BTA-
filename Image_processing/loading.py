import cv2

image=cv2.imread(r'Image_processing\rawImages\python_img.jpg')

if image is not None:
    print("Image loaded successfully.")
else:
    print("Failed to load image.")
    