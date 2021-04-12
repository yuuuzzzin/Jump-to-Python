class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum(self):  # 합계
        sum = 0
        for number in self.numbers:
            sum += number
        return sum

    def avg(self):  # 평균
        average = self.sum() / len(self.numbers)
        return average


cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6, 7, 8, 9, 10])
print(cal2.sum())
print(cal2.avg())
