import time
import os
import pywifi
from pywifi import const
import re


print('scanning networks...')
data = os.popen('sudo iwlist scanning').read()



start_ssid = [m.start() for m in re.finditer('ESSID', data)]

wifi_list = []
for ssid_num in start_ssid:
    wifi_list.append(data[ssid_num:][:data[ssid_num:].find("\n")].split(':')[1][1:-1])

for wifi_point in wifi_list:
    print('WiFi - ', wifi_point)

if 'gate0105' in wifi_list:
    print('wifi point {} in white wifi lists'.format('gate0105'))

    print('set config')
    os.system('wpa_passphrase "gate0105" "Goldstar1!" | sudo tee /etc/wpa_supplicant.conf')
    print('sleep...')
    time.sleep(1)
    os.system('wpa_supplicant -c /etc/wpa_supplicant.conf -i wlan0')
    print('sleep...')
    time.sleep(1)

    print('Done')

if 'iPhone knru' in wifi_list:
    print('wifi point {} in white wifi lists'.format('iPhone knru'))

    print('set config')
    os.system('wpa_passphrase "iPhone knru" "qwerty12345" | sudo tee /etc/wpa_supplicant/wpa_supplicant.conf')
    print('sleep...')
    time.sleep(1)
    os.system('wpa_supplicant -c /etc/wpa_supplicant/wpa_supplicant.conf -i wlan0')
    print('sleep...')
    time.sleep(1)

    print('Done')