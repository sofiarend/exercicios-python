positivos = 0 

while True:
        num = float(input("Digite um número ou 0 para sair: "))
        if num == 0:
            break
        if num > 0:
            positivos += 1
print(f"Quantidade de números positivos: {positivos}")