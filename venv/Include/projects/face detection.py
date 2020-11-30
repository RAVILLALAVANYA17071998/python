import cv2

cap = cv2.Videocapture(r'C:\Users\ravillalavanya\Downloads\vtest.avi')
#videos are just a squences of images
#so,we will add while loop to capture the frame continuously

facecascade = cv2.cascadeclassifier(r"C:\Users\ravillalavanya\Downloads\haarcascade_fullbody.xml")

while True:
    success, frame = cap.read() #frame variable will capture the video & success variable will tell us whether it was captured success are not

    imgGray = cv2.cvtcolor(frame, cv2.COLOR_BGR2GRAY)

    faces = facecascade.detectMultiscale(imgGray,1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow("video", frame)

    if cv2.waitkey(1) == ord('q'): #This adds a Delay and looks for the Key press inorder to break the loop
        break

cap.release() #Release the resources after recording
cv2.destroyAllWindows()
