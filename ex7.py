class Repeat:
    def repeat_me(self):
        # returns -
        name = input("Enter name: ")
        n = int(input("Enter repeat no: "))     # n - number value to repeat the given name
        if n > 0:
            while n > 0:
                print(name)
                n -= 1


r = Repeat()
r.repeat_me()
