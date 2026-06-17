# Desafio 7
# Desenvolva um programa que leia as duas notas de um aluno, calcule a e mostre a sua média

nome = str(input('Digite o nome do Aluno:'))
n1 = float(input('Nota do primeiro sementre do aluno(a) {}: '.format(nome)))
n2 = float(input(f'Nota do segundo sementre do aluno(a) {nome}: '))

m = (n1+n2)/2

print('A Media das notas {} é {} do aluno(a) {} é {}'.format(n1, n2, nome, m))