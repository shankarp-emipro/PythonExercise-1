class NumSquare:
    def num_square(self):
        # returns -
        d1 = {}     # empty dictionary
        for i in range(10):     # 0 to 10
            d1[i+1] = (i+1) * (i+1)

        print(d1)


ns = NumSquare()
ns.num_square()
