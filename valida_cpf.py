# valida o número do cpf com pontos e hífens
import re

# cpf = str("361702628-18")
cpf = str(input('Entre com o número do CPF, com pontos e hífen: \n'))
if re.search('-', cpf):
    cpf = cpf.replace('.', '').split('-')
    if re.search('\d{9}', cpf[0]) and re.search('\d{2}', cpf[1]):
        comparaDigitos = str(cpf[1])
        soma = 0
        digitos = [0, 0]

        for i in range(len(cpf[0])):
            soma += int(cpf[0][i]) * (10 - i)
        soma = soma % 11

        digitos[0] = 0 if soma <= 2 else (11 - soma)

        cpf = cpf[0]
        cpf += str(digitos[0])

        soma = 0

        for i in range(len(cpf)):
            soma += int(cpf[i]) * (11 - i)

        soma = soma % 11

        digitos[1] = 0 if soma <= 2 else (11 - soma)

        cpf += str(digitos[1])

        resutDigitos = cpf[9] + cpf[10]

        if (resutDigitos == comparaDigitos):
            print('Número CPF validado')
            input('Pressione ENTER para sair...')
        else:
            print('Número do CPF errado')
            input('Pressione ENTER para sair...')
    else:
        print('Quantidade de caracteres errada!')
        input('Pressione ENTER para sair...')
else:
    print('Insira um hífen para separa os digitos!')
    input('Pressione ENTER para sair...')
