def calc_multa(v):
    valor = 4 * (v - 1000)
    return valor


peso = float(input('Qual o peso? '))

valor = calc_multa(peso)

if peso > 1000:
    print('Peso acima do permitido')
    print(f'O valor da multa é {valor}')

else:
    print('Peso dentro do permitido')
