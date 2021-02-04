class Students:
    def print_details(self, d1):
        # returns -
        # d1 - dictionary which contains students details
        for name, datalist in d1.items():
            # name and datalist contain key and nested set data respectively
            print(name)
            for data in datalist.items():
                print(data[0], ":", data[1])


s = Students()
s.print_details({'Aex':{'class':'V', 'rolld_id':2}, 'Puja':{'class':'V','roll_id':3}})