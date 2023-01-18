import random as rn
import requests

moz = "test"

if moz:
    user = ['hello', 'how are you', 'local']
    ip = ['172.211.11.123:4221', '341.23.123.1:5342', '454.234.1.13:2133']
    sys = ['linux', 'windows', 'MS-DOS']
    wi = ['win 8', 'win 7', 'win 10', 'win 11', 'kali', 'ubuntu']

    char = rn.choice(user)
    ipi = rn.choice(ip)
    syss = rn.choice(sys)
    wii = rn.choice(wi)

    requests.post("https://sheetdb.io/api/v1/......", data={"clinet": f"{char}", "host": f"{ipi}", "system": f"{syss}", "win~linux": f"{wii}"})

else:
    print("error")