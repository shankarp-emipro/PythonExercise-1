class ContainsOrNOt:
    def __init__(self, mylist):
        self.mylist = mylist

    def check(self):
        # returns -
        n = int(input("Enter a number: "))      # n - number
        if n in self.mylist:
            print("{num} belongs to the group: {nlist}".format(num=n,nlist=self.mylist))
        else:
            print("{} does not belongs to the group: {}".format(n, self.mylist))


con = ContainsOrNOt([1, 2, 3, 4, 5, 6, 7]);
con.check()