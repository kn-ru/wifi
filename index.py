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

    profile = pywifi.Profile()
    profile.ssid = 'gate0105'
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = 'Goldstar1!'

    print('connect with network...')
    wifi = pywifi.PyWiFi()
    Iface = wifi.interfaces()[0]
    Iface.remove_all_network_profiles()
    tmp_profile = Iface.add_network_profile(profile)
    Iface.remove_all_network_profiles()
    tmp_profile = Iface.add_network_profile(profile)
    print('sleep...')
    time.sleep(5)
    print('Done')