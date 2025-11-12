import cv2

image = cv2.imread(r'Image_processing\rawImages\python_img.jpg')

if image is not None:
    # Save the image to a new file
    #syntax: cv2.imwrite(filename, image)
    success = cv2.imwrite(r'Image_processing\Saved_img\python_img_copy.jpg', image)
    if success:
        print("Image saved successfully.")
    else:
        print("Failed to save image.")
