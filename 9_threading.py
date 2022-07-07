# Threading runs multiple code at a time
from time import *                      #imports everything from library time including sub libraries
from threading import Thread            #imports sub-library Thread from library threading

def myBox():
    while True:
        print('..........My box is open')
        sleep(2)                                #sleeps for 1 second
        print('..........My box is closed')
        sleep(2)

def myLED():
    while True:
        print('My LED is On')
        sleep(1)
        print('My LED is Off')
        sleep(1)

boxThread=Thread(targetBox=myBox)
LEDThread=Thread(target=myLED)
boxThread.daemon=True
LEDThread.daemon=True

boxThread.start()
LEDThread.start()

while True:
    pass
