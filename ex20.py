class PrintDictionary:
    def print_dictionary(self, d1):
        # returns -
        # d1 - is a dictionary with some key and value
        for key in d1:
            print(key, "--", d1.get(key))


pd = PrintDictionary()
pd.print_dictionary({'a': 2, 'x': 8, 'z': 1})
