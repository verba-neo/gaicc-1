# lprice_checker.py
import requests
import time
from win10toast import ToastNotifier

NAVER_CLIENT_ID = 'L2q5Wm4QyVn5FanCMBsi'
NAVER_CLIENT_SECRET = 'CK4tH9_vew'
URL = 'https://openapi.naver.com/v1/search/shop.json'
h = {
    'X-Naver-Client-Id': NAVER_CLIENT_ID,
    'X-Naver-Client-Secret': NAVER_CLIENT_SECRET,
}
p = {'query': 'playstation5', 'display': 1,}

while True:
    res = requests.get(URL, headers=h, params=p)
    data = res.json()

    lprice = int(data['items'][0]['lprice'])

    if lprice < 520000:
        toaster = ToastNotifier()
        toaster.show_toast('PS5', '520000보다 싸다!', duration=5)
        break
    # 3시간
    time.sleep(60 * 60 * 3)