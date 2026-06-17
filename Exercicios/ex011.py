# Desafio 10
# Crie um programa que leia quanto dinheiro a pessoa tem na carteira e 
# mostre quantos dolares ela pode comprar 

#---------------------------------------------------------------------

#n = str(input('Qual o seu nome: '))

#c = float(input(f'Quando você gostaria de colocar na sua carteira {n}: R$'))

#vd = c / 3.27

#print(f'{n} pode comprar R${vd:.2f} dolares')

#---------------------------------------------------------------------

carteira =  float(input(f'Quanto você gostaria de adicionar a carteira: R$'))

vd = carteira / 5.09

print(f'Com R${carteira:.2f} reais, você pode comprar R${vd:.2f} dolares')