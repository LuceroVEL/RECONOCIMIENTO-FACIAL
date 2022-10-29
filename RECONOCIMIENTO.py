#-------------importar librerias-------
import cv2
import os
import serial, time #para la comunicacion con el arduino

#arduino = serial.Serial("COM4", 19200)
#time.sleep(2)
#-------------importar nombres de las carpetas------
direccion = 'C:/Users/lucer/Desktop/PROGRAMA_TESIS/IMAGENES'

imagePaths = os.listdir(direccion)
print('imagePaths=', imagePaths)

reconocimiento_facial = cv2.face.EigenFaceRecognizer_create()

#leyendo el modelo
reconocimiento_facial.read('modeloEigenfaces.xml')

cap = cv2.VideoCapture('rtsp://admin:Lucero26@192.168.4.104:554/cam/realmonitor?channel=1&subtype=0admin/Lucero26/192.168.4.104:554')  # IP Camera
#cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

while True:
    ret,frame = cap.read()
    if ret == False: break
    gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame =gray.copy()
    faces = faceClassif.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
        result = reconocimiento_facial.predict(rostro)

        cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)

        #EigenFaces
        if result[1] < 6200:
            cv2.putText(frame, '{}'.format(imagePaths[result[0]]), (x, y - 25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)

        else:
            cv2.putText(frame, 'Desconocido'.format(result), (x, y - 20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            #arduino.write(b'D')

    cv2.imshow('frame',frame)
    k = cv2.waitKey(1)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
#arduino.close()
