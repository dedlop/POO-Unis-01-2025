# l = ['gato', 'cão', 'frango']

# for animal in l:
#     print(animal)


# s = 'cupcake'

# for c in s:
#     if c in 'aeiou':
#         print(c)


# for i in range(10):
#     print(i, end=' ')

# n = 50

# for i in range(n):
#     if i % 2 == 0:
#         print(i, end = ' ')











# Solicita ao usuário uma letra e uma palavra ou frase
letra = input("Digite a letra para contar: ")
frase = input("Digite uma palavra ou frase: ")

# Inicializa uma variável para contar as ocorrências
contador = 0

# Loop para percorrer cada caractere da frase
for caractere in frase:
    if caractere == letra:
        contador += 1  # Aumenta o contador sempre que a letra for encontrada

# Exibe o resultado
print(f"A letra '{letra}' apareceu {contador} vezes.")
