class ListToString:
    def list_to_string(self, mylist):
        # returns -
        # mylist - is a list of some elements
        mystr = ""      # mystr - is empty string to store list elements
        for word in mylist:
            mystr += word + " "
        print(mystr)


lts = ListToString()
lts.list_to_string(["Hello", "I'm", "Shankar", "Pariyar"])