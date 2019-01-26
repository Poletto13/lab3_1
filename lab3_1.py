import RPi.GPIO as GPIO 
import time

import sys
import spidev

GPIO.setmode(GPIO.BOARD)

##########################################################
# TO-DO 1. For the motor
pin1_motor  = 
pin2_motor  = 

GPIO.setup(pin1_motor, GPIO.OUT)
GPIO.setup(pin2_motor, GPIO.OUT) 

##########################################################
# TO-DO 2. Give a value for the duty_cycle
duty_cycle = 

motor1 = GPIO.PWM(pin1_motor,duty_cycle)
motor2 = GPIO.PWM(pin2_motor,duty_cycle)

motor1.start(0)
motor2.start(0)

# For the ADC
spi = spidev.SpiDev()
spi.open(0,0) 

def buildReadCommand(channel):
  startBit = 0x01
  singleEnded = 0x08 
  
  return [startBit, singleEnded | (channel<<4), 0]

def processAdcValue(result):
  ''' Take in result as array of three bytes. 
	  Return the two lowest bits of the 2nd byte and 
	  all of the third byte'''
	    
  byte2 = (result[1] & 0x03) 
  return (byte2 << 8) | result[2]
  
def readAdc(channel): 
  if ((channel > 7) or (channel < 0)):
    return -1
  r = spi.xfer2(buildReadCommand(channel))
  return processAdcValue(r)

motor2.ChangeDutyCycle(0)
   
try:
  while True:
    ##########################################################
    # TO-DO 3. Specify the channel from which you get the water level
    val = readAdc( )
    print "ADC Result: ", str(val)
    # time.sleep(5)
	
    ##########################################################
    # TO-DO 4. Make the motor speed depend on the water level. 
    motor1.ChangeDutyCycle( )    
    time.sleep(0.02)
    
except KeyboardInterrupt: 
  motor1.stop()	
  motor2.stop()	
  spi.close()
  sys.exit(0)  
  #pass 

motor1.stop()	
motor2.stop()	
spi.close()
sys.exit(0)
