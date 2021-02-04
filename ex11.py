class DictIterate:
    def lets_iterate(self, d1):
        # returns -
        # d1 - is a dictionary with some key and value
        for key in d1:
            print("Key is {key} and Value is {val}".format(key=key, val=d1.get(key)))


di = DictIterate()
d1 = {"fname": "Shankar", "lname": "Pariyar", "company": "Emipro"}
di.lets_iterate(d1)