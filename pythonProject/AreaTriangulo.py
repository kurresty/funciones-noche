#Ejemplo para calcular el area del triangulo

#entradas
base = int(input("Ingrese la base del triangulo"))
altura = int(input("Ingrese la altura del triangulo"))


#proceso
def calcularAreaTriangulo(b,a):
    area = (b*a)/2
    #print("El area del triangulo es: ",area)
    return area
resultado = calcularAreaTriangulo(base,altura)
print(f"El area del triangulo es: {resultado}")