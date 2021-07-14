import time
import pywifi
from pywifi import const

print('set class wifi')
wifi = pywifi.PyWiFi()

print('set instance iface')
iface = wifi.interfaces()[0]

print('start scanning network...')
Name = iface.name()
iface.scan()
time.sleep(2)

results = iface.scan_results()

for data in results:
    print('Found network ', data.ssid)