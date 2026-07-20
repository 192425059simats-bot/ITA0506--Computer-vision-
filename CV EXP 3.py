import cv2

# Read the image
img = cv2.imread("C:/Users/saimo/OneDrive/Pictures/Saved Pictures/image.png")

# Check if image is loaded
if img is None:
    print("Image not found!")
else:
    # Resize the image (optional)
    img = cv2.resize(img, (800, 600))

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray, 100, 200)

    # Display original and edge-detected images
    cv2.imshow("Original Image", img)
    cv2.imshow("Canny Edge Detection", edges)

    # Save the edge-detected image
    cv2.imwrite("canny_edges.png", edges)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
