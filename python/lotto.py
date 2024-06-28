# 1 ~ 45 까지의 숫자 중에서 6개를 랜덤하게 뽑는다.
import random

# Lotto 번호 6개 뽑고 lucky 변수에 저장하기.
lucky = random.sample(range(1, 46), 6)
lucky.sort()
# 출력하기
print(lucky)