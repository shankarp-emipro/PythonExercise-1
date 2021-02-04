class CreateListAndTuple:
    def __init__(self):
        print("Enter comma separated numbers to convert to list and tuple:")
        data = input("Enter numbers: ")     # data - takes comma separated string
        print("List: ", list(data.split(',')))
        print("Tuple: ", tuple(data.split(',')))


obj = CreateListAndTuple()
