class DictionaryDemo:
    def concat_me(self, d1, d2, d3):
        # returns -
        # d1,d2 and d3 are dictionary with some key and value
        d1.update(d2)
        d1.update(d3)
        print(d1)


dd = DictionaryDemo()
d1 = {1:10, 2:20}
d2 = {3:30, 4:40}
d3 = {5:50, 6:60}
dd.concat_me(d1, d2, d3)