# pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup

URL = 'https://finance.naver.com/sise/'
# 요청 보내서 HTML 문서 다운로드
response = requests.get(URL)

# 문서를 컴퓨터가 이해할 수 있도록 분석(parsing)
data = BeautifulSoup(response.text, 'html.parser')

# 파싱된 데이터에서 원하는 내용만 추출
kospi = data.select_one('#KOSPI_now').text

print(kospi)

