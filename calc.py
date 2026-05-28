def div ():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    print(a/b)
def mult ():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    print(a*b)
def soma ():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    print(a+b)
def sub ():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    print(a-b)
while True:
    print("\n=== Calculadora ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        soma()
    elif opcao == "2":
        sub()
    elif opcao == "3":
        mult()
    elif opcao == "4":
        div()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")