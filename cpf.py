# função para calcular o dígito verificador do CPF parcial
def calcular_digito_verificador(cpf_parcial):
    soma = 0
    multiplicador = len(cpf_parcial) + 1  # define o multiplicador inicial

    # itera sobre cada dígito do CPF parcial
    for digito in cpf_parcial:
        soma += int(digito) * multiplicador  # soma o número do dígito pelo multiplicador
        multiplicador -= 1  # decrementa o multiplicador
    resto_divisao = soma % 11  # calcula o resto da divisão
    if resto_divisao < 2:
        return '0'  # se o resto da divisão for menor que dois, retorna o dígito verificador calculado
    else:
        return str(11 - resto_divisao)  # caso contrário, retorna o dígito verificador calculado


# função para verificar se o CPF é válido
def verificar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')  # remove pontos e traços do CPF

    # verificar se o CPF tem 11 dígitos e se não contém caracteres não numéricos
    if len(cpf) != 11 or not cpf.isdigit():
        return False  # retorna False se o CPF não tiver 11 dígitos ou conter caracteres não numéricos

    cpf_parcial = cpf[:9]  # obtém os 9 primeiros dígitos do CPF

    digito1 = calcular_digito_verificador(cpf_parcial)  # calcula o primeiro dígito verificador
    cpf_parcial += digito1  # adiciona o primeiro verificador ao CPF parcial

    digito2 = calcular_digito_verificador(cpf_parcial)  # calcula o segundo dígito verificador
    cpf_calculado = cpf_parcial + digito2  # adiciona o segundo dígito ao CPF parcial
    return cpf == cpf_calculado  # retorna True se o CPF original for igual ao CPF calculado com os dígitos verificadores


# função principal
def main():
    cpf = input("Digite o CPF (apenas números): ")  # solicita ao usuário que insira o CPF

    if verificar_cpf(cpf):  # verifica se o CPF é válido
        print("CPF válido")
    else:
        print("CPF inválido")


if __name__ == "__main__":
    main()