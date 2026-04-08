#Funções das operações da calculadora

def calculadora_soma(a, b):
    soma = a + b
    return soma

def calculadora_subtracao(a, b):
    subtracao = a - b
    return subtracao

def calculadora_multiplicacao(a, b):
    multiplicacao = a * b
    return multiplicacao

def calculadora_divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero!")
    
    divisao = a / b
    return divisao

#Função da expressão completa

def expressao_completa(a, b, operacao):
    try:
        if operacao == "+":
            return calculadora_soma(a, b)

        elif operacao == "-":
           return calculadora_subtracao(a, b)

        elif operacao == "x":
           return calculadora_multiplicacao(a, b)

        elif operacao == "/":
           return calculadora_divisao(a, b)

        else :
            return ("Insira uma operação válida!")

    except ValueError as e:
        return str(e)

def formatacao(valor):
    if valor.is_integer():
        return int(valor)
    
    return valor