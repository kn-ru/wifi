import pywifi
import time

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
iface.scan()
time.sleep(0.5)
results = iface.scan_results()

# use for or other loop to retrieve you data
print('start scan...')
for i in enumerate(results):    
    bssid = i.bssid
    ssid  = i.ssid
    print("Mac Address" + bssid +"\t" + "access point name" + ssid)
print('all done')