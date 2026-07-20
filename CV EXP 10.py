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

    # Translation values
    tx = 100   # Move right by 100 pixels
    ty = 50    # Move down by 50 pixels

    # Translation matrix
    M = np.float32([[1, 0, tx],
                    [0, 1, ty]])

    # Apply translation
    moved = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Moved Image", moved)

    # Save the moved image
    cv2.imwrite("moved_image.png", moved)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
