valor = float(input("Digite o valor da sua prestação:"))
taxa = float(input("Digite o valor da sua taxa:"))
tempo =int(input("Digite o tempo que sua prestação está atrasada:"))

print(f"O valor da sua prestação é: {valor+(valor*(taxa/100)*tempo)}")
