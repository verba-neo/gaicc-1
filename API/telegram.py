import requests
import random

BOT_TOKEN = '7333426597:AAE9ZwENgHMEeWhh6vheuevD_rgLVAiaLzM'
BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}'

NAVER_CLIENT_ID = 'L2q5Wm4QyVn5FanCMBsi'
NAVER_CLIENT_SECRET = 'CK4tH9_vew'

# 지금까지 온 메시지 목록 확인
res = requests.get(BASE_URL + '/getUpdates')
data = res.json()

# 마지막(최신) 메시지의 발신자 / 내용 추출
sender_id = data['result'][-1]['message']['chat']['id']
msg = data['result'][-1]['message']['text']

# 맨 앞단어
command = msg.split()[0]
# 그 뒤에 오는 단어들 (띄어쓰기 기준)
args = msg.split()[1:]

if command == '안녕':
    reply = '안녕하세요'

elif command == '로또':
    import random
    reply = str(random.sample(range(1, 46), 6))

elif command == '최저가' or command == '쇼핑':
    #검색할 상품
    product = args[0]
    # Naver API 로 최저가 검색 기능 활용.
    NAVER_URL = 'https://openapi.naver.com/v1/search/shop.json'
    h = {
        'X-Naver-Client-Id': NAVER_CLIENT_ID,
        'X-Naver-Client-Secret': NAVER_CLIENT_SECRET,
    }
    p = {'query': product, 'display': 1, }

    res = requests.get(NAVER_URL, headers=h, params=p)
    shopping_data = res.json()['items'][0]
    reply = f'{product} => {shopping_data['lprice']} / {shopping_data['link']}'
else:
    reply = '몰라유..'


# 그대로 메시지 돌려주기
p = {
    'chat_id': sender_id,
    'text': reply,
}

res = requests.get(BASE_URL + '/sendMessage', params=p)