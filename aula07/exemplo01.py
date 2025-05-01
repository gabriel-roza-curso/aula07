# funções em python inicia com a palavra
# reservada def.
# Funções são rotinas em seu conceito
# Só serão executadas se forem chamadas

# def mostrar_linha():
#     print(30 * '=')


# mostrar_linha()
# print('MÓDULO 01')
# mostrar_linha()
# print('ALGORITMOS')
# mostrar_linha()
# print('ANÁLISE DE DADOS')
# mostrar_linha()

# def saudacao(texto):
#     print(f'Olá {texto}!')


# nome = input('Qual o seu nome? ')
# saudacao(nome)

# def somar(a, b):
#     s = a + b
#     return s


# soma = somar(4, 5)
# print(f'O valor da variavel soma é {soma}')


def somar_numeros(x, y):
    s = x + y
    return s


for i in range(3):
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    soma = somar_numeros(n1, n2)
    print(soma)