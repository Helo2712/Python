import re




vem = float(input("Digete o valor do seu emprestimo: "))
sl = float(input("Digite o valor liquido do salario do solicitante do emprestimo: "))
qdp = int(input("Digite a quntidade de parcelas a serem pagas: "))
nc = str(input("Digete o nome completo do cliente: ")).title()
end = str(input("Digite o endereço do cliente: "))

continuar = True
while continuar:
        cpf = input("Digite o CPF do cliente: ")
        cpf = re.sub(r'/D',"",cpf)
else:
    continuar = False

continuar2 = True
while continuar2:
    tel = input("Digite o número de telefone do cliente: ")
    tel = re.sub(r'/D',"",tel)
if len(tel) != 11:
    print("Telefone invalido!")
else:
    continuar2 = False

continuar3 = True
while continuar3:
    cep = int(input("Digite o CEP do cliente: "))
    cep = re.sub(r'/D',"",cep)
if len(cep) != 8:
    print("CEP invalido!")
else:
    continuar3 = False

continuar4 = True
while continuar4:
    email = str(input("Digite o email so cliente: "))
    email = re.sub(r'/D',"",email)
if not email.endswith('@gmail.com'):
    print("email invalido!")
    email.lower()
else:
    continuar4 = False
    email.lower()



prestacao = vem / qdp

print(f"Nome:{nc}\nCPF:{cpf}\nTelefone{tel}\nCEP{cep}\nE-mail{email}\n")







