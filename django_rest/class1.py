""" Создайте базовый класс Animal с методом speak(), который выводит "Звук животного".
Создайте классы-наследники:

Dog, который переопределяет speak() и выводит "Гав!"
Cat, который переопределяет speak() и выводит "Мяу! """

class Animal:
    @staticmethod
    def speak():
        print('Звук животного')
    

class Dog(Animal):
    @staticmethod
    def speak():
        print('Гав!')
        

class Cat(Animal):
    @staticmethod
    def speak():
        print('Мяу!')


animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.speak()
    