class Produto:
    def __init__(self, nomeloja, preco):
        self.nomeloja = nomeloja
        self.preco = preco
    
    def get_nomeloja(self):
        return self.nomeloja
    
    def set_nomeloja(self, nomeloja):
        self.nomeloja = nomeloja
    
    def get_preco(self):
        return self.preco
    
    def set_preco(self, preco):
        self.preco = preco
    
    def get_descricao(self):
        return "Produto de informática"
