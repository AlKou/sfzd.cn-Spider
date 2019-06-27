#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:47:36 2019

@author: Al_gou
"""

import time
import subprocess as sp
import os
import signal
import psutil

def checkChr():
    # Check if new files are being scraped and downloaded to the destination folder and return values accordingly.
    # Time interval is 2 minutes.
        
    b_len = len(os.listdir('/Users/Al_gou/Desktop/Scraped/Pics/'))
    time.sleep(120)
    a_len = len(os.listdir('/Users/Al_gou/Desktop/Scraped/Pics/'))

    if a_len == b_len:
        return False
    else:
        return True
    
def monitorChr():
    
    # Monitor the spider. When finding it adding no more files to folder, kill the process and restart a new one.
    
    with open('/Users/Al_gou/Desktop/Scraped/ChineseChar 3.5K.txt', 'r') as f:
        data = f.read()

    while data != '':
        # Start the spider.
        spd = sp.Popen('scrapy crawl chr', 
                        cwd='/Users/Al_gou/Desktop/ChineseChr/',
                        shell=True) 
        print('@ {} Process {} {} started.'.format(time.ctime(), spd.pid, psutil.Process(spd.pid).name()))
        print('@ {} Spider crawling...'.format(time.ctime()))

        # While files being added continueously, keep checking if more are being added.
        while checkChr():           
            checkChr() 
        # If not, kill the process, restart the monitoring.    
        else:                       
            os.kill(spd.pid, signal.SIGKILL)
            print('@ {} Spider killed. Restarting...\n'.format(time.ctime()))
            monitorChr()
            break


if __name__ == '__main__':
    monitorChr()

