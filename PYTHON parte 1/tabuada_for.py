num = int(input('Digite um número: '))

print(f'\nTABUADA DE {num}:')

for i in range (1, 11): #range(x, y) gera e retorna uma lista de números de x até y, sem incluir o y
    print(f'{num} x {i} = {num*(i)}')