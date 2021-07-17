import time
import os
import requests
import re
import os
from dotenv import load_dotenv
load_dotenv()

test_urls = os.getenv("TEST_LISTS_URL").split(',')
white_list = os.getenv("WHITE_LISTS").split(',')
check_url = os.getenv("CHECKS_URL")
test_check_url = os.getenv("INTERNET_CHECK_URL")

def url_ok(url):
    try:
        r = requests.head(url)
        print('status - ', r.status_code)
        return r.status_code == 200
    except requests.exceptions.ConnectionError:
        if r.status_code = "Connection refused":
            return True
        else:
            return False
        
            

def get_wifi_list():
    data = os.popen('sudo iwlist scanning').read()

    start_ssid = [m.start() for m in re.finditer('ESSID', data)]

    wifi_list = []
    for ssid_num in start_ssid:
        wifi_list.append(data[ssid_num:][:data[ssid_num:].find("\n")].split(':')[1][1:-1])
    return wifi_list

def check_connection(wifi_point):
    if wifi_point in test_urls:
        return url_ok(test_check_url)
    elif wifi_point in white_list:
        return url_ok(check_url)
    else:
        print('wrong connection')
        return False
def check_connection_mode(mode):
    if mode == "internet":
        return url_ok(test_check_url)        
    else:
        return url_ok(check_url)