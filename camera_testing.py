import cv2
cap = cv2.VideoCapture(0)
if not (cap.isOpened()):
    print("Could not open video device")
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
while(True):
    ret, frame = cap.read()
    cv2.imshow('preview',frame)
    key = cv2.waitKey(1)
    if key == ord('z'):
        cv2.imwrite(filename='saved_img.jpg', img=frame)
        cap.release()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
