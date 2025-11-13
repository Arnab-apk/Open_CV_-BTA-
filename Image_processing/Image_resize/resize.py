import cv2
image = cv2.imread(r'Image_processing\rawImages\python_img.jpg')
if image is not None:
    # Resize the image to 200x200 pixels
    # syntax : cv2.resize(image, (width, height),fx, fy, interpolation)
    resized_image = cv2.resize(image, (200, 200))
    cv2.imshow('Resized Image', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    