import time
import os
from utils import *
import requests

while True:

    try:
        print('check connection')
        connection = check_connection(wifi_point)
        if connection:
            print('CONNECTED SUCCESSFULLY: ', wifi_point)
            break


    except Exception as e:
        print('Error - ', e)
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        break
