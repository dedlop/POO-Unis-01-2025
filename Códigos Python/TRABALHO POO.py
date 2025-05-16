
class Vestido:
    def tamanho(self):
        pass
class P(Vestido):
    def tamanho(self):
        print("Você escolheu o vestido P.")
class M(Vestido):
    def tamanho(self):
        print("Você escolheu o vestido M.")
class G(Vestido):
    def tamanho(self):
        print("Você escolheu o vestido G.")

def tamanho_do_vestido(vestido: Vestido):
    vestido.tamanho()

p = P()
m = M()
g = G()

tamanho = input('Digite um tamanho do vestido:').lower()
if tamanho == 'p':
    tamanho_do_vestido(p)
elif tamanho == 'm':
    tamanho_do_vestido(m)
elif tamanho == 'g':
    tamanho_do_vestido(g)
else:
    print('Tamanho inválido.')