reg = "881120-1068234"
year = "19" + reg[0:2]  # yyyy
month = reg[2:4]  # mm
date = reg[4:6]  # dd
num = reg[7:]  # 주민등록번호 뒷자리

print(year + month + date)  # 년월일(yyyymmdd) 출력
print(num)  # 주민등록번호 뒷자리 출력
