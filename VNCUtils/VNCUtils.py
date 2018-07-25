from vncdotool import api
from time import sleep
import os
from PIL import Image
from pytesseract import image_to_string
class vncConnect:
    def __init__(self,vnc_server,passwd):
        self.vnc_server = vnc_server
        self.passwd = passwd

    def getConnection(self):
        try:
            client  = api.connect(self.vnc_server,self.passwd)
            print("Successully established the connection with vnc server.")
        except ValueError as e:
            print("Error While logging in to VNC Server")
        except Exception as e:
            print("Check the VNC Server Details")
        return client

    def execute_command(self,obj,cmd):
        self.cmd = cmd
        for k in self.cmd:
            obj.keyPress(k)
        obj.keyPress('enter')
        obj.captureScreen('screen.png')
        screen = "screen.png"
        start = os.stat(screen)
        obj.captureScreen(screen)
        while os.stat(screen) == start:
            sleep(0.05)
        sleep(0.2)

    def close(self,obj):
        obj.disconnect()

    def extractDatafromImage(self,image_name):
        self.img_name = image_name + ".png"
        print("The Image name is : {}".format(self.img_name))
        #output =  image_to_string(Image.open(self.img_name),lang='')
        output = image_to_string(Image.open(self.img_name), lang='eng', config='-psm 6')
        #output = str(output)
        print(output)
        return output


if __name__ == '__main__':
    obj = vncConnect('Servername','password')
    vnc_instance = obj.getConnection()
    obj.execute_command(vnc_instance,"8f,pprg,view,list")
    obj.close(vnc_instance)
    #print("Completed!!!")
    obj.extractDatafromImage('screen')
