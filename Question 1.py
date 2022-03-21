class Calculator:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def adder(self):
        return self.val1 + self.val2

    def subtractor(self):
        return self.val1 - self.val2

    def multiplier(self):
        return self.val1 * self.val2

    def divider(self):
        return self.val1 / self.val2

    def clear(self):
        self.val1 = self.val2 = 0

val1 = int(input("Input value 1: "))
val2 = int(input("Input value 2: "))

calculator = Calculator(val1, val2)

print("Addition:", calculator.adder())
print("Subtraction:", calculator.subtractor())
print("Multiplication:", calculator.multiplier())
print("Division:", calculator.divider())
calculator.clear()
