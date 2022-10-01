operacao = 5
while(operacao != 0): 
    
    print("Escolha a opereção que deseja fazer.")
    operacao = int (input("[1] para soma \n[2] para subtração \n[3] para mutiplicação \n[4] para divisão \n[0] para sair\n"))
    
    if(operacao == 1 ):
        n1= float(input("Digite o primeiro número: "))
        n2= float(input("Digite o segundo número: "))
        print(n1,"+",n2,"=",n1+n2)
    
    elif(operacao == 2 ):
        n1= float(input("Digite o primeiro número: "))
        n2= float(input("Digite o segundo número: "))
        print(n1,"-",n2,"=",n1-n2)
    
    elif(operacao == 3 ):
        n1= float(input("Digite o primeiro número: "))
        n2= float(input("Digite o segundo número: "))
        print(n1,"*",n2,"=",n1*n2)
    
    elif(operacao == 4 ):
        n1= float(input("Digite o primeiro número: "))
        n2= float(input("Digite o segundo número: "))
        print(n1,"/",n2,"=",n1/n2)
    
    elif(operacao == 0):
        print("Saindo")
    
    else:
        print("Essa opção não existe!\n")
