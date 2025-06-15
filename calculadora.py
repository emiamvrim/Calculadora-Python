# CALCULADORA
while True:
    numero_1 = input("Digite um numero: ")
    numero_2 = input("Digite outro numero: ")
    
    operações = input("Escolha uma operação: [+], [-], [*], [/] ")


    int_n1 = int(numero_1)
    int_n2 = int(numero_2)

    if operações == "+":
        soma = int_n1 + int_n2
        print(f'O resultado é: {numero_1} + {numero_2} = {soma: .0f}')

    if operações == "-":
     sub = int_n1 - int_n2
     print(f'O resultado é: {numero_1} - {numero_2} = {sub: .0f}')

    if operações == "*":
     multiplicacao = int_n1 * int_n2
     print(f'O resultado é: {int_n1} * {int_n2} = {multiplicacao: .0f}')

    if operações == "/":
        divisao = int_n1 / int_n2
        print(f'O resultado é: {int_n1} / {int_n2} = {divisao: .0f}')

    sair = input("Você deseja sair? (Sim/Não): ").strip().lower()

    if sair == "sim":
        print("Você saiu")
        break
    elif sair == "não":
        continue
    else:
        print("Resposta inválida. Digite 'Sim' ou 'Não'.")
