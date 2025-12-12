import cv2

#path of image
path1 = r"C:\Users\EJO\OneDrive\Desktop\opencv\task\messi.jpg"
path2 = r"C:\Users\EJO\OneDrive\Desktop\opencv\task\freedom.png"

#read image
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

print("Image 1 shape:", img1.shape) #print shape of image 1
print("Image 2 shape:", img2.shape) #print shape of image 2

#convert to gray scale
img_gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img_gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#display images
cv2.imshow("OutputMessi", img1)
cv2.imshow("Gray_Output1", img_gray1)
cv2.imshow("OutputFreedom" , img2)
cv2.imshow("Gray_Output2", img_gray2)

print('a pixel at (5,5):', img1[5,5]) #print pixel value at (5,5) of image 1

new_image = img1[:10,:10] #crop a 10x10 pixel image from top-left corner
B = new_image[:,:,0] #blue channel
G = new_image[:,:,1] #green channel
R = new_image[:,:,2] #red channel

print("Blue channel of cropped image:\n", B)
print("Green channel of cropped image:\n", G)
print("Red channel of cropped image:\n", R)

cv2.imshow("Cropped Image", img1[:10,:10]) #display cropped image

img1[:,:] = (0,0,0) #set all pixels to black
cv2.imshow("Black Image", img1) #display black image

#create 4x4 chessboard pattern using img2
height, width = img2.shape[:2]
tile_height = height // 4
tile_width = width // 4

for i in range(4):
    for j in range(4):
        if (i + j) % 2 == 0:
            img2[i*tile_height:(i+1)*tile_height, j*tile_width:(j+1)*tile_width] = (255, 255, 255) #white
        else:
            img2[i*tile_height:(i+1)*tile_height, j*tile_width:(j+1)*tile_width] = (0, 0, 0) #black

cv2.imshow("Chessboard", img2) #display chessboard

#save gray scale image
cv2.imwrite(r"C:\Users\EJO\OneDrive\Desktop\opencv\task\messi_gray.jpg", img_gray1)
cv2.imwrite(r"C:\Users\EJO\OneDrive\Desktop\opencv\task\freedom_gray.png", img_gray2)


#wait for a key press and close windows
cv2.waitKey(0)
#kill all open windows
cv2.destroyAllWindows()

