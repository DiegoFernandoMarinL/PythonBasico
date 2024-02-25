a = "0"
cantidad = 0 
suma = 0

while a == "0":
    cantidad = cantidad + 1
    num = input("Digite número: ")
    suma = suma + int(num)
    a = input("Desea ingresar otro valor (Si=0  No=1): ")

promedio = suma/cantidad
print("El promedio de los datos ingresados es: ",promedio)