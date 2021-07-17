import time
import os
from utils import *
import requests

while True:

    try:
        print('scanning networks...')
        
        wifi_list = get_wifi_list()

        for wifi_point in wifi_list:
            print('WiFi - ', wifi_point)
            if wifi_point in white_list:
                print('wifi point {} in white wifi lists'.format(wifi_point))
                print('check connection')
                connection = check_connection(wifi_point)
                if connection:
                    print('CONNECTED SUCCESSFULLY: ', wifi_point)
                    break


    except Exception as e:
        print('Error - ', e)
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        break
