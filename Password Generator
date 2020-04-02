from random import *
from string import *

class Password:
    def __init__(self,l1):
        self.l1 = l1
        self.str = ""
        self.generate()

    def setup(self):
        print("Setup:-")
        print("     aascii_char: ", ascii_letters)
        print("     digits: ", digits)
        print("     special_char: ", punctuation)
        print("     Password parameters : length - ", self.l1)

    def generate(self):
        self.str = "".join(sample(ascii_letters + digits + punctuation, self.l1))
        print("\nGenerated Password: ", self.str)
        """join() method joins the elements of an iterable to the end of the string
        sample() method returns a list with a randomly selection of a specified number of items from a sequnce"""


p1 = Password(int(input("Password Length : ")))

#p1.setup()
