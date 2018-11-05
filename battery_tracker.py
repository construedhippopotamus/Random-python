# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 11:16:56 2018

@author: Pizzagirl

Track laptop battery power and graph it

"""
import schedule   
import time


def bat_level():
    
    import psutil
    import time
    import csv

    #save battery data
    savefile = r'C:\Users\Pizzagirl\Documents\programming\python\battery.csv'
    
    timelist = []
    batlist = []
    
    battery = psutil.sensors_battery()
    remaining = str(battery[0])
    time = time.time()
    #timelist.append(time)
    #batlist.append(str(battery[0]))
    
    #print battery[0], ", ", time
    
    with open(savefile, 'ab') as f:
    
        #quote minimal suppresses a white line that is otherwise after each row
        writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        writer.writerow([time, remaining])
    return

bat_level()

 
schedule.every(5).minutes.do(bat_level)  

while True:
    schedule.run_pending()
    time.sleep(60)
