"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
"""
def converte_moeda(real, taxa, nome_moeda):
    quantidade_moeda = real / taxa
    print(f'{real:.2f} reais equivalem a {quantidade_moeda:.2f} {nome_moeda}.')

def main():
    dolar = 4.91
    peso = 0.02
    dolar_australiano = 3.18
    dolar_canadense = 3.64
    franco = 0.42
    euro = 5.36
    libra = 6.21

    real = float(input('Qual o valor a ser convertido em reais? '))

    converte_moeda(real, dolar, 'dólares')
    converte_moeda(real, dolar_australiano, 'dólares australianos')
    converte_moeda(real, dolar_canadense, 'dólares canadenses')
    converte_moeda(real, peso, 'pesos')
    converte_moeda(real, franco, 'francos')
    converte_moeda(real, euro, 'euros')
    converte_moeda(real, libra, 'libras')

if __name__ == "__main__":
    main()