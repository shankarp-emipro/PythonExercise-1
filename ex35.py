class DictFilter:
    def filter_me(self, d1):
        # returns -
        # d1 is dictionary which contains some keys and values
        filtered_dict = {}      # empty dictionary to store filtered data
        for name, data in d1.items():
            # name contains key and data contains value from the dictionary d1
            if (data[0] >= 6) & (data[1] >= 70):
                filtered_dict[name] = {data[0]: data[1]}

        print(filtered_dict)


df = DictFilter()
df.filter_me({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)})
