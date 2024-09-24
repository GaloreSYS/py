import json
import time
from tkinter import *

file = open("Data\\Socket.json", "r")
x = file.read()
finaldata = json.loads(x)

dict = {
    "ActiveState": "Standby",
	"ProductValue": 0
}
################################################################
#standby state

def Set_on_standBy():
    StateData = "Standby"
    json_object = json.dumps(dict,  indent=4)
    with open("Data\\Socket.json", "w") as oytfile:
         oytfile.write(json_object)

################################################################

StateData =  str(finaldata['ActiveState'])
StateValue = str(finaldata['ProductValue'])

if StateData == "Running":
    time.sleep(5)
    Set_on_standBy()
  
if StateData == "Standby":
    print("Procces not running:")
    