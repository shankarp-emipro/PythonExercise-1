class DisjointSet:
    def get_disjointset(self, s1, s2):
        # returns -
        # s1 and s2 - are two sets
        print(s1.difference(s2))


ds = DisjointSet()
ds.get_disjointset({"White", "Black", "Red"}, {"Red", "Green"})