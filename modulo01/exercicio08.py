#Modulo01 - Exercicio 08: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print("Bem-vinde ao programa: Calcule seu sálario")
hora_trabalhada = float(input("Quanto você ganha por hora? ").replace(',', '.'))

total_horas = float(input("Quantas horas você trabalhou esse mês? ").replace(',', '.'))

salario = round(hora_trabalhada * total_horas, 2)

print(f"Seu salário esse mês será de R${salario}.")