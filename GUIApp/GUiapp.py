from tkinter import *
import os
import sys
import time
import math
from xarm.wrapper import XArmAPI
from PIL import Image
######### Ui controllers #########
root = Tk()
root.title("COLA MACHINE")
#root.geometry("800x600")
root.attributes('-fullscreen',True)
################################ Xarm Api system #################################
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
#######################################################
"""
Just for test example
"""
if len(sys.argv) >= 2:
    ip = sys.argv[1]
else:
    try:
        from configparser import ConfigParser
        parser = ConfigParser()
        parser.read('robot.conf')
        ip = parser.get('xArm', 'ip')
    except:
        #ip = input('Please input the xArm ip address:')
        ip = "192.168.1.111"
        if not ip:
            print('input error, exit')
            sys.exit(1)
        
arm = XArmAPI(ip, is_radian=True)
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)
arm.reset(wait=True)
looptime = 2

arm = XArmAPI(ip)
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)

arm.reset(wait=True)
speed = 150
########################################################


def call_forFirstProduct():
    arm.reset(wait=True)  
    arm.set_position(227.5,0.3,469.9,179.8,-0.6,-5.8)
    arm.set_position(-15.5,233,469.2,178.8,-4.1,88.6)
    arm.set_position(-20.5,290.6,528.5,178.4,-87.3,94.9)
    arm.open_lite6_gripper()
    time.sleep(8)
    arm.set_position(6.2,437.6,204.6,-161.8,-87,72.1)
    arm.set_position(7.3,437.1,176.8,-101,-84.8,9.5)
    arm.close_lite6_gripper()
    time.sleep(8)
    arm.set_position(1.8,391.5,469.4,-103.6,-84.1,12.3)
    arm.set_position(389.7,1.4,472.9,-66,-87.3,-114.2)
    arm.set_position(269.5,3.7,204.8,150.7,-87.3,31.9)
    arm.set_position(413.3,0.9,184.7,-2.8,-87.4,-177.9)
    time.sleep(8)
    arm.open_lite6_gripper()
    arm.set_position(390.1,1.6,220.5,83.5,-88.1,96.7)
    arm.close_lite6_gripper()
    arm.reset(wait= True)
    arm.stop_lite6_gripper()
    
    
    
    
def call_forSecondProduct():
    arm.reset(wait=True)  
    arm.set_position(227.5,0.3,469.9,179.8,-0.6,-5.8)
    arm.set_position(-15.5,233,469.2,178.8,-4.1,88.6)
    arm.set_position(-20.5,290.6,528.5,178.4,-87.3,94.9)
    arm.open_lite6_gripper()
    time.sleep(8)
    arm.set_position(93.3,437.6,182.5,179.1,-85.5,87.5)
    arm.set_position(92,437.4,159.9,177.1,-84,88.4)
    arm.close_lite6_gripper()
    time.sleep(8)
    arm.set_position(87.4,396.6,462.3,-80,-79.7,-22.3)
    arm.set_position(389.7,1.4,472.9,-66,-87.3,-114.2)
    arm.set_position(269.5,3.7,204.8,150.7,-87.3,31.9)
    arm.set_position(410.2,1.9,162,-160.7,-85.9,-19)
    time.sleep(8)
    arm.open_lite6_gripper()
    arm.set_position(390.1,1.6,220.5,83.5,-88.1,96.7)
    arm.close_lite6_gripper()
    arm.reset(wait= True)
    arm.stop_lite6_gripper()
    
    

    
    
def call_forThirdProduct():
    arm.reset(wait=True)  
    arm.set_position(227.5,0.3,469.9,179.8,-0.6,-5.8)
    arm.set_position(-15.5,233,469.2,178.8,-4.1,88.6)
    arm.set_position(-20.5,290.6,528.5,178.4,-87.3,94.9)
    arm.open_lite6_gripper()
    time.sleep(8)
    arm.set_position(163.4,440.8,183,-67.3,-85.9,-44.7)
    arm.set_position(161.5,443.6,159.3,-127.8,-85.7,15)
    arm.close_lite6_gripper()
    time.sleep(8)
    arm.set_position(131.7,387.9,425.4,42.2,-88.5,-152.8)
    arm.set_position(389.7,1.4,472.9,-66,-87.3,-114.2)
    arm.set_position(269.5,3.7,204.8,150.7,-87.3,31.9)
    arm.set_position(410.2,1.9,162,-160.7,-85.9,-19)
    time.sleep(8)
    arm.open_lite6_gripper()
    arm.set_position(390.1,1.6,220.5,83.5,-88.1,96.7)
    arm.close_lite6_gripper()
    arm.reset(wait= True)
    arm.stop_lite6_gripper()
    
    
def Call_resetRobot():
    arm.reset(wait= True)
    
    
    

################################### Inside Xarm Api Robot Commands ################################
theLable = Button(text = "Serve a Coke", font=("Arial", 18), bg = "red", command = call_forFirstProduct, height= 5, width= 15)
theLableone = Button(text = "Serve a Sprite",font=("Arial", 18), bg = "green", command = call_forSecondProduct, height= 5, width= 15)
theLabletwo = Button(text = "Serve a Fanta",font=("Arial", 18), bg = "yellow", command = call_forThirdProduct, height= 5, width= 15)
Resetbutton = Button(text = "Reset Arm", font=("Arial", 18), bg="blue",command= Call_resetRobot, height= 5, width= 15)
####################### griding ###########



#########################################
theLable.pack(pady= 20, anchor= CENTER)
theLableone.pack(pady= 20, anchor= CENTER)
theLabletwo.pack(pady= 20, anchor= CENTER)
Resetbutton.pack(pady= 15, anchor= NE)
root.mainloop()


