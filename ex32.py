class CommonValue:
    def get_common(self, d1, d2):
        # returns -
        # d1 and d2 are two dictionaries which contains some keys and values
        for k1, v1 in d1.items():   # k1 and v1 are key and value respectively from d1
            for k2, v2 in d2.items():   # k2 and v2 are key and value respectively from d2
                if (k1 == k2) & (v1 == v2):
                    print(k1, ":", v1, "is present in both d1 and d2")


cv = CommonValue()
cv.get_common({'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2})
