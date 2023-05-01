from blinkpy.blinkpy import Blink
from tkinter import *
from blinkpy.api import *
import tkinter

# Change 'NAME OF SYNC DEVICE' and 'NAME OF CAMERA' with your camera and sync devices, respectively.


# Initialize our instances, Blink, tkinter, etc.
blink = Blink()
blink.start()
screen = tkinter.Tk()


# Placeholder, meant to print camera names and stuff.
for name, camera in blink.cameras.items():
  print(name + ' loaded.')       
  camerastats = camera.attributes     
  camerabattery = camera.battery   
 # print(camera.attributes)      



# Arms the camera by enabling motion alerts.
# Note: You can disable motion controls for individual cameras.
def armCamera():
    blink.sync["NAME OF SYNC DEVICE"].arm = True
    blink.refresh()

# Disarms the camera by disabling motion alerts.
# Note: You can disable motion controls for individual cameras.
def disarmCamera():
    blink.sync["NAME OF SYNC DEVICE"].arm = False
    blink.refresh()
    
# Prints diagnostics in the console.
def printDiag():    
    camera = blink.cameras["NAME OF CAMERA"]
    print(camera.get_sensor_info())
  

# Initalize all UI elements here.
top.title("Blinkpy Camera Control")

# Pack all UI elements here.
screen.configure(bg='white') # Change to any color you want, for this example it's white.
screen.mainloop()

