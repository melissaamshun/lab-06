from grovepi import *
import time
from grove_rgb_lcd import *
grovepi.set_bus("RPI_1") # set I2C to use the hardware bus

ultrasonic_ranger = 4 # Connect the Grove Ultrasonic Ranger to digital port D4
potentiometer = 0 # Connect the Grove Rotary Angle Sensor to analog port A0

grovepi.pinMode(potentiometer,"INPUT")
time.sleep(1)

# Reference voltage of ADC is 5v
adc_ref = 5
# Vcc of the grove interface is normally 5v
grove_vcc = 5
# Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
full_angle = 300

while True:
 try:  
  dist=grovepi.ultrasonicRead(ultrasonic_ranger) # Read distance value from Ultrasonic
  time.sleep(0.1) # don't overload the i2c bus 
 
  sensor_value = (grovepi.analogRead(potentiometer)/2) # Read sensor value from potentiometer and devides by two to fit range of ultrasonic

  if(dist >= sensor_value): #if distance is higher or equal than the threshhold it prints threshhold and the distane (colour of background green)
   setText_norefresh("%d cm          \n%d cm" %(sensor_value,dist))
   setRGB(0,125,0)
  elif(dist < sensor_value):  #if distance is lower than the threshhold prints the threshhold then "OBJ PRES" and the distane (colour of background red)
   setText_norefresh("%d cm OBJ PRES\n%d cm" %(sensor_value,dist))
   setRGB(125,0,0)    
 except IOError:
  print ("Error angle")
