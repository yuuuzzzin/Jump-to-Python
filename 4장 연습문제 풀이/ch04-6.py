user_input = input("파일에 저장할 내용을 입력해주세요 : ")

with open("test.txt", 'a') as f1:
    f1.write(user_input)

with open("test.txt", 'r') as f2:
    print(f2.read())