class CheckDictValue:
    def __init__(self, d1):
        self.d1 = d1    # d1 is dictionary which contains some keys and values

    def check_dict_val(self, n):
        # returns -
        # n is a number to check if it is equal to all the values in dictionary
        flag = 0    # flag value will be used in condition to check whether all value are same or not
        for val in self.d1.values():
            if val != n:
                flag = 1
                break

        if flag == 0:
            print(True)
        else:
            print(False)


cdv = CheckDictValue({'Cierra Vega': 23, 'Alden Cantrell': 23, 'Kierra Gentry': 23, 'Pierre Cox': 23})
cdv.check_dict_val(23)
