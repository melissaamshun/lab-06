import grovepi
import time
grovepi.set_bus("RPI_1") # set I2C to use the hardware bus


potentiometer = 0 # Connect the Grove Rotary Angle Sensor to analog port A0
led = 5 # Connect the LED to digital port D5
ultrasonic_ranger = 4 # Connect the Grove Ultrasonic Ranger to digital port D4



#ultrasonic
while True:
    try:
        # Read distance value from Ultrasonic
        print(grovepi.ultrasonicRead(ultrasonic_ranger))

    except Exception as e:
        print ("Error:{}".format(e))
    
    time.sleep(0.1) # don't overload the i2c bus

    

grovepi.pinMode(potentiometer,"INPUT")
grovepi.pinMode(led,"OUTPUT")
time.sleep(1)

# Reference voltage of ADC is 5v
adc_ref = 5

# Vcc of the grove interface is normally 5v
grove_vcc = 5

# Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
full_angle = 300

while True:
    try:
        # Read sensor value from potentiometer
        sensor_value = grovepi.analogRead(potentiometer)

        # Calculate voltage
        voltage = round((float)(sensor_value) * adc_ref / 1023, 2)

        # Calculate rotation in degrees (0 to 300)
        degrees = round((voltage * full_angle) / grove_vcc, 2)

        # Calculate LED brightess (0 to 255) from degrees (0 to 300)
        brightness = int(degrees / full_angle * 255)

        # Give PWM output to LED
        grovepi.analogWrite(led,brightness)

        print("sensor_value = %d voltage = %.2f degrees = %.1f brightness = %d" %(sensor_value, voltage, degrees, brightness))
    except KeyboardInterrupt:
        grovepi.analogWrite(led,0)
        break
    except IOError:
        print ("Error")
        
        
        from grove_rgb_lcd import *

setText("Hello world\nLCD test")
setRGB(0,128,64)

# Slowly change the colors every 0.01 seconds.
for c in range(0,255):
    setRGB(c,255-c,0)
    time.sleep(0.01)

setRGB(0,255,0)
setText("Bye bye, this should wrap")
