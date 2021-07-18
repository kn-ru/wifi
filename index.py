import time
import os
from utils import *
import requests
import sys
import datetime
from gpiozero import LED
lend_wifi_status = LED(18)

wifi_connection = False
lend_wifi_status.off()

while True:

    try:
        print('start search wifi network....')
        wifi_list = get_wifi_list()
        if len([x for x in white_list if x in set(wifi_list)]) > 0:
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
        else:
            wifi_connection = False
            print('WIFI NOT FOUND')
            lend_wifi_status.off()

    except Exception as e:
        wifi_connection = False
        lend_wifi_status.off()
        print('Error - ', e)
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        print('CONNECTED NOT ESTABLISHED. NETWORK DONT WORK')

