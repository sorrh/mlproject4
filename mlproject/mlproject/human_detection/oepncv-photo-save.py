# pip install opencv-contrib-python 터미널에서 설치

import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#사진에서 얼굴 추출 함수(faces 파일에 저장)
def face_extractor(img):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces ==():
        return None

    for(x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face

#카메라 자동실행 및 캡쳐진행
cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if face_extractor(frame) is not None:  #얼굴이 추출됐을 경우
        count+=1
        face = cv2.resize(face_extractor(frame),(200,200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        file_name_path = 'faces/user'+str(count)+'.jpg'
        cv2.imwrite(file_name_path,face)

        cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        cv2.imshow('Face Cropper',face)
    else:  #얼굴이 추출되지 않았을 경우
        print("Face not Found")
        pass
        
        #사진 100장 촬영 후 종료
    if cv2.waitKey(1)==13 or count==100:
        break

cap.release()
cv2.destroyAllWindows()
print('Colleting Samples Complete!!!')
