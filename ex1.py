class CreateListAndTuple:
    def get_data(self):
        # returns -
        print("Enter comma separated numbers to convert to list and tuple:")
        data = input("Enter numbers: ")     # data - takes comma separated string
        my_list = list(data.split(','))     # my_list - generates list from given comma separated string
        my_tuple = tuple(data.split(','))   # my_tuple - generates tuple from given comma separated string
        print("List: ", my_list)
        print("Tuple: ", my_tuple)


obj = CreateListAndTuple()
obj.get_data()
