fib_list = [0, 1]


def fib(n):
    i = 0
    while fib_list[i] + fib_list[i+1] <= int(n):
        fib_list.append(fib_list[i] + fib_list[i+1])
        i += 1


num = input("정수를 입력하세요 : ")
fib(num)
print(fib_list)
