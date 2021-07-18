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

while True:

    try:
        button.wait_for_press()
        print('You pushed me')
        led_send.on()
        send_to_api(message)
        time.sleep(2)
        led_send.off()


    except Exception as e:
        led_send.off()
        print('Error - ', e)
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
