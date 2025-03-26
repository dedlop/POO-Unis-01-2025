class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        print("Au au!")

class Gato(Animal):
    def falar(self):
        print("Miau!")

# Utilizando polimorfismo e late binding
def fazer_animal_falar(animal: Animal):
    animal.falar()

cachorro = Cachorro()
gato = Gato()

fazer_animal_falar(cachorro)  # Saída: Au au!
fazer_animal_falar(gato)  # Saída: Miau!





# Classe base
class Pagamento:
    def processar_pagamento(self):
        pass

# Classe CartaoDeCredito
class CartaoDeCredito(Pagamento):
    def processar_pagamento(self):
        print("Processando pagamento com Cartão de Crédito.")

# Classe Boleto
class Boleto(Pagamento):
    def processar_pagamento(self):
        print("Gerando boleto bancário.")

# Classe PayPal
class PayPal(Pagamento):
    def processar_pagamento(self):
        print("Processando pagamento via PayPal.")

# Função que pode realizar qualquer pagamento
def realizar_pagamento(pagamento: Pagamento):
    pagamento.processar_pagamento()

# Teste do sistema de pagamento
cartao = CartaoDeCredito()
boleto = Boleto()
paypal = PayPal()

# Realizando pagamentos de diferentes formas
realizar_pagamento(cartao)   # Saída: Processando pagamento com Cartão de Crédito.
realizar_pagamento(boleto)   # Saída: Gerando boleto bancário.
realizar_pagamento(paypal)   # Saída: Processando pagamento via PayPal.
