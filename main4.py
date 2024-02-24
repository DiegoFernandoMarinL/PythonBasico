num1 = input("Digite un número: ")
num1 = int(num1)
pr = 0

for i in range(num1):
    i = i+1
    val = num1 % i
    if (val == 0):
        pr = pr + 1
       

if (pr == 2):
    print(num1," es primo")
else:
    print(num1," no es primo")    

