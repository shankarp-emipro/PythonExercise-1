class SortDictionary:
    def sort_dict(self, d1):
        # returns -
        # d1 : dictionary
        d2 = {}     # empty dictionary for future use
        print("sort in ascending by key")
        for d in sorted(d1):
            d2[d] = d1.get(d)
        print(d2)

        d3 = {}     # empty dictionary for future use
        print("sort in descending by key")
        for d in sorted(d1, reverse=True):
            d3[d] = d1.get(d)
        print(d3)

        print("sort in ascending by value")
        print(dict(sorted(d1.items(), key=lambda l: (l[1], l[0]))))

        print("sort in descending by value")
        print(dict(sorted(d1.items(), key=lambda l: (l[1], l[0]), reverse=True)))


sd = SortDictionary()
sd.sort_dict({7: 2, 9: 4, 4: 3, 2: 1, 0: 0})
