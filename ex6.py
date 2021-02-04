class Sum:
    def add(self):
        # returns -
        # a,b and c are future numbers on which different mathematical operation will be performed
        a = int(input("Ener n1: "))
        b = int(input("Ener n2: "))
        c = int(input("Ener n3: "))
        if a == b == c:
            return 3*(a + b + c)
        return a + b + c


s = Sum()
print("Sum is: ", s.add())
