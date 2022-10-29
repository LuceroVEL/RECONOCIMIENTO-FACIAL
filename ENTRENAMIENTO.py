#-------------importar librerias-------
import cv2
import os
import numpy as np
import time

inicio = time.time()

direccion = 'C:/Users/lucer/Desktop/PROGRAMA_TESIS/IMAGENES'#ruta donde se ha almacenado la Data
peopleList = os.listdir(direccion)
print('Lista de personas: ', peopleList)
labels = []
facesData = []
label = 0
for nameDir in peopleList:
    personPath = direccion + '/' + nameDir
    print('Leyendo las imágenes')
    for fileName in os.listdir(personPath):
        print('Rostros: ', nameDir + '/' + fileName)
        labels.append(label)
        facesData.append(cv2.imread(personPath+'/'+fileName,0)) #imagenes en escala de grises
        imagenes = cv2.imread(personPath+'/'+fileName,0)  #muestra la imagen en escala de grises en pantalla
        #cv2.imshow('imagenes',imagenes)
        #cv2.waitKey(10) #velocidad de muestra
    label = label + 1

print('labels= ',labels)
print('Número de etiquetas 0: ',np.count_nonzero(np.array(labels)==0)) #contar numero de etiquetas 0
print('Número de etiquetas 1: ',np.count_nonzero(np.array(labels)==1)) #contar numero de etiquetas 1
print('Número de etiquetas 2: ',np.count_nonzero(np.array(labels)==2)) #contar numero de etiquetas 2
print('Número de etiquetas 3: ',np.count_nonzero(np.array(labels)==3)) #contar numero de etiquetas 3
# Métodos para entrenar el reconocedor
reconocimiento_facial = cv2.face.EigenFaceRecognizer_create()
#print(face_recognizer) # ver matriz de la imagen

#Entrenando el reconocedor de rostros
print("Entrenando...")
reconocimiento_facial.train(facesData, np.array(labels))
#print(np.array(facesData).shape) #numero de imagenes y dimensiones
#Alacenando el modelo obtenido
reconocimiento_facial.write('modeloEigenfaces.xml')
print("Modelo Eigenfaces Entrenado")
#------------------------------------------------
fin = time.time()
tiempo = fin - inicio
print('Tiempo de Ejecucion es:', tiempo)