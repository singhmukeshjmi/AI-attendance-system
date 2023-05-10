# https://face-recognition.readthedocs.io/en/latest/_modules/face_recognition/api.html#face_distance
import os
import cv2
import numpy as np
import face_recognition
import imutils
import requests
url = "http://192.168.0.33:8080/shot.jpg"

print('imported')


encode_list = []
dict = {}
for file in os.listdir('images'):
    # print(file.split('.')[0].split('_')[0])
    image = face_recognition.load_image_file(f'images/{file}')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imshow('image', image)
    encode = face_recognition.face_encodings(image)
    encode_list.append(encode)
    dict[file] = encode
print(len(encode_list))
print(len(dict))



camera = cv2.VideoCapture(0)

while(True):
    # img_resp = requests.get(url)
    # img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    # img = cv2.imdecode(img_arr, -1)
    # frame = imutils.resize(img, width=1000, height=1800)



    cam,frame = camera.read()

    try:
        facelocation = face_recognition.face_locations(frame)[0]
        cv2.rectangle(frame, (facelocation[3],facelocation[0]), (facelocation[1],facelocation[2]), 2)
        encodeframe = face_recognition.face_encodings(frame)[0]
        # distances = []
        # for i in range(10):
        #     currcompare = face_recognition.compare_faces([encode_list[i][0]],encodeframe, tolerance=0.3)
        #     currdist = face_recognition.face_distance([encode_list[i][0]],encodeframe)
        #     print(currcompare, end='')
        #     print(currdist, end='')
        #     distances.append(currdist)
        #     minindex = distances.index(min(distances[0]))




        for key in dict:
            currcompare = face_recognition.compare_faces([dict[key][0]],encodeframe, tolerance=0.3)
            currdist = face_recognition.face_distance([dict[key][0]],encodeframe)
            print(key, end='')
            print(currcompare, end='')
            print(currdist, end='')
            if currcompare[0]==True:
                punch = requests.get(f'http://127.0.0.1:8000/attendpost/?personid={key.split(".")[0].split("_")[0]}')
        print()
    except:
        print('')
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
camera.release()
cv2.destroyAllWindows()