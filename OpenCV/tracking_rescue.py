import cv2
import numpy 
import numpy as np

camera = cv2.VideoCapture(0)
#kernel = numpy.ones((5 ,5), numpy.uint8)

while True:
    _, img = camera.read()

    #img = cv2.resize(img, (200, 400))

    #gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

    lowerPreto = np.array([0, 0, 0])
    upperPreto = np.array([100, 100, 100])

    mascara = cv2.inRange(img, lowerPreto, upperPreto)

    contours, hierarchy = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

   
    if contours:
        #max = cv2.contourArea(contours[0])
       # idArea = 0
        #i = 0

        #for cnt in contours:
         #   if max < cv2.contourArea(cnt):
         #       max = cv2.contourArea(cnt)
          #      idArea = i
          #  i += 1      

        x, y, w, h = cv2.boundingRect(contours[10])
    
        #if max > 100.0 and max < 1000 :
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 3)          


    cv2.imshow("mask", mascara)
    cv2.imshow("detect", img)

    k = cv2.waitKey(100)
    if k == 27:
        break

cv2.destroyAllWindows()
camera.release()
