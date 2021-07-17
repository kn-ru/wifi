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
                connection = check_connection(wifi_point)
                if connection:
                    print('CONNECTED SUCCESSFULLY: ', wifi_point)
                    break


    except:
        pass
    finally:
