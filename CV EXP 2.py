import cv2

# Read the image
img = cv2.imread("C:/Users/saimo/OneDrive/Pictures/Saved Pictures/image.png")

# Check if image is loaded
if img is None:
    print("Image not found!")
else:
    # Resize the image (optional)
    img = cv2.resize(img, (800, 600))

    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(img, (15, 15), 0)

    # Display original and blurred images
    cv2.imshow("Original Image", img)
    cv2.imshow("Gaussian Blurred Image", blurred)

    # Save the blurred image
    cv2.imwrite("gaussian_blur_image.png", blurred)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
