import requests
import random

BOT_TOKEN = '7333426597:AAE9ZwENgHMEeWhh6vheuevD_rgLVAiaLzM'
BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}'

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

elif command == '더하기':
    total = 0
    for arg in args:
        total += int(arg)
    reply = total

else:
    reply = '모르는 명령어 입니다.'


# 그대로 메시지 돌려주기
p = {
    'chat_id': sender_id,
    'text': reply,
}

res = requests.get(BASE_URL + '/sendMessage', params=p)