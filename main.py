def validar_cartao(cartao):
    # Remover espaços
    cartao = cartao.replace(" ", "")
    
    # Verificar se todos os caracteres são dígitos
    if not cartao.isdigit():
        return "ERRO! Você digitou caracteres inválidos! Verifique e tente novamente."

    # Verificar se o comprimento do cartão está no intervalo adequado
    if len(cartao) < 13 or len(cartao) > 19:
        return "Número de cartão inválido. O comprimento do número do cartão deve ter entre 13 e 19 dígitos."

    # Inverter a string
    cartao_invertido = cartao[::-1]

    soma = 0
    # Para cada dígito, se o índice for ímpar (começando do final), multiplica-se por 2
    for i, digito in enumerate(cartao_invertido):
        num = int(digito)  # Converte o caractere para inteiro

        # Se o índice for ímpar (começando do final)
        if i % 2 == 1:
            num *= 2
            if num > 9:
                num -= 9  # Ajuste se o valor for maior que 9

        soma += num

    # Se a soma for divisível por 10, o cartão é válido
    if soma % 10 == 0:
        return True  # Cartão válido
    else:
        return False  # Cartão inválido


def identificar_bandeira(cartao):
    # Remover espaços (caso o número tenha sido inserido com espaços)
    cartao = cartao.replace(" ", "")
    
    # Verificar o comprimento do cartão
    if len(cartao) < 13 or len(cartao) > 19:
        return "Número de cartão inválido."

    # Identificar a bandeira com base nos primeiros dígitos
    if cartao.startswith("4"):
        return "Visa"
    elif cartao.startswith("5"):
        # MasterCard tem uma faixa de números de 2221 a 2720 para os prefixos
        if 2221 <= int(cartao[:4]) <= 2720 or cartao.startswith("5"):
            return "MasterCard"
    elif cartao.startswith("34") or cartao.startswith("37"):
        return "American Express"
    elif cartao.startswith("6"):
        return "Discover"
    elif cartao.startswith("36") or cartao.startswith("38") or cartao.startswith("39"):
        return "Diners Club"
    elif cartao.startswith("3528") or cartao.startswith("3589"):
        return "JCB"
    elif cartao.startswith("62"):
        return "UnionPay"
    elif cartao.startswith("50"):
        return "Carte Bancaire"
    elif cartao.startswith("60"):
        return "RuPay"
    elif cartao.startswith("6362") or cartao.startswith("5067") or cartao.startswith("4389"):
        return "Elo"
    else:
        return "Bandeira não identificada."


def processar_cartao(cartao):
    # 1. Validar o número do cartão
    valido = validar_cartao(cartao)
    if valido is not True:  # Se o cartão não for válido, retornar a mensagem de erro
        return valido

    # 2. Identificar a bandeira do cartão
    marca = identificar_bandeira(cartao)
    return f"Cartão válido! Marca: {marca}"


# Recebe o número do cartão do usuário
cartao = input("Digite o número do cartão: ")
resultado = processar_cartao(cartao)
print(resultado)
