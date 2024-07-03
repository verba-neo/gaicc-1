import random
import requests
from bs4 import BeautifulSoup

print(random.sample(range(1, 46), 6))

res = requests.get('https://dhlottery.co.kr/gameResult.do?method=byWin')
data = BeautifulSoup(res.text, 'html.parser')

data.select()