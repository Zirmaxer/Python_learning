class Dog:
    age_factor = 7
    def __init__(self, age):
        if Dog.validate(self, age) == True:
            self.age = age
        else:
            raise TypeError

        # write your program here
    def human_age(self):
        age = self.age * Dog.age_factor
        return "%.2f" %age

    def validate (self, age):
        if (type(age) == int or type(age) == float):
            return True
        else:
            raise TypeError