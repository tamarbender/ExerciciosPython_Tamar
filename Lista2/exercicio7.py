# Exercício 7 - Tomada de Decisão
# Desenvolver um programa que solicite a idade do usuário e identifique se
# ele é uma criança, um adolescente, adulto ou idoso.


def classificar_idade(idade):
    if idade < 0:
        return "Idade inválida"
    elif idade < 12:
        return "Criança"
    elif idade < 18:
        return "Adolescente"
    elif idade < 60:
        return "Adulto"
    else:
        return "Idoso"

def main():
    try:
        # Solicitar a idade ao usuário
        idade = int(input("Digite sua idade: "))
        
        # Classificar a idade e imprimir a categoria correspondente
        categoria = classificar_idade(idade)
        print(f"Você é considerado um(a) {categoria}.")
    except ValueError:
        print("Por favor, insira um valor numérico válido para a idade.")

if __name__ == "__main__":
    main()
