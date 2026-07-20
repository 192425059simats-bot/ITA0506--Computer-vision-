import cv2
import numpy as np

# Read the image
img = cv2.imread("C:/Users/saimo/OneDrive/Pictures/Saved Pictures/image.png")

# Check if image is loaded
if img is None:
    print("Image not found!")
else:
    # Resize the image (optional)
    img = cv2.resize(img, (800, 600))

    # Create a 5x5 kernel
    kernel = np.ones((5, 5), np.uint8)

    # Dilate the image
    dilated = cv2.dilate(img, kernel, iterations=1)

    # Display original and dilated images
    cv2.imshow("Original Image", img)
    cv2.imshow("Dilated Image", dilated)

    # Save the dilated image
    cv2.imwrite("dilated_image.png", dilated)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
