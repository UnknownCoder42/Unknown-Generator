from concurrent.futures import ThreadPoolExecutor
from httpx_socks import SyncProxyTransport
from random import choice
from string import ascii_letters
from httpx import Client
from HCaptcha import Bypass
from time import sleep, time
import json
import subprocess
import os
import requests
import sys

os.system('cls') 

os.system("")
os.system('mode con: cols=90 lines=20')

os.system('title  Unkonwn Coder︱Loading Menu') 
sleep(5)
os.system('cls') 
os.system('title Unkonwn Coder︱Menu') 

_0, __0, _______0, _____0, ________0 = 0, open("proxies.txt", encoding='utf-8').readlines(), 60, ThreadPoolExecutor(max_workers=int(100000)), 500
____0 = 2500 # Thread Amount


print("                              \u001b[38;5;90m _   _        _                                     ___          _           ")
print("                              \u001b[38;5;91m| | | | _ _  | |__ _ _   ___  _ __ __  _ _         / __| ___  __| | ___  _ _ ")
print("                              \u001b[38;5;93m| |_| || ' \ | / /| ' \ / _ \ \ V  V /| ' \       | (__ / _ \/ _` |/ -_)| '_|")
print("                              \u001b[38;5;94m \___/ |_||_||_\_\|_||_|\___/  \_/\_/ |_||_|       \___|\___/\__/_|\___||_|  ")

print()
___0 = str(input("                                      [+] \u001b[38;5;93mInvite Code: "))
_________0 = str(input("                                      [+] \u001b[38;5;93mBot Usernames: "))
__________0 = str(input("                                      [+] \u001b[38;5;93mThread Usernames: "))


def _O():
    global _0, __0
    try:
        _ = __0[_0]
        _0 += 1
    except:
        _, _0 = __0[0], 0
    return _.replace('\n','')

def __O(_0):
    return ''.join(choice(ascii_letters)for _ in range(_0))

def ___O(X, OO_):
    global __X0, __X1
    X_ = Bypass()
    print("\u001b[38;5;89m [-] Unkonwn Coder | Captcha Bypassed")
    while True:
        if OO_ <= int(time()):
            break
        sleep(1)
    while True:
        try:
            with Client(transport=SyncProxyTransport.from_url(f'socks4://{_O()}')) as _00:
                _ = _00.post("https://discord.com/api/v9/auth/register", headers={"Host":"discord.com", "Connection":"keep-alive", "sec-ch-ua":'"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', "X-Super-Properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkzLjAuNDU3Ny42MyBTYWZhcmkvNTM3LjM2IEVkZy85My4wLjk2MS40NyIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAuNDU3Ny42MyIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS9jaGFubmVscy81NTQxMjU3Nzc4MTg2MTU4NDQvODcwODgxOTEyMzQyODUxNTk1IiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==", "X-Fingerprint": "", "Accept-Language":"en-US", "sec-ch-ua-mobile":"?0", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47", "Content-Type":"application/json", "Authorization":"undefined", "Accept":"*/*", "Origin":"https://discord.com", "Sec-Fetch-Site":"same-origin", "Sec-Fetch-Mode":"cors", "Sec-Fetch-Dest":"empty", "Referer":"https://discord.com/register", "X-Debug-Options":"bugReporterEnabled", "Accept-Encoding":"gzip, deflate, br", "Cookie": "OptanonConsent=version=6.17.0; locale=th"}, json={"fingerprint": "", "username":f"{_________0} | {__O(int(__________0))}", "invite": X , "consent": True, "gift_code_sku_id":"", "captcha_key": X_}).json()
            ______0 = open("tokens.txt", "a")
            ______0.write(f'{_["token"]}\n')
            ______0.close()
            return _["token"]
        except: pass

def ____O(OO_):
    print(' [$] ' + ___O(___0, OO_))

___OO = int(time()+int(_______0))
print(f"Start In: {_______0} Seconds")
for _ in range (____0):
    _____0.submit(____O, ___OO)
    if _ == ________0:
        sleep(10);________0 += 500
