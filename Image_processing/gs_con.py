#grey scale conversion
import cv2
image = cv2.imread(r'Image_processing\rawImages\python_img.jpg')
if image is not None:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Optionally, save the grayscale image
    cv2.imwrite(r'Image_processing\Saved_img\python_img_grayscale.jpg', gray_image)
else:
    print("Failed to load image.")