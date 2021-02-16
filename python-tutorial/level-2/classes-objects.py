# python unlike java is not an object oriented language, but it isnt a procedural language either
# python has elements of both procedural and oop, thus making it the SUPERIOR language


class Calc:  # we create a class named Calc
    # __init__ is called whenever its class is called
    def __init__(self, int1, int2):  # self binds arguments with our class attributes
        self.int1 = int1
        self.int2 = int2
        self.addition = self.int1 + self.int2
        self.subtract = self.int1 - self.int2
        self.multiply = self.int1 * self.int2
        self.division = self.int1 / self.int2

    def add(self):
        return self.addition

    def sub(self):
        return self.subtract

    def mul(self):
        return self.multiply

    def div(self):
        return self.division


# __init__ is used to define the main part of the class, the code in here is used when the class is called
Calc(1, 2).add()  # here we call Calc with ints 1 and 2 then use its object add()

