import random

result = []

while len(result) < 6:
    num = random.randint(1, 45)  # 1~45 사이의 숫자 랜덤으로 생성
    if num not in result:  # 리스트 안에 중복되는 숫자가 없는 경우
        result.append(num)

print(sorted(result))
