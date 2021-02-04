class Calculate:
    def calculate(self):
        # returns -
        num = int(input("Enter num: "))     # num - number
        if num <= 17:
            return 17 - num
        return 2 * (num - 17)


c = Calculate()
print(c.calculate())
