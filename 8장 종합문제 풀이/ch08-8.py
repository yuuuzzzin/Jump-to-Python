f = open('abc.txt', 'r')
content = f.readlines()  # 파일의 모든 라인을 읽어들인다.
f.close()

content.reverse()  # 라인을 역순으로 정렬한다.

f = open('abc.txt', 'w')
for line in content:
    line = line.strip()  # 줄 바꿈 문자를 제거한다.
    f.write(line)
    f.write('\n')
f.close()
