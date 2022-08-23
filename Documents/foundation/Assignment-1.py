import time
import random
import keyboard


def getAcc(g):
    if(g ==1):
        return(random.randrange(6,8))
    if(g ==2):
        return(random.randrange(4,6))
    if(g ==3):
        return(random.randrange(6,8))
    if(g ==4):
        return(random.randrange(3, 4))
    if(g ==5):
        return(random.randrange(1, 3))



def getTopSpeed(g):
    if(g == 1):
        return(36)
    if(g == 2):
        return(80)
    if(g == 3):
        return(120)
    if(g == 4):
        return(156)
    if(g == 5):
        return(181)


def updateSpeedometer():
    return(random.uniform(0.2,0.5))

def isAccelerating():
    if keyboard.is_pressed("w"):
        return True
    else:
        return False
    
def move():
    
    speed = 0  
    gear = 1 
    while True:
        
        while (isAccelerating()):
            if(speed > getTopSpeed(gear)):
                print(f"{space} {speed}            Change gear")
                if keyboard.is_pressed("c"):
                    gear += 1               
            else:
                print(f"{space} {speed}             Gear:{gear}" )
                speed += getAcc(gear)
            time.sleep(updateSpeedometer())
        
        while not (isAccelerating()):
            print(space, speed)
            if(speed>=0):
                speed -= getAcc(gear)
            if(speed<0):
                speed=0             
            time.sleep(updateSpeedometer())   
     

    
def accelerate():
    print("Tingggg set to First gear", end="\n")
    keyboard.wait("w")
    move()
    

def ignition():
    print("Start Car (s)")
    keyboard.wait("s")
    print("Ghrrrrrrrrrrrrrr..... Ghrrrrrrrrr.....",end="\n")
    accelerate();


space = "-------------------->"
ignition()
 