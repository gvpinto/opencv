import cv2

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    # Read frame
    ret, frame = cap.read()
    if not ret:
        break

    # Get the key press and mask it with 0xFF for compatibility
    k = cv2.waitKey(250) & 0xFF

    # Identify if 'ESC' is pressed (ASCII 27)
    if k == 27:
        break
    
    # Identify if 'e' or 'E' is pressed
    if k == ord('e') or k == ord('E'):
        cv2.putText(frame, "E is pressed, press Z or ESC", 
                    (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                    1, (0, 255, 0), 2)
    
    # Identify if 'z' or 'Z' is pressed
    elif k == ord('z') or k == ord('Z'):
        cv2.putText(frame, "Z is pressed",
                    (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                    1, (0, 255, 0), 2)

    cv2.imshow("Image", frame)

cap.release()
cv2.destroyAllWindows()