import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


cap=cv2.VideoCapture(0)
cap.set(3,1880) #length
cap.set(4,860)  #width
cap.set(10,100) #briteness

while True:
    success,img=cap.read() #success is boolean
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.2,2)
    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
