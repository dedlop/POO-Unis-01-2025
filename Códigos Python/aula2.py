class Carro: # Definição da classe
    def __init__(self, modelo, cor): # Método construtor
        self.modelo = modelo  # Atributo de instância
        self.cor = cor        # Atributo de instância
        
    def mostrar_informacoes(self):
        print(f"Modelo: {self.modelo}, Cor: {self.cor}")


meu_carro = Carro("Fusca", "Azul")




class Aluno:
    def __init__(self, nome, curso, matriculado):
        self.nome = nome  # Atributo para o nome do aluno
        self.curso = curso  # Atributo para o curso que o aluno está fazendo
        self.matriculado = matriculado  # Atributo para indicar se o aluno está matriculado ou não

    def mostrar_informacoes(self):
        # Função para mostrar as informações do aluno
        print(f"Nome: {self.nome}")
        print(f"Curso: {self.curso}")
        print(f"Matriculado: {self.matriculado}")
        # print(f"Matriculado: {'Sim' if self.matriculado else 'Não'}")

aluno1 = Aluno("João Silva", "ADS", True)

aluno1.mostrar_informacoes()




class Cliente:
    def __init__(self, nome, cpf, saldo):
        self.nome = nome    # Atributo para o nome do cliente
        self.cpf = cpf      # Atributo para o CPF do cliente
        self.saldo = saldo  # Atributo para o saldo do cliente

    def fazer_deposito(self, valor):
        # Soma o valor ao saldo
        self.saldo = self.saldo + valor   # self.saldo += valor

    def mostrar_informacoes(self):
        # Exibe as informações do cliente
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Saldo: R${self.saldo:.2f}")


cliente1 = Cliente("Maria", "123.456.789-00", 100.0)

cliente1.mostrar_informacoes()

cliente1.fazer_deposito(50.0)

cliente1.mostrar_informacoes()

cliente1.fazer_deposito(5000.0)

cliente1.mostrar_informacoes()


