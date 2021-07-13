import subprocess
networks = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
networks = networks.decode('ascii')
networks = networks.replace('\r', '')
ssid = networks.split('\n')
ssid = ssid[4:]
ssids = []
x = 0
print('START')
while x < len(ssid):
    if x % 5 == 0:
        ssids.append(ssid[x])
    x += 1
print(ssids) 