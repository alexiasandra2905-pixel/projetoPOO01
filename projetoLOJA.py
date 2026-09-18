class Produto:
    def __init__ (self, nome, preco, estoque):
        self.nome = nome
        self._preco = preco
        self.estoque = estoque
    def get_preco(self):
        return self._preco
    def diminuir_estoque(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        else:
            print(f"Estoque insuficiênte de {self.nome}!")
            return False

class Usuario:
    def __init__ (self, nome, email):
        self