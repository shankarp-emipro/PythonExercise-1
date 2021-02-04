class DictionaryListValue:
    def dict_list_demo(self):
        # returns -
        mydict = {}     # empty dictionary for further use
        l1 = []     # empty list for further use
        l2 = []     # empty list for further use
        l3 = []     # empty list for further use

        for i in range(10, 41):
            if i < 21:
                l1.append(i)
            elif i < 31:
                l2.append(i)
            else:
                l3.append(i)
        mydict['x'] = l1
        mydict['y'] = l2
        mydict['z'] = l3
        print("First")
        for key, val in mydict.items():
            print(key, "has value", val)

        print("Second")
        for v in mydict.items():
            print(v[1][4])


dlv = DictionaryListValue()
dlv.dict_list_demo()
