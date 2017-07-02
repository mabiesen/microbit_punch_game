import microbit

# Measure total velocity of a punch

# gets the x, y, and z positions
def getAcc():
    x = microbit.accelerometer.get_x()
    y = microbit.accelerometer.get_y()
    z = microbit.accelerometer.get_z()
    return (x,y,z)

# Makes a number positive if negative
def makeAbsolute(input):
    if input < 0:
        input = input * -1
    return input

# 3,2,1
def countDown():
    microbit.display.scroll(str(3))
    microbit.display.scroll(str(2))
    microbit.display.scroll(str(1))

# loops for data over 1 second, collecting 100ms long distances
# gets the largest and displays
def mainFunc():
    distanceList = []
    countDown()
    initialTime = microbit.running_time()
    newTime = initialTime
    time =100 # in milliseconds
    while((newTime - initialTime)< 1000):
        x1,y1,z1 = getAcc()
        microbit.sleep(time)
        x2,y2,z2 = getAcc()
        # next, get the difference
        xdistance = makeAbsolute(x2-x1)
        ydistance = makeAbsolute(y2-y1)
        zdistance = makeAbsolute(z2-z1)
        totaldistance = (xdistance + ydistance + zdistance)/3
        distanceList.append(totaldistance)
        newTime = microbit.running_time()
    distanceList.sort()
    displayDistance(distanceList[-1])
    
# display greatest distance traveled over the course of 100ms   
def displayDistance(totaldistance):
    microbit.sleep(1000)
    microbit.display.scroll("Score:")
    microbit.display.scroll(str(int(totaldistance)))

# loop for button to begin program 
while True:
   if microbit.button_a.was_pressed():
      mainFunc() 
    
