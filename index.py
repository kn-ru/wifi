import time
import os
from utils import *
import requests
import sys
import datetime
from gpiozero import LED, Button
led_send = LED(17)
lend_wifi_status = LED(18)
button = Button(2)

wifi_connection = False
press_connection = False

while True:

    try:
        print('scanning networks...')
        if press_connection:
            delta = (datetime.datetime.now()-start).seconds
            if delta >= 3:
                press_connection = False

        if button.is_pressed and not press_connection:
            press_connection = True
            send_to_api(message)
            start = datetime.datetime.now()
        
        wifi_list = get_wifi_list()

        for wifi_point in wifi_list:
            print('WiFi - ', wifi_point)
            if wifi_point in white_list:
                print('wifi point {} in white wifi lists'.format(wifi_point))
                print('check connection')
                connection = check_connection(wifi_point)
                if connection:
                    print('CONNECTED SUCCESSFULLY: ', wifi_point)
                    send_message_debug('CONNECTED SUCCESSFULLY')
                    wifi_connection = True
                    lend_wifi_status.on()
                else:
                    wifi_connection = False
                    print('CONNECTED NOT ESTABLISHED')
                    lend_wifi_status.off()

    except Exception as e:
        wifi_connection = False
        lend_wifi_status.off()
        print('Error - ', e)
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        print('CONNECTED NOT ESTABLISHED. NETWORK DONT WORK')
