# filter와 lmbda를 사용해 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거
a = list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3]))
print(a)
