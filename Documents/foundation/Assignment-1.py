import time
import random
import keyboard



def getAcc(gear):
    if(gear ==1):
        return(random.randrange(6,8))
    if(gear ==2):
        return(random.randrange(4,6))
    if(gear ==3):
        return(random.randrange(6,8))
    if(gear ==4):
        return(random.randrange(3, 4))
    if(gear ==5):
        return(random.randrange(1, 3))

def getDistance(speed, time):
    global elapsed
    global avgSpeed
    global distance
    
    elapsed += time
    avgSpeed = (avgSpeed + speed)/2
    distance += avgSpeed * (elapsed/3600)
    return(int(distance))


def getTopSpeed(gear):
    if(gear == 1):
        return(36)
    if(gear == 2):
        return(80)
    if(gear == 3):
        return(120)
    if(gear == 4):
        return(156)
    if(gear == 5):
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
            distance = getDistance(speed,updateSpeedometer())
            if(speed > getTopSpeed(gear)):
                print(f"{space} {speed}            Change gear    [Trip:{distance} Km ]")
                if keyboard.is_pressed("c"):
                    gear += 1               
            else:
                print(f"{space} {speed}             Gear:{gear} [Trip:{distance} Km ]" )
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

elapsed = 0
avgSpeed = 0
distance = 0
space = "-------------------->"
ignition()
