from random import randint
numeros = randint (1,10), randint (1,10), randint (1,10), randint (1,10), randint (1,10)
print('Os valoeres sorteados foram:',end='')
for n in numeros:
    print(f' {n} ', end='')

print(f'\nO maior valor mostrado foi {max(numeros)}')
print(f'\nO maior valor mostrado foi {min(numeros)}')
