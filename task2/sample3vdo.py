import cv2

#video capture object where 0 is the camera number for a webcam
cam = cv2.VideoCapture(0)

width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH)) #get the width of the frames
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)) #get the height of the
fps = cam.get(cv2.CAP_PROP_FPS) #get the frames per second

output_file = r"C:\Users\EJO\OneDrive\Desktop\opencv\task2\output_video.avi"
output = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'XVID'), 20.0, (width, height))

while True:
    _, frame = cam.read() #reading one frame form the camera
    output.write(frame) #write the current frame to the output file
    cv2.imshow("Webcam", frame) #displaying the current frame
    if cv2.waitKey(1) & 0xff == ord('q'): #if 'q' key is pressed, break the loop
        break
cam.release() #close the camera
output.release() #release the video writer
cv2.destroyAllWindows() #close all OpenCV windows