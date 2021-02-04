class ListSum:
    def list_sum(self, mylist):
        # returns -
        # mylist - is a list of some elements
        total = 0
        for n in mylist:
            total += n

        print("sum:", total)


ls = ListSum()
ls.list_sum([1, 2, 3, 4, 5])
