# Função que recebe dois valores e um separador opcional, e os concatena em uma string
def concatenar_valores():
    # Recebe o primeiro valor do usuário
    valor1 = input("Digite o primeiro valor: ")
    
    # Recebe o segundo valor do usuário
    valor2 = input("Digite o segundo valor: ")
    
    # Recebe um separador opcional do usuário
    separador = input("Digite um separador (opcional, pressione Enter para pular): ")
    
    # Concatena os valores com o separador ou sem, se não for fornecido
    if separador:
        string_concatenada = valor1 + separador + valor2
    else:
        string_concatenada = valor1 + valor2
    
    # Retorna a string concatenada
    return string_concatenada

# Chama a função e exibe o resultado
resultado = concatenar_valores()
print("String concatenada:", resultado)
