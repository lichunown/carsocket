import RPi.GPIO as GPIO
import time

ports=[7,11,12,13,15,16,18,22,29,31,32,33,35,36,37,38,40]

def init():
    GPIO.setmode(GPIO.BOARD)
    for item in ports:
        try:
            GPIO.setup(item,GPIO.OUT)
        except Exception,e:
            print "%d error:%s" % (item,e)

def sethigh(port):
    try:
        GPIO.output(port,GPIO.HIGH)
    except Exception,e:
        return e
    return "ok"

def setlow(port):
    try:
        GPIO.output(port,GPIO.LOW)
    except Exception,e:
        return e
    return "ok"

def changestat(port):
    try:
        if GPIO.input(port):
            GPIO.output(port,GPIO.LOW)
        else:
            GPIO.output(port,GPIO.HIGH) 
    except Exception,e:
        return e
    return "ok"

def getstatus():
    data=[]
    for item in ports:
        try:
            if GPIO.input(item):
                data.append(item)
        except Exception,e:
            pass
    return data