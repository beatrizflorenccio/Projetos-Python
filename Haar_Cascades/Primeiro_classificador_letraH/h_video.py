import cv2
import numpy as np
import pkg_resources

dir_xml = pkg_resources.resource_filename("cv2", "data\\cascade.xml")

h_cascade = cv2.CascadeClassifier(dir_xml)
camera = cv2.VideoCapture(0)

while True:

    retval, img = camera.read()

    img = cv2.resize(img, (200, 200))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #gray = cv2.blur(gray, (10, 10))

    objeto = h_cascade.detectMultiScale(gray, 1.3, 10)

    for x, y, w, h in objeto:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
  
    print(len(objeto))

    cv2.imshow("detecta letra", img)

    k = cv2.waitKey(100)

    if k == 27:
        break

camera.release()
cv2.destroyAllWindows()

