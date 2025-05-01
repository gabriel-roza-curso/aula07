def calcula(n):
    dobro = n * 2
    triplo = n * 3
    quadrado = n ** 2
    return dobro, triplo, quadrado


num = float(input('Escolha um número:'))

dobro, triplo, quadrado = calcula(num)
print(f'O dobro de {num} é {dobro}')
print(f'O triplo de {num} é {triplo}')
print(f'O quadrado de {num} é {quadrado}')