num =  (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o ultimo número: ')),
)
print(num)
print(f'O número 9 apareceu {num.count(9)} x')
print(f'O número 3 aprececeu na posição {num.index(3)+1}°')

for i in num:
    if i % 2 == 0:
        print(f'O número par é {i} e esta na posição {num.index(i)+1}')


