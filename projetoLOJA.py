class Produto:
    def __init__(self, nome, preco, estoque):
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
            print(f"Estoque insuficiente para o produto {self.nome}.")
            return False

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Cliente(Usuario):
    def __init__(self, nome, email, endereco):
        self.nome = nome
        self.email = email
        self.endereco = endereco
        self.carrinho = []

    def adicionar_ao_carrinho(self, produto):
        self.carrinho.append(produto)
        print(f"{produto.nome} adicionado ao carrinho de {self.nome}.")

class EntregaPadrao:
    def calcular_frete(self, distancia_km):
        return distancia_km * 1.5

class EntregaExpressa:
    def calcular_frete(self, distancia_km):
        return (distancia_km * 2.0) + 10.0

class Pedido:
    def __init__(self, cliente, tipo_entrega, distancia_km):
        self.cliente = cliente
        self.produtos = list(cliente.carrinho)
        self.tipo_entrega = tipo_entrega
        self.distancia_km = distancia_km

    def calcular_total(self):
        subtotal = sum(p.get_preco() for p in self.produtos)
        frete = self.tipo_entrega.calcular_frete(self.distancia_km)
        return subtotal + frete, subtotal, frete

    def finalizar_pedido(self):
        print("\nFinalizando pedido...")
        for produto in self.produtos:
            if not produto.diminuir_estoque(1):
                print("Pedido cancelado por falta de estoque")
                return
                
        total, subtotal, frete = self.calcular_total()
        print(f"Cliente: {self.cliente.nome}")
        print(f"Endereço: {self.cliente.endereco}")
        print(f"Subtotal: R${subtotal:.2f}")
        print(f"Frete: R${frete:.2f}")
        print(f"Total: R${total:.2f}")
        print("Status: pedido confirmado e em separação")


p1 = Produto("camiseta", 50.0, estoque=10)
p2 = Produto("tenis", 200.0, estoque=2)


maria = Cliente(
    "maria silva", 
    "maria@email.com", 
    "rua das flores, 123"
)

maria.adicionar_ao_carrinho(p1)
maria.adicionar_ao_carrinho(p2)

frete_rapido = EntregaExpressa()
pedido1 = Pedido(
    cliente=maria, 
    tipo_entrega=frete_rapido, 
    distancia_km=15
)
pedido1.finalizar_pedido()
