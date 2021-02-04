class DropNoneValue:
    def drop_none(self, d1):
        # returns -
        # d1 is dictionary which contains some keys and values
        del_keys = []   # empty list for further use, which will hold all keys of values to be deleted
        for key, val in d1.items():
            if val == None:
                del_keys.append(key)

        print("Original dictionary:", d1)
        for i in del_keys:
            d1.pop(i)

        print("New Dictionary after dropping empty items", d1)


dnv = DropNoneValue()
dnv.drop_none({'c1': 'Red', 'c2': 'Green', 'c3': None})
