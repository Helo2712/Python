v1 = float(input("Digite o seu primeiro valor: "))
v2 = float(input("Digite o seu segundo valor: "))

if v1<v2:
    print(f"{v2} é maior que {v1}")
elif v2 == v1:
    print(f"{v1} e {v2} são iguais")
else:
    print(f"{v1} é maior que {v2}")