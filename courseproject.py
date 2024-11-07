import serial
import time
import re

import pandas as pd

from datetime import datetime

ser=serial.Serial('COM4',9600,timeout=1)

time.sleep(2)
df=pd.DataFrame(columns=["Datetime","V1","V2"])
try:
    while True:
        if ser.in_waiting>0:
            line=ser.readline().decode('utf-8').strip()
            timestamp=datetime.now()
            v1,v2=re.findall(pattern=r"[-+]?\d*\.\d+|[-+]?\d+",string=line)
            print("v1",v1,"v2",v2)
            new_row= {"Datatime":timestamp,"V1":v1,"V2":v2}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
except KeyboardInterrupt:
    print("Programe interrupted by user.")
finally:
    ser.close()


