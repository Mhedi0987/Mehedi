RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m' 
CYAN = "\033[36m"
END = "\033[0m"

banner = f"""
  {GREEN}                      ___ ___    _____  _________  ____  __.___________________   
 /   |   \  /  _  \ \_   ___ \|    |/ _|\_   _____/\______ \  
/    ~    \/  /_\  \/    \  \/|      <   |    __)_  |    |  \ 
\    Y    /    |    \     \___|    |  \  |        \ |    `   \
 \___|_  /\____|__  /\______  /____|__ \/_______  //_______  /
       \/         \/        \/        \/        \/         \/ 

  𝘛𝘰𝘰𝘭 𝘣𝘺 𝘚𝘈𝘝𝘈𝘎𝘌
  𝘛𝘌𝘓𝘌𝘎𝘙𝘈𝘔 𝘊𝘏𝘈𝘕𝘕𝘌𝘓 - @𝗦𝗮𝘃𝗮𝗴𝗲𝘅25  """

print(banner)

import requests

#Telegram channel :- t.m/savagex25 

url = "https://app.mynagad.com:20002/api/user/check-user-status-for-log-in"
number = input("Enter phone number: ")  # Assuming you get the phone number as input

headers = {
    "X-KM-User-AspId": "100012345612345",
    "X-KM-User-Agent": "ANDROID/1152",
    "X-KM-DEVICE-FGP": "19DC58E052A91F5B2EB59399AABB2B898CA68CFE780878C0DB69EAAB0553C3C6",
    "X-KM-Accept-language": "bn",
    "X-KM-AppCode": "01",
}

params = {"msisdn": number}

response = requests.get(url, headers=headers, params=params)

print(response.text)