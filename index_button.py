import time
import os
from utils import *
import requests
import sys
import datetime
from gpiozero import LED, Button
led_send = LED(17)
button = Button(2)

wifi_connection = False
press_connection = False
start = datetime.datetime.now()

while True:

    try:
        button.wait_for_press()
        delta = (datetime.datetime.now() - start).seconds
        if delta > 3:
            press_connection = False
        print('You pushed me')
        led_send.on()
        if not press_connection:
            send_to_api(message)
            press_connection = True
            start = datetime.datetime.now()       
        
        time.sleep(2)
        led_send.off()


    except Exception as e:
        led_send.off()
        print('Error - ', e)
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
