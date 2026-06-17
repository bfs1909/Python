# Desafio 11
# Faça um programa que leia a largura e a altura de uma parede 
# em metros, calcule a sua area e a quantidade de tinta necessaria
# para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m²

l = float(input('Digite a largura da parede:'))
a = float(input('Digite a altura da parede: '))

area = l * a 
p = area / 2

print(f'A area da parede é {area:.0f}m²')
print(f'Portanto você precisara de {p:.0f} litros de tinta para pintar essa parede.')