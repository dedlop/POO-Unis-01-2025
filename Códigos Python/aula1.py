class Guerreiro:
    def __init__(self, nome, arma, dano_da_espada):
        self.nome = nome
        self.arma = arma
        self.dano_da_espada = dano_da_espada

    def ataque(self):
        return f"{self.nome} atacou usando {self.arma} e causou {self.dano_da_espada} de dano!!!"
    
player1 = Guerreiro("Arthurito", "Espada", 50)

print(player1.nome)
print(player1.ataque())

pessoa = {"nome": "Maria", "idade": 30}

for c, v in pessoa.items():
    print(v)