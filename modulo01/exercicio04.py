
''' 
Exercicio 4
4- Receba do usuário aquantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprimao consumo médio em km/l.
'''

quant_litros = (float(input('Informe o valor em litros de combustivel consumido: ')))
distancia_percorrida = (float(input('Informe a distáncia percorrida: ')))
valor_km_l = distancia_percorrida / quant_litros

print('-------------------------------------------------')
print('-------------------------------------------------')

print(f'O Consumo médio foi de : {valor_km_l} km/l')
