#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:47:36 2019

@author: Al_gou
"""

import psutil
import time
import os
import signal

def getPrcs():
    # Get all PIDS and select out python processes.
    
    
    all_pids = psutil.pids()
    prcs = {}
    for p in all_pids:
        prcs[p] = psutil.Process(p).name()
    pyprc = []
    for k, v in prcs.items():  
        if v == 'python3.6':
            pyprc.append(k)
    return pyprc


def startPrc():
    # Start the spider and print the process PID
    
    import subprocess as sub
    
    prc = sub.Popen('scrapy crawl chr',
                cwd='/Users/Al_gou/Desktop/ChineseChr/', 
                shell=True)
    print('Process PID: {}\nSpider crawling...\n'.format(prc.pid))

    
def killPrc(pre, aft):
    # Kill newly started processes by compare the  processes sets at two times
    
    
    for prc in aft:
        if prc not in pre:
            os.kill(int(prc), signal.SIGKILL)
            
def checkChr():
    # Check if new files are being scraped and downloaded to the distination 
    # folder and return values accordingly
    # Time interval is 2 minutes
    
    b_len = len(os.listdir('/Users/Al_gou/Desktop/Scraped/Pics/'))
    time.sleep(120)
    a_len = len(os.listdir('/Users/Al_gou/Desktop/Scraped/Pics/'))

    if a_len == b_len:
        return False
    else:
        return True
    
def monitorChr():
    
    # Monitor the spider. When finding it adding no more files to folder, 
    # kill the process and restart a new one.
        
    with open('/Users/Al_gou/Desktop/Scraped/ChineseChar 3.5K.txt', 'r') as f:
        data = f.read()

    while data != '':
        pre = getPrcs()  # Get the python processes running before starting 
                         # the spider
        startPrc()       # Start the spider
        time.sleep(600)  # Let the spider crawling for 10 minutes
        aft = getPrcs()  # Get the python processes running now

        while checkChr():# While files being added continueously, keep 
                         # checking if more are being added
            checkChr()        
        else:            # If not, kill the process, restart the monitoring
            killPrc(pre, aft)
            print('Spider killed. Restarting...\n')
            monitorChr()
            break

if __name__ == '__main__':
    monitorChr()

