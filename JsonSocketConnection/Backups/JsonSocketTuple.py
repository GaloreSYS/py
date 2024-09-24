import json
import time
import sys
import math
import os
from xarm.wrapper import XArmAPI

file = open("Data\\Socket.json", "r")
x = file.read()
finaldata = json.loads(x)

Decider = 0

dict = {
    "ActiveState": "Standby",
	"ProductValue": 0
}
#standby state

def Set_on_standBy():
    StateData = "Standby"
    json_object = json.dumps(dict,  indent=4)
    with open("Data\\Socket.json", "w") as oytfile:
         oytfile.write(json_object)
         
############################################################# Robot communication

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
############################################################         
         
         
############################################################## Code type 1
def codeset1():
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
    print("Product value 1")
############################################################## Code type 2
def codeset2():
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
    print("Product value 2")
############################################################## Code type 3
def codeset3():
    print("Product value 3")
############################################################## Code type 4
def codeset4():
    print("Product value 4")    
##############################################################

StateData =  str(finaldata['ActiveState'])
StateValue = str(finaldata['ProductValue'])
################################################


################################################
if StateData == "Running":
 if StateValue == "0":
     print("Sorry no products")
 if StateValue == "1":
     codeset1()    
 if StateValue == "2":
     codeset2() 
 if StateValue == "3":
     codeset3()     
 if StateValue == "4":
     codeset4()              
 time.sleep(1)
 Set_on_standBy()
  
if StateData == "Standby":
    if StateValue != "0":
        Set_on_standBy()
    print("Procces not running:")


    