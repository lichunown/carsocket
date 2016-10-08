import socket,json
import threading
from .gpio import run

host = ""
port = 8000

car = run.Car()

def getsocket():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((host,port))
    s.listen(10)
    return s

def run(skt):
    sock,addr = skt.accept()
    while True:
        try:
            data = sock.recv(1024)
        except Exception,e:
            print e
            sock.close()
            break
        data = data.split()
        print data
        if data[0]=="car":
            if data[1]=="go":
                car.go()
            elif data[1]=="stop":
                car.stop()
            elif data[1]=="back":
                car.back()
            elif data[1]=="leftback":
                car.leftback()
            elif data[1]=="leftgo":
                car.leftgo()
            elif data[1]=="leftstop":
                car.leftstop()
            elif data[1]=="rightgo":
                car.rightgo()
            elif data[1]=="rightstop":
                car.rightstop()
            elif data[1]=="rightback":
                car.rightback()
            else:
                print "no cmd: %s" % data[1]


if __name__=="__main__":
    print "run server:"
    run(getsocket())