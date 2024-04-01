n1 =  float (input("Digite a primeira nota do aluno: "))
n2 =  float (input("Digite a primeira nota do aluno: "))

media = (n1+n2)/2

if media >=6:
    print("Aprovado")
elif media <5:
    print("Reprovado")
else:
    print("Recuperação")