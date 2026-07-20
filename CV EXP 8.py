import cv2

# Read the image
img = cv2.imread("C:/Users/saimo/OneDrive/Pictures/Saved Pictures/image.png")

# Check if image is loaded
if img is None:
    print("Image not found!")
else:
    # Scale the image to a bigger size (200%)
    bigger = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Scale the image to a smaller size (50%)
    smaller = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # Display the images
    cv2.imshow("Original Image", img)
    cv2.imshow("Bigger Image", bigger)
    cv2.imshow("Smaller Image", smaller)

    # Save the scaled images
    cv2.imwrite("bigger_image.png", bigger)
    cv2.imwrite("smaller_image.png", smaller)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
