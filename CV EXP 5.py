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

    # Erode the image
    eroded = cv2.erode(img, kernel, iterations=1)

    # Display original and eroded images
    cv2.imshow("Original Image", img)
    cv2.imshow("Eroded Image", eroded)

    # Save the eroded image
    cv2.imwrite("eroded_image.png", eroded)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
