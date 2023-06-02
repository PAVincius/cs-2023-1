class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        pass


class Cachorro(Animal):
    def emitir_som(self):
        return "Au au!"


class Cavalo(Animal):
    def emitir_som(self):
        return "Relincho!"


class Preguica(Animal):
    def emitir_som(self):
        return "a mimir..."


class AnimalInvalidoException(Exception):
    def __init__(self):
        super().__init__("Tipo de Animal Inválido")


class Veterinario:
    def examinar(self, animais):
        for animal in animais:
            if isinstance(animal, (Cachorro, Cavalo, Preguica)):
                print(f"Examinando {animal.nome}")
                print(animal.emitir_som())
            else:
                raise AnimalInvalidoException()


# Testando o código

try:
    veterinario = Veterinario()
    
    cachorro = Cachorro("Rex")
    cavalo = Cavalo("Spirit o corsel indomável")
    preguica = Preguica("Sid")
    gato = Animal("Garfield")  # animal inválido
    
    animais = [cachorro, cavalo, preguica, gato]
    veterinario.examinar(animais)
    
except AnimalInvalidoException as e:
    print(e)
