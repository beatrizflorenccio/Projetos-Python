#MaBe
import RPi.GPIO as GPIO
import time

#setando os pinos
GPIO.setmode(GPIO.BOARD)
GPIO.setup(17, OUTPUT) #LED Vermelho
GPIO.setup(27, OUTPUT) #LED Amarelo
GPIO.setup(22, OUTPUT) #LED Verde

while True:


    #Vermelho ligado
    GPIO.output(17, HIGH)
    GPIO.output(27, LOW)
    GPIO.output(22, LOW) 
    time.sleep(t1)

    #Amarelo ligado
    GPIO.output(17, HIGH)
    GPIO.output(27, LOW)
    GPIO.output(22, LOW)
    time.sleep(t2)

    #Verde ligado
    GPIO.output(17, HIGH)
    GPIO.output(27, LOW)
    GPIO.output(22, LOW)
    time.sleep(t3)
