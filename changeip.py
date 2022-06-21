
import os
import subprocess
import random 
import time
allLocations =['smart','in','nlth','nlam','nlro','hk2','hk1','ukdo','ukel','uklo','usny','usnj3','defr3','denu','defri','ch','itco','cato']

os.system("expressvpn disconnect")
time.sleep(2)


from subprocess import STDOUT, check_output
while(1):
    try:
        location=random.choice(allLocations)
        output = check_output(["expressvpn","connect", str(location)], stderr=STDOUT, timeout=25)
        print("connected to",location)
        break

    except Exception as e:
        print(e)
        print("timeout")
        os.system("expressvpn disconnect")
    
        time.sleep(5)   














