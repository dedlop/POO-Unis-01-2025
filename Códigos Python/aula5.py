# import random

# class MinhaLista:
#     def __init__(self, inicial = []):
#         self.lst = inicial
        
#     def __len__(self):
#         return len(self.lst)
    
#     def append(self, item):
#         self.lst.append(item)

#     def escolha(self):
#         return random.choice(self.lst)
    
#     def count(self,item):
#         return self.lst.count(item)


# minhalista = MinhaLista([10, 20, 30, 40, 40, 40])
# minhalista.append(2)
# minhalista.append(3)
# minhalista.append(5)
# minhalista.append(3)
# print(len(minhalista))
# print(minhalista.escolha())
# print(minhalista.count(40))


# import random

# class MinhaLista(list):

#     def escolha(self):
#         return random.escolha(self)
    
# minhalista = MinhaLista([2, 3, 5, 3, 10])
# print(len(minhalista))
# minhalista.append(100)
# print(minhalista)
# print(minhalista.count(3))


# Definindo a classe Personagem
# class Personagem:
#     def __init__(self, nome, idade, vida):
#         self.nome = nome
#         self.idade = idade
#         self.vida = vida

#     def exibir_info(self):
#         print(f"Nome: {self.nome}")
#         print(f"Idade: {self.idade}")
#         print(f"Vida: {self.vida}")


# # Definindo a classe Guerreiro, que herda de Personagem
# class Guerreiro(Personagem):
#     def __init__(self, nome, idade, vida, força, armadura):
#         # Chamando o construtor da classe pai (Personagem)
#         super().__init__(nome, idade, vida)
#         self.força = força
#         self.armadura = armadura

#     def exibir_info(self):
#         # Exibe informações do guerreiro, incluindo os atributos herdados
#         super().exibir_info()
#         print(f"Força: {self.força}")
#         print(f"Armadura: {self.armadura}")

# # Criando uma instância de Guerreiro
# player1 = Guerreiro("Lord Ded", 37, 150, 80, "Cota de malha")
# print("Informações do Guerreiro:")
# player1.exibir_info()


# Classe Pai: Usuario
class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def exibir_info(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Senha: {self.senha}")

# Classe Filho: Admin
class Admin(Usuario):
    def __init__(self, nome, email, senha, nivel_acesso):
        super().__init__(nome, email, senha)  
        self.nivel_acesso = nivel_acesso

    def exibir_info(self):
        super().exibir_info()  
        print(f"Nível de Acesso: {self.nivel_acesso}")

# Classe Filho: Cliente
class Cliente(Usuario):
    def __init__(self, nome, email, senha, plano_assinatura):
        super().__init__(nome, email, senha)  
        self.plano_assinatura = plano_assinatura

    def exibir_info(self):
        super().exibir_info()  
        print(f"Plano de Assinatura: {self.plano_assinatura}")



# Criando um objeto Admin
admin1 = Admin("Carlos Souza", "carlos@admin.com", "admin123", 3)
print("Informações do Administrador:")
admin1.exibir_info()

print("\n------------------\n")

# Criando um objeto Cliente
cliente1 = Cliente("Maria Oliveira", "maria@cliente.com", "cliente123", "Premium")
print("Informações do Cliente:")
cliente1.exibir_info()

