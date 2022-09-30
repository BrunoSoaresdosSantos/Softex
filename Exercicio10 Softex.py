def calculadora():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print("[1] para soma \n[2] para subtração \n[3] para mutiplicação \n[4] para divisão ")
    operacao = int(input("Digite a operação que irá fazer: "))

    if(operacao == 1):
        soma = n1 + n2
        print(soma)
    elif(operacao == 2):
        sub = n1 -n2
        print(sub)
    elif(operacao == 3):
        mut = n1* n2
        print(mut)
    elif(operacao == 4):
        div = n1/n2
        print(div)
    else:
        print("0")
calculadora()