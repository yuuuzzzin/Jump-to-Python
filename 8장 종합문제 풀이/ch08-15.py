def duplicateNum(s):
    result = []
    for c in s:
        if c not in result:
            result.append(c)
        else:
            return False
    return len(result) == 10


num = input("입력: ")
numList = num.split(" ")
result = list(map(duplicateNum, numList))

print("출력:", end=" ")
for v in result:
    print(v, end=" ")
