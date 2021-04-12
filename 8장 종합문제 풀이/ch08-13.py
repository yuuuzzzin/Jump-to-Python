number = input("입력: ")
nums = list(map(int, number))  # 숫자 문자열을 숫자 리스트로 바꾸어준다.
result = []

for i, num in enumerate(nums):
    result.append(str(num))
    if i<len(nums)-1:  # 리스트 안 현재 요소가 다음 요소를 가질 때
        if (num%2==1) & (nums[i+1] %2==1):  # 현재 요소와 다음 요소가 홀수이면
            result.append('-')
        elif (num%2==0) & (nums[i+1] %2==0):  # 현재 요소와 다음 요소가 짝수이면
            result.append('*')

print("".join(result))