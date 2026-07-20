import cv2

# Read the image
img = cv2.imread("C:/Users/saimo/OneDrive/Pictures/Saved Pictures/image.png")

if img is None:
    print("Image not found!")
else:
    # Resize the image
    img = cv2.resize(img, (800, 600))

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Grayscale Image", gray)

    # Save grayscale image
    cv2.imwrite("gray_image.png", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
