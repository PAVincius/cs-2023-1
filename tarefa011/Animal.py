class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        pass
    
class Dog(Animal):
    def make_sound(self):
        return "Woof woof!"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow meow!"
    
class Bird(Animal):
    def make_sound(self):
        return "Chirp chirp!"
