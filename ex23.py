class ListItemMultiply:
    def multiply(self, mylist):
        # returns -
        # mylist - is a list of some elements
        ans = 1
        for num in mylist:
            ans *= num

        print("ans:", ans)


lim = ListItemMultiply()
lim.multiply([1, 2, 3, 4])
