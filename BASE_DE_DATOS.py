#-------------importar librerias-------
import cv2  #libreria opencv
import os   #
import imutils  #
import matplotlib.pyplot as plt

Nombredelapersona = 'Lucero' #nombre de la persona a entrenar
direccion = 'C:/Users/lucer/Desktop/PROGRAMA_TESIS/IMAGENES'  # ruta donde se ha almacenado la Data
personPath = direccion + '/' + Nombredelapersona
if not os.path.exists(personPath): #si no existe la capeta se crea una
    print('Carpeta creada: ', personPath)
    os.makedirs(personPath)

#cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


cap = cv2.VideoCapture('rtsp://admin:Lucero26@192.168.4.109:554/cam/realmonitor?channel=1&subtype=0admin/Lucero26/192.168.4.109:554')  # IP Camera


deteccionrostro = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  #detector de rostro haar cascade
count = 0
while True:
    ret, frame = cap.read() #para ver cada fotograma de que capture
    if ret == False: break
    frame = imutils.resize(frame, width=640) #se redimensiona si el tamaño es muy grande
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #conversion a escala de grises
    auxFrame = frame.copy()
    faces = deteccionrostro.detectMultiScale(gray, 1.3, 5) #parametros (imagen,reduccion de la imagen,minimo de rectagulos en detecccion de rostro
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) #color verde
        rostro = auxFrame[y:y + h, x:x + w] #dimesiones de la imagen
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC) # redimensiona a 150*150 y crea un cubo
        cv2.imwrite(personPath + '/rostro_{}.jpg'.format(count), rostro) #cada imagen extraida ira con nombre de rostro y el numero correspondiente
        count = count + 1  #contardor 1 a 1
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k == 27 or count >= 20:  #k27 para que el scape pare la entraxion de datos
        #plt.imshow(rostro)
        #plt.show()
        break
        #plt.imshow(rostro[:, :, ::-1])  # muestra el rostro 150*150 a color
#plt.imshow(auxFrame)
#print(gray) # ver matriz de la imagen
cap.release()
cv2.destroyAllWindows()