# map과 lambda를 사용해 [1, 2, 3, 4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3, 6, 9, 12] 만들기
a = list(map(lambda x: x*3, [1, 2, 3, 4]))
print(a)
