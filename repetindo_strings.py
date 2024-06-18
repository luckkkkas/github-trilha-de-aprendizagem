# Função que recebe uma string e um número, e repete a string o número de vezes especificado
def repetir_string_n_vezes():
    # Recebe a string do usuário
    string = input("Digite uma string: ")
    
    # Recebe o número de repetições
    n = int(input("Digite o número de repetições: "))
    
    # Repete a string o número de vezes especificado
    string_repetida = ' '.join([string] * n)
    
    # Retorna a string repetida
    return string_repetida

# Chama a função e exibe o resultado
resultado = repetir_string_n_vezes()
print("String repetida:", resultado)
