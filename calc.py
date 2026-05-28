def valores():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    return a, b
def div (a,b):
    return a/b
def mult (a,b):
    return a*b
def soma (a,b):
    return a+b
def sub (a,b):
    return a-b
while True:
    print("\n=== Calculadora ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao in ["1", "2", "3", "4"]:
        a, b = valores()
        if opcao == "1":
            print(f"Resultado: {a} + {b} = {soma(a, b)}")
        elif opcao == "2":
            print(f"Resultado: {a} - {b} = {sub(a, b)}")
        elif opcao == "3":
            print(f"Resultado: {a} * {b} = {mult(a, b)}")
        elif opcao == "4":
            if b == 0:
                print("Erro: Divisão por zero não é permitida.")    
            else:   
                print(f"Resultado: {a} / {b} = {div(a, b)}")
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")