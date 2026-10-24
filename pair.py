import requests
import time



url = "https://whatsbot.hostify.co.zw/api/pair"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json",
    "Origin": "https://whatsbot.hostify.co.zw",
    "Referer": "https://whatsbot.hostify.co.zw/",
}


def pair(number):
    try:
        resp = requests.post(url, headers=headers, json={"number": number}, timeout=15)
        print(f"[{resp.status_code}] {resp.text[:800]}")

        if resp.status_code == 200:
            try:
                return resp.json()
            except:
                return resp.text
        return None

    except Exception as e:
        print(f"Error: {e}")
        return None


number = int(input("Enter number. e.g:923xxx"))
lim = input("Enter limit. e.g: 500:")
for i in range(1,lim + 1):
    print(f"\nAttempt {i+1} for {number}...")
    result = pair(number)
    if result:
        print(f"Success -> {result}")
        break
    time.sleep(2)
