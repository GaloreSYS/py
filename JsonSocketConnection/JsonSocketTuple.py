import time
import sys
import math
import os
from xarm.wrapper import XArmAPI

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
           #sys.exit(1)
        
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
speed = 100
############################################################# Robot communication

################################ Xarm Api system #################################
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
#######################################################

############################################################         
         
         
############################################################## Code type 1

arm.reset(wait=True)  
arm.set_position(292.1,0.5,515.7,-94.7,-88.5,-85.3)
arm.set_position(112.2,433.1,431.8,22.5,-80.3,-125.2)
arm.open_lite6_gripper()
time.sleep(5)
arm.set_position(115,439.3,404.5,1.2,-81.9,-104.6)
time.sleep(5)
arm.close_lite6_gripper()
time.sleep(5)
arm.set_position(77.8,294.3,600.3,16.7,-77.9,-123)



############################################################

    