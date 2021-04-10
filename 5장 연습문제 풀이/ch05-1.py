class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class UpgradeCalculator(Calculator):  # Calculator 클래스를 상속하는 UpgradeCalculator
    def minus(self, val):  # 값을 뺄 수 있는 minus 메서드 추가
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)  # 10에서 7을 뺀 3을 출력
