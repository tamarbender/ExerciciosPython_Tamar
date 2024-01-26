
''' 
Exercicio 3
3- Faça um Programa que peça a quantidade de quilômetros, transforme em metros,c entímetros e milímetros.
'''

quant_quilometro = (float(input('Informe um valor em quilometros: ')))
print(f'O valor informado foi: {quant_quilometro}')

valor_metros = quant_quilometro * 1000
valor_centimetro = quant_quilometro * 100000
valor_milimetro = quant_quilometro * 100000000
print('-------------------------------------------------')
print('-------------------------------------------------')

print(f'{quant_quilometro} transformado em Metros: {valor_metros} m')
print(f'{quant_quilometro} transformado em Centimetros: {valor_centimetro}cm')
print(f'{quant_quilometro} transformado em Milimetro : {valor_milimetro}mm')
