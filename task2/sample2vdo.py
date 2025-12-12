import cv2

#video capture object where 0 is the camera number for a webcam
cam = cv2.VideoCapture(0)

#set camera properties
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) #set the width of the frames
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) #set the height of the frames
cam.set(cv2.CAP_PROP_FPS, 15) #set the frames per second

#get camera properties
width = cam.get(cv2.CAP_PROP_FRAME_WIDTH) #set the width of the frames
height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT) #set the height of the frames
fps = cam.get(cv2.CAP_PROP_FPS) #set the frames per second

#read and display frames in a loop
while True:
    i, frame = cam.read() #reading one frame form the camera
    cv2.imshow("Webcam", frame) #displaying the current frame

    print('resolution:' ,width, 'x', height, '| frames per second:', fps) #print the resolution and fps
    #wait for 1 millisecond for a key press
    if cv2.waitKey(1) & 0xFF == ord('q'): #if 'q' key is pressed, break the loop
        break

cam.release() #close the camera
cv2.destroyAllWindows() #close all OpenCV windows