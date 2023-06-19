print('Desafio010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares pode comprar.')

real = float(input('Digite um valor:R$ '))
dolar = real / 5
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))