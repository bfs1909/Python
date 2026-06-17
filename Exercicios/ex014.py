# Desafio 13
# Faça um algoritimo que leia o salario de um funcionario
# e mostre seu novo salario, com 15% de aumento 

s = float(input('Digite o seu salario: R$'))

aumento = s * 0.15
salario_novo = s + aumento

print(f'O seu novo salario com 15% de aumento é R${salario_novo:.2f}!')

