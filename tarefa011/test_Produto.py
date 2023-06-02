class ProdutoTeste:
    def __init__(self):
        self.carrinho = []
    
    def adicionar_produto(self, produto):
        self.carrinho.append(produto)
    
    def exibir_descricoes(self):
        for produto in self.carrinho:
            print(produto.get_descricao())
