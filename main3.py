num1 = input("Digite un número: ")
num1 = int(num1)
i = 1
factorial = 1
for i in range(num1):
    factorial = factorial * (i+1)
    i = i + 1
    
print("El factorial de ",num1," es: ",factorial )    
       

     