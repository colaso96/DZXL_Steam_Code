import time
import ADS1256
import RPi.GPIO as GPIO


try:
    ADC = ADS1256.ADS1256()
    ADC.ADS1256_init()

    while(1):
        ADC_Value = ADC.ADS1256_GetAll()
        print ("1 ADC = %lf"%(ADC_Value[1]/0x7fffff))
        print ("2 ADC = %lf"%(ADC_Value[2]/0x7fffff))
        print ("3 ADC = %lf"%(ADC_Value[3]/0x7fffff))
        print ("4 ADC = %lf"%(ADC_Value[4]/0x7fffff))
        print ("5 ADC = %lf"%(ADC_Value[5]/0x7fffff))
        print ("6 ADC = %lf"%(ADC_Value[6]/0x7fffff))
        time.sleep(3)
        
except :
    GPIO.cleanup()
    print ("\r\nProgram end     ")
    exit()
