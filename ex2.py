class Colors:
    def __init__(self, color_list):
        self.color_list = color_list

    def get_fist_last(self):
        # returns -
        first_color = self.color_list[0]
        last_color = self.color_list[-1]
        print("First color: {fcolor}\nLast color: {lcolor}".format(fcolor=first_color, lcolor=last_color))


color = Colors(["red", "green", "white", "black"])
color.get_fist_last()


data = list(filter(lambda x: x*2, range(1, 10)))
print(data)
