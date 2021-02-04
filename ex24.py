class CountStringNum:
    def count_numof_string(self, mylist):
        # returns -
        # mylist - is a list of some elements
        count = 0
        for word in mylist:
            if len(word) >= 2:
                if word[0] == word[-1]:
                    count += 1

        print(count)


csn = CountStringNum()
csn.count_numof_string(["apple", "nayan", "d", "cc", "sp", "sounds"])