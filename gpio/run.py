import RPi.GPIO as GPIO
import time
from . import port
# class Car():
#     def __init__(self):
#         print "car init"
#         self.left=[35,37]
#         self.right=[36,38]
#         port.sethigh(self.left[0])
#         port.sethigh(self.left[1])
#         port.sethigh(self.right[0])
#         port.sethigh(self.right[1])
#     def leftgo(self):
#         port.setlow(self.left[0])
#         port.sethigh(self.left[1])
#     def leftback(self):
#         port.setlow(self.left[1])
#         port.sethigh(self.left[0])        
#     def rightgo(self):
#         port.setlow(self.right[0])
#         port.sethigh(self.right[1])
#     def rightback(self):
#         port.setlow(self.right[1])
#         port.sethigh(self.right[0])  
#     def stopleft(self):
#         port.sethigh(self.left[0])
#         port.sethigh(self.left[1])   
#     def stopright(self):
#         port.sethigh(self.right[0])
#         port.sethigh(self.right[1])            
#     def stop(self):
#         port.sethigh(self.left[0])
#         port.sethigh(self.left[1])
#         port.sethigh(self.right[0])
#         port.sethigh(self.right[1])        
#     def run(self):
#         self.leftgo()
#         self.rightgo()

class Car():
    def __init__(self):
        print "car init"
        self.DEVIleft = 0  #deviation
        self.DEVIright = 0  #deviation
        self.left=[35,37]
        self.right=[36,38]
        try:
            GPIO.setmode(GPIO.BOARD)
        except Exception,e:
            print e
        for item in self.left+self.right:
            try:
                GPIO.setup(item,GPIO.OUT)
            except Exception,e:
                print "%d error:%s" % (item,e)        
        self.left1 = GPIO.PWM(self.left[0],500)
        self.left2 = GPIO.PWM(self.left[1],500) 
        self.right1 = GPIO.PWM(self.right[0],500)
        self.right2 = GPIO.PWM(self.right[1],500)         
        self.left1.ChangeDutyCycle(100)
        self.left2.ChangeDutyCycle(100)    
        self.right1.ChangeDutyCycle(100)
        self.right2.ChangeDutyCycle(100)          
    def go(self,devleft = None,devright = None):
        # self.left1.ChangeDutyCycle(devleft)
        # self.right1.ChangeDutyCycle(devright)
        # self.left2.ChangeDutyCycle(100)  
        # self.right2.ChangeDutyCycle(100) 
        devleft = self.DEVIleft if not devleft else int(devleft)
        devright = self.DEVIright if not devright else int(devright)
        self.rightgo(devright)
        self.leftgo(devleft)
    def stop(self):
        self.leftstop()
        self.rightstop()
    def back(self,devleft = None,devright = None):
        devleft = self.DEVIleft if not devleft else int(devleft)
        devright = self.DEVIright if not devright else int(devright)        
        self.leftback(devleft)
        self.rightback(devright)

    def leftgo(self,dev = None):
        dev = self.DEVIleft if not dev else int(dev)
        self.left1.ChangeDutyCycle(dev)
        self.left2.ChangeDutyCycle(100)  
    def leftback(self,dev = None):
        dev = self.DEVIleft if not dev else int(dev)
        self.left1.ChangeDutyCycle(100)                      
        self.left2.ChangeDutyCycle(dev)
    def leftstop(self):
        self.left1.ChangeDutyCycle(100)                      
        self.left2.ChangeDutyCycle(100)      
    def rightgo(self,dev = None):
        dev = self.DEVIright if not dev else int(dev)       
        self.right1.ChangeDutyCycle(dev)
        self.left2.ChangeDutyCycle(100) 
    def rightback(self,dev = None):
        dev = self.DEVIright if not dev else int(dev)            
        self.right1.ChangeDutyCycle(100)
        self.right2.ChangeDutyCycle(dev)
    def rightstop(self):
        self.right1.ChangeDutyCycle(100)                      
        self.right2.ChangeDutyCycle(100)                 
