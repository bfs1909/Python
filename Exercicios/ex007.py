# Desafio 6 
# Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite um numero:'))
d = n * 2
t = n * 3
r = n ** 0.5

print('O dobro de {} é {}!, o triplo de {} é {}!, é a raiz quadra de {} é {:.2f}!'
      .format(n,d,n,t,n,r))