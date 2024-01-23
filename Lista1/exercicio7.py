# Exercício 7 - Conceitos Básicos de Python 

# Solicite ao usuário o peso em kg e a altura em metros. Calcule e
# imprima o Índice de Massa Corporal (IMC) usando a fórmula:
# IMC = peso / (altura x altura).

# Solicitar ao usuário o peso em kg e a altura em metros
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

# Calcular o Índice de Massa Corporal (IMC)
imc = peso / (altura ** 2)

# Exibir o resultado
print(f"\nO Índice de Massa Corporal (IMC) é: {imc:.2f}")
