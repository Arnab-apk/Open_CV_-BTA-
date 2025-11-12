import cv2
#The imshow function displays an image in a window.
#The waitKey function waits for a key event indefinitely (0) or for a specified amount of time in milliseconds.
#The destroyAllWindows function closes all OpenCV windows.
image = cv2.imread('Image_processing\python_img.jpg')

if image is not None:
    cv2.imshow('Python Logo', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Failed to load image.")


