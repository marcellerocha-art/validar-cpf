# Função que verifica se o CPF é válido
def validar_cpf(cpf):
    # Tirando pontos e traços (fica só número)
    cpf = cpf.replace(".", "").replace("-", "")

    # Verificação básica:
    # Se não tiver 11 números ou todos forem iguais → inválido
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # -------------------------
    # Conferindo o 1º dígito
    # -------------------------
    soma = 0

    # Faz a conta com os 9 primeiros números
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    # Calcula o resultado
    resto = (soma * 10) % 11

    # Se der 10, considera como 0
    if resto == 10:
        resto = 0

    # Vê se bate com o dígito do CPF
    if resto != int(cpf[9]):
        return False

    # -------------------------
    # Conferindo o 2º dígito
    # -------------------------
    soma = 0

    # Agora usa os 10 primeiros números
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    resto = (soma * 10) % 11

    if resto == 10:
        resto = 0

    # Confere com o último número do CPF
    if resto != int(cpf[10]):
        return False

    # Se passou em tudo, é válido
    return True


# Programa principal

# Pede o CPF para o usuário
cpf = input("Digite o CPF: ")

# Verifica se é válido
if validar_cpf(cpf):
    print("CPF válido!")
else:
    print("CPF inválido!")
