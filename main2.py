num1 = input("Digite primer número: ")
num1 = int(num1)
num2 = input("Digite segundo número: ")
num2 = int(num2)
num3 = input("Digite tercer número: ")
num3 = int(num3)

if (num1 > num2): 
    if (num1 > num3): 
        print ("El número mayor es: ",num1)
    elif (num2 < num3):
        print ("El número mayor es: ",num3)   
elif (num2 > num3):
    print ("El numero mayor es: ",num2)
else:
    print ("El numero mayor es: ",num3)    