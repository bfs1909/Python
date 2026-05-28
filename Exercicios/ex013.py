# Desafio 12
# Faça um algoritmo que leia o preço de um produto e 
# mostre seu novo preço, com 5% de desconto 

produto = float(input('Digite o preço do produto que vai receber os 5%: '))

desconto = produto * 0.05
valor_final = produto - desconto

print(f'O valor final do produto é R${valor_final}')