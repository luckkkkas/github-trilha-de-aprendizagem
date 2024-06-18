# Função que realiza a operação desejada
def calcular(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero não é permitida."
    else:
        return "Erro: Operação inválida."

# Função principal para receber os valores e a operação
def main():
    try:
        # Recebe os números do usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Recebe a operação desejada do usuário
        operacao = input("Digite a operação (+, -, *, /): ")
        
        # Realiza a operação e obtém o resultado
        resultado = calcular(num1, num2, operacao)
        
        # Exibe o resultado
        print("Resultado:", resultado)
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite números válidos.")

# Executa o programa principal
if __name__ == "__main__":
    main()
