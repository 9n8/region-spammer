import os

os.system(f'title [REGION SPAMMER]')
os.system(f'mode 75,24')

import colorama
from colorama import Fore

token = input(f"{Fore.MAGENTA}Token :{Fore.CYAN} ")
id = input(f"{Fore.MAGENTA}GC ID :{Fore.CYAN} ")

os.system('cls')

import requests

vc = "https://discord.com/api/v9/channels/"+str(id)+"/call"
msg = "https://discord.com/api/v9/channels/"+str(id)+"/messages"

m = {
    'content': 'hi'
}

headers = {
    'Authorization': str(token)
}

requests.post(msg, headers=headers, json=m)

region = [
    'hongkong',
    'europe',
    'brazil',
    'us-central',
    'us-east',
    'sydney',
    'russia',
    'india',
    'japan',
    'us-west',
    'us-south',
    'singapore'
]

print(f'{Fore.CYAN}                             By: {Fore.MAGENTA}@uo2')

import random

while True:
    rgc = random.choice(region)
    payload = {
        'region': str(rgc)
    }

    requests.patch(vc, json = payload, headers=headers)
    print(f"{Fore.LIGHTGREEN_EX}Region: "+str(rgc))
