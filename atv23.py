# Crie um programa que receba um número do usuário e exiba a tabuada desse número de 1 a 10.
n=int(input("Digite um numero para ver a tabuada"))
for c in range(11):
    print(f"{n} x {c} = {n*c}")

