str1 = "a:b:c:d"
str2 = str1.split(":")  # ':'를 구분자로 문자열을 나누어 리스트에 넣는다.
result = '#'.join(str2)  # 리스트 요소 사이사이에 '#'를 삽입하고 문자열로 만들어준다.
print(result)
