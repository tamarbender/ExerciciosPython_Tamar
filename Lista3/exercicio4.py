# Exercício 4 - Tuplas, Listas e Dicionários

# Crie um dicionário representando contatos (nome, telefone).
# Permita ao usuário procurar por um contato pelo nome.


def procurar_contato(contatos, nome):
    if nome in contatos:
        return contatos[nome]
    else:
        return "Contato não encontrado."

def main():
    # Inicializar o dicionário de contatos
    contatos = {
        "Reynaldo":  "123456789",
        "Iracema":   "987654321",
        "José Carlos":"777777777"
    }

    # Solicitar ao usuário o nome para procurar
    nome_procurado = input("Digite o nome do contato que deseja procurar: ")

    # Procurar o contato e imprimir o resultado
    resultado_procura = procurar_contato(contatos, nome_procurado)
    print(f"\nResultado da procura: {resultado_procura}")

if __name__ == "__main__":
    main()
