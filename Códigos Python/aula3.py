class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo encapsulado (não acessível diretamente)

    def deposito(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def saque(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def consultar_saldo(self):
        return self.__saldo  # Acesso controlado ao saldo

# Criando uma conta bancária
conta = ContaBancaria("João", 1000)

# Realizando algumas operações
conta.deposito(500)  # Depósito de 500
conta.saque(200)     # Saque de 200
print("Saldo atual:", conta.consultar_saldo())  # Consultando saldo

print(conta.__saldo)