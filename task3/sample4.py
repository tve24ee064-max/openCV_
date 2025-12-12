import cv2
import numpy as np

line = np.zeros((300, 300, 3), dtype=np.uint8) #create a black image
arrow = line.copy() #copy the black image for arrow drawing
polyLine = line.copy() #copy the black image for polyline drawing
rectangle = line.copy() #copy the black image for rectangle drawing
circle = line.copy() #copy the black image for circle drawing
text = line.copy() #copy the black image for text drawing

p1 = [100,100]
p2 = [200,200]
p3 = [200,100]
p4 = [100,200]
points = np.array([p1, p2, p3, p4])

cv2.line(line,p1,p2,(0,255,0),2) #draw a blue line
cv2.arrowedLine(arrow,p1,p2,(0,255,0),2)
cv2.polylines(polyLine,[points],False,color=(0,255,0),thickness=2) #draw a green polyline
cv2.rectangle(rectangle,p1,p2,(0,255,0),2) #draw a green rectangle
cv2.circle(circle,(150,150),50,(0,255,0),2) #draw a green circle
cv2.putText(text,'OpenCV',p4,cv2.FONT_ITALIC,1,(0,255,0),2) #put green text

cv2.imshow("Line", line)
cv2.imshow("Arrowed Line", arrow)
cv2.imshow("PolyLine", polyLine)
cv2.imshow("Rectangle", rectangle)
cv2.imshow("Circle", circle)
cv2.imshow("Text", text)

cv2.waitKey(0)
cv2.destroyAllWindows()