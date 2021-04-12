num = input("구구단을 출력할 숫자를 입력하세요(2~9): ")

for i in range(1, 9):
    print((int(num)*i), end=' ')