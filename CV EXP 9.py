import cv2

# Read the image
img = cv2.imread("C:/Users/saimo/OneDrive/Pictures/Saved Pictures/image.png")

# Check if image is loaded
if img is None:
    print("Image not found!")
else:
    # Resize the image (optional)
    img = cv2.resize(img, (800, 600))

    # Rotate the image 90° clockwise
    clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Rotate the image 90° counterclockwise
    counter_clockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Display the images
    cv2.imshow("Original Image", img)
    cv2.imshow("Clockwise Rotation", clockwise)
    cv2.imshow("Counter Clockwise Rotation", counter_clockwise)

    # Save the rotated images
    cv2.imwrite("clockwise_rotation.png", clockwise)
    cv2.imwrite("counter_clockwise_rotation.png", counter_clockwise)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
