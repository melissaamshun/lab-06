import grovepi
import time
grovepi.set_bus("RPI_1") # set I2C to use the hardware bus

ultrasonic_ranger = 4 # Connect the Grove Ultrasonic Ranger to digital port D4
potentiometer = 0 # Connect the Grove Rotary Angle Sensor to analog port A0
led = 5 # Connect the LED to digital port D5


grovepi.pinMode(potentiometer,"INPUT")
grovepi.pinMode(led,"OUTPUT")
time.sleep(1)
# Reference voltage of ADC is 5v
adc_ref = 5
# Vcc of the grove interface is normally 5v
grove_vcc = 5
# Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
full_angle = 300




#ultrasonic
while True:
    try:
       
        dist=grovepi.ultrasonicRead(ultrasonic_ranger) # Read distance value from Ultrasonic


        time.sleep(0.1) # don't overload the i2c bus

    
        # Read sensor value from potentiometer
        sensor_value = (grovepi.analogRead(potentiometer)/2)

        print("sensor_value = %d voltage = %.2f degrees = %.1f brightness = %d" %(sensor_value, voltage, degrees, brightness))
 

 
        if(dist >= sensor_value):
            setText("%d cm \n%d cm" %(sensor_value,dist))
            setRGB(0,125,0)
        elif(dist < sensor_value):
            setText("%d cm OBJ PRES\n%d cm" %(sensor_value,dist))
            setRGB(125,0,0)   
            
    except IOError:
        print ("Error angle")

