class IterateDictionary:
    def iterate_dict(self, d1):
        # returns -
        for kv in d1.items():       # items() - for individual key-value pair
            print("Key is", kv[0], "and Value is", kv[1])


idict = IterateDictionary()
idict.iterate_dict({1: 10, 2: 20, 3: 30, 4: 40, 5: 50})
