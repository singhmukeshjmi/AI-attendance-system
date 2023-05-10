import os
import cv2
import face_recognition


if not os.path.exists('images'):
    os.makedirs('images')
print('folder tak')

id = int(input('ID: '))
name = input('Name: ')

input("\nPress ENTER to start when you're ready, the system will automatically detect and save first 5 frames with your face")

import imutils
import requests
import numpy as np
url = "http://192.168.0.33:8080/shot.jpg"


camera = cv2.VideoCapture(0)
count=0
while True:

    # img_resp = requests.get(url)
    # img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    # img = cv2.imdecode(img_arr, -1)
    # img = imutils.resize(img, width=500, height=500)

    cam,img = camera.read()



    try:
        facelocation = face_recognition.face_locations(img)[0]
        print(facelocation)
        cv2.rectangle(img, (facelocation[3],facelocation[0]), (facelocation[1],facelocation[2]), 2)
        if count<5:
            cv2.imwrite(f'images/{id}_{name}_{count}.jpg',img)
            count=count+1
            print("saved")
        print(facelocation)
    except:
        print("Please ensure your face is in the frame")
    cv2.imshow("Cloud_cam", img)
        


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
