'''
Створіть базовий клас Animal із методом talk. Потім створіть два підкласи: Dog і Cat з їхніми
власними реалізаціями методу talk. Наприклад, у Dog може бути print 'woof woof', а у Cat –
print 'meow'. Також створіть просту функцію, яка приймає на вхід екземпляр класу Cat або Dog і
виконує метод talk для вхідного параметра.
'''


class Animal:

    def talk(self):
        raise NotImplementedError ('Must be Implemented in sub class')


def animal_talk(inst):
    print(inst.animal_talk())


class Dog(Animal):

    def talk(self):
        print('woof woof')


class Cat(Animal):

    def talk(self):
        print('meow')
