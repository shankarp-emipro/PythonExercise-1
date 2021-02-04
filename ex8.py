class Vowel:
    def is_vowel(self):
        # returns -
        vowel_list = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        ltr = input("Enter any letter: ")       # ltr - letter/character
        if ltr in vowel_list:
            print("{ltr} is a vowel".format(ltr=ltr))
        else:
            print("{ltr} is not a vowel".format(ltr=ltr))


v = Vowel()
v.is_vowel()