#Modulo01 - Exercicio 09 - Solicite ao usuário o número de horas de exercício físico por semana.
#Calcule o total de calorias queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício.

horas_exercicio =  float(input("Quantas horas de exercício você faz por semana? ").replace(',', '.'))
minutos_exercicio = horas_exercicio*60

total_calorias = round((minutos_exercicio*5),2)

print (f"Esse mês você gastou {total_calorias} calorias.")