import os

os.system(f'title [REGION SPAMMER]')
os.system(f'mode 75,24')

import sys, time

from pystyle import Colors, Colorate

def slow_write(text):
    for x in text: print('' + x, end="");sys.stdout.flush();time.sleep(0.005)

slow_write("\u001b[38;5;159m-> Token: ")
token = input()
slow_write("\u001b[38;5;159m->  Gc ID: ")
id = input()

os.system('cls')

import requests

from colorama import Fore

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

print(f'{Fore.CYAN}                             By: {Fore.MAGENTA}@9n8')

import random

while True:
    rgc = random.choice(region)
    payload = {
        'region': str(rgc)
    }

    requests.patch(vc, json = payload, headers=headers)
    print(f"Region: "+str(rgc))
