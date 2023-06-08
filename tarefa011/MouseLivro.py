class Mouse(Produto):
    def __init__(self, nomeloja, preco, tipo):
        super().__init__(nomeloja, preco)
        self.tipo = tipo
    
    def get_tipo(self):
        return self.tipo
    
    def set_tipo(self, tipo):
        self.tipo = tipo
    
    def get_descricao(self):
        return super().get_descricao() + f", {self.tipo}"
        

class Livro(Produto):
    def __init__(self, nomeloja, preco, autor):
        super().__init__(nomeloja, preco)
        self.autor = autor
    
    def get_autor(self):
        return self.autor
    
    def set_autor(self, autor):
        self.autor = autor
    
    def get_descricao(self):
        return super().get_descricao() + f", {self.autor}"
