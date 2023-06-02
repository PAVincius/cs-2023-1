class Zoologico:
    def __init__(self):
        self.jaulas = []
    
    def add_animal(self, animal):
        self.jaulas.append(animal)
    
    def make_sounds(self):
        for animal in self.jaulas:
            animal.make_sound()
            
    def make_animals_run(self):
        for animal in self.jaulas:
            if isinstance(animal, Dog):
                print(animal.name, "is running!")
            elif isinstance(animal, Cat):
                print(animal.name, "is running!")
