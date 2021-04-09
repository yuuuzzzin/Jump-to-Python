def is_odd(n):  # 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수
    if int(n) % 2 == 1:  # 2로 나눈 나머지가 1이면 홀수
        print("%d는 홀수입니다" % int(n))
    else:  # 2로 나눈 나머지가 1이 아니면 짝수
        print("%d는 짝수입니다" % int(n))


num = input("자연수를 입력하세요 : ")
is_odd(num)
