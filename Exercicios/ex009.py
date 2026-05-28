# Desafio 08
# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros 

n = int(input('Digite um valor: '))

m = n
cm = m * 100
mn = m * 1000

print('{}m e igual a {}cm é {}mn'.format(m,cm,mn))