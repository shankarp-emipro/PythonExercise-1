class CopyList:
    def copy_list(self, mylist):
        # returns -
        # mylist - is a list of some elements
        l2 = mylist
        print("Original:", mylist)
        print("Copy:", l2)


cl = CopyList()
cl.copy_list([1, 2, 3, 4, 5])