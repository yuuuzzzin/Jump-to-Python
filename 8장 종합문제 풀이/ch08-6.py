str = input("여러 개의 숫자를 콤마로 구분해 입력해주세요 : ")
numbers = str.split(',')  # ','를 구분자로 구분해 입력 받은 숫자들을 하나씩 리스트에 넣는다.
sum = 0

for i in numbers:
    sum += int(i)

print(sum)
