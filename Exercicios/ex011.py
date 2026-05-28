# Desafio 10
# Crie um programa que leia quanto dinheiro a pessoa tem na carteira e 
# mostre quantos dolares ela pode comprar 

n = str(input('Qual o seu nome:'))
c = int(input(f'Quando você gostaria de colocar na sua carteira {n}: '))

vd = c / 3.27

print(f'{n} pode comprar R${vd:.2f} dolares')
