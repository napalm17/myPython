import subprocess

data = subprocess.check_output(['netsh','wlan', 'show', 'profile']).decode('cp857').split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]
f = open("profiles.txt", "w+")

for wifi in wifis:
    results = subprocess.check_output(['netsh','wlan', 'show', 'profile', wifi, 'key=clear']).decode('cp857').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
    try:
        text = f"Profile: {wifi}, Password: {results[0]}\n"
        f.write(text)
    except:
        pass
