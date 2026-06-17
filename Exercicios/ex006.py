# Desafio 5
# Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e o seu antecessor.

n = int(input('Digite um numero:'))

s = n +1
a = n -1

print('O sucessor de {} e {}'.format(n, s))
print('O antecessor de {} e {}'.format(n, a))

# outra forma de fazer 

print('O numero {} tem como sucessor o numero {} e como antecessor o numero {}'.format(n,n+1,n-1))
