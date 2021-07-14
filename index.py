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
    wifi_list.append(data[ssid_num:][:data[ssid_num:].find("\n")].split(':')[1])

for wifi_point in wifi_list:
    print('WiFi - ', wifi_point)
# print('set class wifi')
# wifi = pywifi.PyWiFi()

# print('set instance iface')
# iface = wifi.interfaces()[0]

# print('start scanning network...')
# Name = iface.name()
# iface.scan()
# time.sleep(2)

# results = iface.scan_results()

# for data in results:
#     print('Found network ', data.ssid)