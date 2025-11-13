import cv2
import os

def display_menu():
    print("\n" + "="*50)
    print("         IMAGE PROCESSING MENU")
    print("="*50)
    print("1. Load and Display Image")
    print("2. Convert to Grayscale and Save")
    print("3. Save Image to Custom Location")
    print("4. Display and Save Image")
    print("5. Exit")
    print("="*50)
    choice = input("Enter your choice (1-5): ")
    return choice

def load_image():
    image_path = input("\nEnter the image path (e.g., Image_processing\\rawImages\\python_img.jpg): ")
    image = cv2.imread(image_path)
    
    if image is not None:
        print(f"✓ Image loaded successfully from: {image_path}")
        return image
    else:
        print(f"✗ Failed to load image from: {image_path}")
        return None

def display_image(image, title="Image"):
    if image is not None:
        cv2.imshow(title, image)
        print(f"Displaying: {title} (Press any key to close)")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(f"✓ {title} window closed.")
    else:
        print("✗ No image to display.")

def save_image(image, filename):
    if image is not None:
        # Create directory if it doesn't exist
        save_dir = os.path.dirname(filename)
        if save_dir and not os.path.exists(save_dir):
            os.makedirs(save_dir)
        
        success = cv2.imwrite(filename, image)
        if success:
            print(f"✓ Image saved successfully to: {filename}")
            return True
        else:
            print(f"✗ Failed to save image to: {filename}")
            return False
    else:
        print("✗ No image to save.")
        return False

def convert_to_grayscale(image):
    if image is not None:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print("✓ Image converted to grayscale successfully.")
        return gray_image
    else:
        print("✗ No image to convert.")
        return None

# Main program
image = None

while True:
    choice = display_menu()
    
    if choice == '1':
        image = load_image()
        if image is not None:
            display_image(image, "Original Image")
    
    elif choice == '2':
        if image is not None:
            gray_image = convert_to_grayscale(image)
            if gray_image is not None:
                display_image(gray_image, "Grayscale Image")
                save_path = input("Enter save path (e.g., Image_processing\\Saved_img\\gray_image.jpg): ")
                save_image(gray_image, save_path)
        else:
            print("✗ Please load an image first (Option 1).")
    
    elif choice == '3':
        if image is not None:
            save_path = input("Enter the save location and filename (e.g., Image_processing\\Saved_img\\custom_image.jpg): ")
            save_image(image, save_path)
        else:
            print("✗ Please load an image first (Option 1).")
    
    elif choice == '4':
        image = load_image()
        if image is not None:
            display_image(image, "Original Image")
            save_path = input("Enter the save location and filename (e.g., Image_processing\\Saved_img\\image.jpg): ")
            save_image(image, save_path)
    
    elif choice == '5':
        print("\n✓ Thank you for using Image Processing Program. Goodbye!")
        break
    
    else:
        print("✗ Invalid choice. Please enter a number between 1 and 5.")
    
    