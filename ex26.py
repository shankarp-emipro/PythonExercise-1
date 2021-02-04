class AddToDictionary:
    mydict = {"fname": "shankar"}

    def add_to_dict(self):
        # returns -
        print("Old Dictionary:", self.mydict)
        key, val = input("Enter (key:value): ").split(':')
        self.mydict[key] = val
        print("New dictionary:", self.mydict)


atd = AddToDictionary()
atd.add_to_dict()
