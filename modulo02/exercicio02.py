'''Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

turno = input("Em que turno você estuda? Digite M para Matutino, V para Vespertino ou N para Noturno: ")

if turno.upper == 'M':
    print("Bom Dia!")
if turno.upper() == 'V':
    print("Boa Tarde!")
if turno.upper() == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")

