# Modulo 03 - Exercício 01
'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"; "Esteve no local do crime?"; "Mora perto da vítima?"; "Devia para a vítima?";
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como “Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classifica do como "Inocente".'''

print( 'Sobre o crime em questão, responda: ')

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas = []
for pergunta in perguntas:
    resposta = input(pergunta + " (s/n): ")
    if resposta.lower() == 's':
        respostas.append(1)
    else:
        respostas.append(0)

total = sum(respostas)

if total < 2:
    classificacao = "Inocente"
elif total == 2:
    classificacao = "Suspeita"
elif 2 < total <= 4:
    classificacao = "Cúmplice"
else:
    classificacao = "Assassino"

print("A pessoa é classificada como: " + classificacao)