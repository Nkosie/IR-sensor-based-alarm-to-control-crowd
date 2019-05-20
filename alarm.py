
import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(4,IO.IN)
IO.setup(27,IO.IN)
IO.setup(14,IO.OUT)
counter_1=0;
counter_3=0;
IO.output(14,False)
while 1:
      if (counter_1==0):   
        IO.output(14,False)
        
        
      if (IO.input(4)==False):
         counter_1=counter_1+1
         time.sleep(0.5)
         
         
         
         
      if (IO.input(27)==False):
         counter_3=counter_3+1
         time.sleep(0.5)        
         


         
      if (counter_3==1 and counter_1>1):
         IO.output(14,True)
         time.sleep(15)
         counter_1=0;
         counter_3=0;
GPOI.cleanup()
