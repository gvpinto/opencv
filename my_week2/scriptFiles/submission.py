import cv2
import math

# Lists to store the points
point1=(0,0)
point2=(0,0)

# source = cv2.imread("./data/images/sample.jpg", cv2.IMREAD_COLOR)
source = cv2.imread("sample.jpg", cv2.IMREAD_COLOR)
# Make a dummy image, will be useful to clear the drawing
dummy = source.copy()

def drawRectangle(action, x, y, flags, userdata):
  
    # Referencing global variables 
    global point1, point2
    # Action to be taken when left mouse button is pressed

    if action==cv2.EVENT_LBUTTONDOWN:
        point1=(x,y)

    # Action to be taken when left mouse button is released
    elif action==cv2.EVENT_LBUTTONUP:
        circumference=[(x,y)]
        # Calculate radius of the circle
        point2=(x,y)
        # Draw the circle
        cv2.rectangle(source, point1, point2, (0,255,0),2, cv2.LINE_AA)

        # Calculate width and height to crop the image
        width = point2[0] - point1[0]
        height = point2[1] - point1[1]
        
        # Print the x, y and size of the cropped image
        # print(f"Top-left: {point1}, Width: {width}, Height: {height}")

        imageRoi = source[point1[1]:point1[1]+height, point1[0]:point1[0]+width]
        # cv2.imshow("Cropped Image", roi)
        cv2.imwrite("cropped_image.jpg", imageRoi, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        cv2.imshow("Window",source)


# Positioning and style for the text
text = "Choose top-left point and drag, Press ESC to exit and c to clear"
position = (10, 15) # Starting (X, Y)
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 0.4
color = (255, 255, 255)
thickness = 2

# Creating a named window
cv2.namedWindow("Window")

# highgui function called when mouse events occur
cv2.setMouseCallback("Window", drawRectangle)

k = 0

# loop until escape character is pressed
while k != 27 : # 27 is the ASCII code for ESC
    cv2.imshow("Window", source)
    cv2.putText(source, text, position, font, scale, color, thickness)

    k = cv2.waitKey(20) & 0xFF
    # Another way of cloning
    if k == ord('c'): # 99 is the ASCII code for 'c'
        source= dummy.copy()


cv2.destroyAllWindows()

