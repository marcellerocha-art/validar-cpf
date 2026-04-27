# Função que verifica se o CPF é válido
def validar_cpf(cpf):
    # Remove pontos e traços (deixa só números)
    cpf = cpf.replace(".", "").replace("-", "")
    
    # Primeiro teste:
    # Se não tiver 11 números ou se todos forem iguais → inválido
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # =========================
    # Verificando o 1º dígito
    # =========================
    soma = 0
    
    # Faz a conta com os 9 primeiros números
    # Multiplicando por pesos de 10 até 2
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    
    # Calcula o resultado final
    resto = (soma * 10) % 11
    
    # Se der 10, vira 0 (regra do CPF)
    if resto == 10:
        resto = 0
    
    # Compara com o dígito do CPF
    if resto != int(cpf[9]):
        return False

    # =========================
    # Verificando o 2º dígito
    # =========================
    soma = 0
    
    # Agora usa 10 números com pesos de 11 até 2
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    
    resto = (soma * 10) % 11
    
    if resto == 10:
        resto = 0
    
    # Compara com o último número do CPF
    if resto != int(cpf[10]):
        return False

    # Se passou por tudo → CPF válido
    return True


# Aqui começa o programa principal

# Pede o CPF pro usuário
cpf = input("Digite o CPF: ")

# Chama a função de validação
if validar_cpf(cpf):
    # Mostra se for válido
    print("CPF válido!")
else:
    # Mostra se for inválido
    print("CPF inválido!")