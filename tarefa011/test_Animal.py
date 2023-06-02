class AnimalTeste:
    def __init__(self):
        self.animals = []
    
    def create_animals(self):
        dog = Dog("Rex")
        cat = Cat("Whiskers")
        bird = Bird("Tweety")
        
        self.animals.append(dog)
        self.animals.append(cat)
        self.animals.append(bird)
    
    def make_sounds(self):
        for animal in self.animals:
            print(animal.make_sound())
