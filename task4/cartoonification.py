import cv2
import numpy as np

# Read image
img_path1 = r"C:\Users\EJO\OneDrive\Desktop\opencv\task\messi.jpg"
img_path2 = r"C:\Users\EJO\OneDrive\Desktop\opencv\task\freedom.png"

img1 = cv2.imread(img_path1)
img2 = cv2.imread(img_path2)

# Step 1: Apply bilateral filter to smooth colors while keeping edges sharp
color1 = cv2.bilateralFilter(img1, 9, 300, 300)
color2 = cv2.bilateralFilter(img2, 9, 300, 300)

# Step 2: Convert to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  

# Step 3: Apply median blur to reduce noise
gray_blur1 = cv2.medianBlur(gray1, 5)
gray_blur2 = cv2.medianBlur(gray2, 5)

# Step 4: Detect edges using adaptive threshold
edges1 = cv2.adaptiveThreshold(gray_blur1, 255, 
                              cv2.ADAPTIVE_THRESH_MEAN_C, 
                              cv2.THRESH_BINARY, 9, 5)

edges2 = cv2.adaptiveThreshold(gray_blur2, 255, 
                              cv2.ADAPTIVE_THRESH_MEAN_C, 
                              cv2.THRESH_BINARY, 9, 5)

# Step 5: Combine edges with color image to create cartoon effect
cartoon1 = cv2.bitwise_and(color1, color1, mask=edges1)
cartoon2 = cv2.bitwise_and(color2, color2, mask=edges2)

# Display images
cv2.imshow("Original", img1)
cv2.imshow("Cartoon", cartoon1)
cv2.imshow("Original2", img2)
cv2.imshow("Cartoon2", cartoon2)

# Save cartoon image
cv2.imwrite(r"C:\Users\EJO\OneDrive\Desktop\opencv\task5\cartoon_output1.jpg", cartoon1)
cv2.imwrite(r"C:\Users\EJO\OneDrive\Desktop\opencv\task5\cartoon_output2.jpg", cartoon2)

cv2.waitKey(0)
cv2.destroyAllWindows()
