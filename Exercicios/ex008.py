# Desafio 7
# Desenvolva um programa que leia as duas notas de um aluno, calcule a e mostre a sua média

nome = str(input('Digite o nome do Aluno:'))
n1 = int(input('Nota do primeiro sementre: '))
n2 = int(input('Nota do segundo sementre: '))

m = (n1+n2)/2

print('A Media do aluno(a) {} é {}'.format(nome,m))