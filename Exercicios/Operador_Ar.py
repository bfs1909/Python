# Operadores Aritimericos 

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

resultado1 = n1 + n2
resultado2 = n1 - n2
resultado3 = n1 * n2
resultado4 = n1 / n2
resultado5 = n1 // n2
resultado6 = n1 ** n2
resultado7 = n1 % n2

print('Resultado da soma: {} '.format(resultado1))
print('='*20)

print(f'Resultado da subtração: {resultado2} ')
print('='*20)

print('Resultado da multiplicação: ', resultado3)
print('='*20)

print('Resultado da divisão: {:.2f}' .format(resultado4))
print('='*20)

print('Resultado da divisão inteira: ', resultado5)
print('='*20)

print('Resultado da potência: {} '.format(resultado6))
print('='*20)

print('Resultado do módulo: ', resultado7)
print('='*20)
