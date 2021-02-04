class RemoveFirst:
    def remove_first(self, mylist):
        # returns -
        # mylist - is a list of some elements
        print("Old list: ", mylist)
        mylist.pop(0)
        print("New list: ", mylist)


rf = RemoveFirst()
rf.remove_first(["red", "black", "green", "white", "orange"])
rf.remove_first([255, 3678, 95, 158, 759, 157])
