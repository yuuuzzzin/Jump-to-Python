f1 = open("test.txt", 'r')
content = f1.read()
print("[원래 내용]\n" + content, end='\n')
f1.close()

content = content.replace("java", "python")

f2 = open("test.txt", 'w')
f2.write(content)
f2.close()

f3 = open("test.txt", 'r')
print("[바뀐 내용]\n" + f3.read())
f3.close()