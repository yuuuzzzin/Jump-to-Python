def average(*args):  # 입력으로 들어오는 수의 개수가 정해져 있지 않기 때문에 *args 사용
    sum = 0
    for i in args:
        sum += i
    average = sum / len(args) # 수의 총 합을 입력으로 받은 수의 개수로 나누어 평균 구하기
    return average

print(average(1, 2, 3, 4, 5))