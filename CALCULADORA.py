print("CALCULADORA")

ip = (input("Escolha a operação [ + - * /]"))

if  (ip=="+"):
    n1 = int(input("digite o primeiro número: "))
    n2 = int(input("digite o segundo número: "))
    resultado = n1+n2
    print("O resultado da equação é",resultado)
if  (ip=="-"):
    n1 = int(input("digite o primeiro número: "))
    n2 = int(input("digite o segundo número: "))
    resultado2 = n1-n2
    print("O resultado da equação é",resultado2)
if (ip=="/"):
    n1 = int(input("digite o primeiro número: "))
    n2 = int(input("digite o segundo número: "))
    resultado3 = n1/n2
    print("O resultado da equação é",resultado3)
if (ip=="*"):
    n1 = int(input("digite o primeiro número: "))
    n2 = int(input("digite o segundo número: "))
    resultado4 = n1*n2
    print("O resultado da equação é",resultado4)
print ("Fim")