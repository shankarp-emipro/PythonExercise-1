class CheckDictionaryValue:
    def check_value(self, d1):
        # returns -
        # d1 - is a dictionary with some key and value
        cname = input("Enter color name: ")     # cname - customer name
        if cname in d1.values():
            print(cname, "belongs to the dictionary")
        else:
            print(cname, "does not belongs to the dictionary")


cdv = CheckDictionaryValue()
cdv.check_value({"color1": "Red", "color2": "Green", "color3": "Blue"})