import cv2
image = cv2.imread(r'Image_processing\rawImages\python_img.jpg')
if image is not None:
    #original dimensions
    height, width = image.shape[:2]
    print(f"Original Dimensions: Width={width}, Height={height}")
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #slicing the image
    #syntax: image[y1:y2, x1:x2]
    #image[startY:endY, startX:endX]
    cropped_image = image[50:300, 100:301]
    cropped_height, cropped_width = cropped_image.shape[:2]
    print(f"Cropped Dimensions: Width={cropped_width}, Height={cropped_height}")
    cv2.imshow('Cropped Image', cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Failed to load image.")
    