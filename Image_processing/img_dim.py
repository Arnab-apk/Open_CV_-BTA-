import cv2
image=cv2.imread(r'Image_processing\rawImages\python_img.jpg')
# Get image dimensions
# The shape attribute returns a tuple of (height, width, channels)
# height: number of rows, width: number of columns, channels: number of color channels
# For a color image, channels will typically be 3 (BGR)
# For a grayscale image, channels will be 1
# Example output: (480, 640, 3) for a 640x480 color image
if image is not None:
    height, width, channels = image.shape
    print(f"Image Dimensions: {width}x{height} pixels")
    print(f"Number of Channels: {channels}")
else:
    print("Failed to load image.")