count = ('zero', 'um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')

while True:
    num = int(input('Digite um numero: '))
    if 0 <= num <= 20:
        break
    print(f'vocé digitou o número {num}, tente novamente!')

print(f'Vocé digitou o número {num}, e seu nome por extenso é {count[num]}')