import requests

g = "\033[92m"
r = "\033[0m"
b = "\033[34m"
red = "\033[31m"


def banner():
    b = r"""


 ____   _    ___ ____    ____  ____   _    __  __
|  _ \ / \  |_ _|  _ \  / ___||  _ \ / \  |  \/  |
| |_) / _ \  | || |_) | \___ \| |_) / _ \ | |\/| |
|  __/ ___ \ | ||  _ <   ___) |  __/ ___ \| |  | |
|_| /_/   \_\___|_| \_\ |____/|_| /_/   \_\_|  |_|

                  BY ERRORKING404
"""

    print(f"{g}{b}{r}")


url = "https://whatsbot.hostify.co.zw/api/pair"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "en-US,es-US,ur-PK",
    "Content-Type": "application/json",
    "Origin": "https://whatsbot.hostify.co.zw",
    "Referer": "https://whatsbot.hostify.co.zw/",
    "Accept-Encoding": "gzip, deflate, br",
}


def pair(number):
    try:
        resp = requests.post(url, headers=headers, json={"number": number}, timeout=15)

        if resp.status_code == 200:
            print(f"[SUCCESS {resp.status_code}]")
            try:
                return resp.json()
            except:
                return resp.text
        else:
            print(f"[ERROR {resp.status_code}] Failed. Try again later.")
            print(resp.text[:800])
            return None

    except requests.exceptions.RequestException as e:
        print(f"[NETWORK ERROR] {e} - Try again later")
        return None
    except Exception as e:
        print(f"[ERROR] {e} - Try again later")
        return None


banner()
number = input("Enter number. e.g:923xxx:")
lim = int(input("Enter limit. e.g: 500:"))
for i in range(1, lim + 1):
    print(f"{g}\nAttempt {i} for {number}...{r}")
    result = pair(number)
    if result:
        print(f"{g} Success.{r}")
        break
    time.sleep(2)
